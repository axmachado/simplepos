# -*- coding: utf-8 -*-
"""
    Copyright © 2017 - Alexandre Machado <axmachado@gmail.com>

    This file is part of Simple POS Compiler.

    Simnple POS Compiler is free software: you can redistribute iti
    and/or modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, either version 3
    of the License, or (at your option) any later version.

    Simple POS Compiler is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Simple POS Compiler. If not, see <http://www.gnu.org/licenses/>.


    @author: Alexandre Machado <axmachado@gmail.com>

    Linked module data structure
"""

import logging
from ..objfile.typedefs import (INT, VOID, Variable, Assignment,
                                IntConstant, StringConstant)
from ..objfile.functions import BuiltinFunction
from ..codegen import POSXMLCode
from .callgraph import CallGraph

logger = logging.getLogger("linker")

class LinkerException(Exception):
    "All link errors"
    def __init__(self, message):
        super(LinkerException, self).__init__(message)


class LinkedModule(object):
    # pylint: disable=R0902
    # disables pylint check of too many instance attributes
    "Linked POSXML module or application"
    def __init__(self):
        self.mainModule = None
        self.globalVars = {}
        self.functions = []
        self.allFunctions = {}
        self.statements = []
        self.unresolvedFunctions = []
        self.linkedModules = []
        self.linkedFunctions = {}
        self.definedConstants = {}
        self.finalName = None
        self.callGraph = None

    def addModule(self, module):
        "Add an object module to the linked module"
        if module.name:
            if self.mainModule:
                msg = ("Only one main module is allowed." +
                       "You tryed to link %s and %s") % \
                       (module.name, self.mainModule.name)
                raise LinkerException(msg)
            else:
                logger.info ("Defining %s as main module", module.name)
                self.mainModule = module
                if not self.finalName:
                    self.finalName = module.name + ".posxml"
        logger.debug ("adding module to list")
        self.linkedModules.append(module)

    def loadAllGlobals(self, module):
        "Load all module variables as globals"
        logger.info ("Loading global variables")
        for var in module.variables.values():
            logger.debug ("   defining %s", var)
            if var.name in self.globalVars:
                existingVar = self.globalVars[var.name]
                logger.debug ("        already exists as %s. "
                              "Replacing references", existingVar)
                if existingVar.type_ != var.type_:
                    raise LinkerException("Global variable with conflicting "
                                          "type in module" + module.name)
                module.replaceVariableReferences(var.name, existingVar)
            else:
                self.globalVars[var.name] = var

    def loadAllFunctions(self, module):
        "Load all module functions"
        logger.info ("Loading functions")
        for function in module.functions.values():
            logger.debug ("   %s", function.name)
            self.functions.append(function)
        for function in module.externalFunctions.values():
            logger.debug ("   reference to %s", function.name)
            self.unresolvedFunctions.append(function)

    def loadAllConstants(self, module):
        logger.info ("Loading constants")
        for name, constant in module.constants.items():
            if name in self.definedConstants:
                existingConstant = self.definedConstants[name]
                if existingConstant.value != constant.value:
                    raise LinkerException("Redefined constant " + name)
            else:
                logger.debug ("    defining %s as %s", name, constant)
                self.definedConstants[name] = constant

    def checkDuplicateFunctions(self):
        "Check duplicate function names"
        logger.debug ("Checking for duplicate functions")
        functionNames = [f.name for f in self.functions]
        visited = set()
        dups = set()
        for name in functionNames:
            if name not in visited:
                visited.add(name)
            else:
                dups.add(name)
        if len(dups) > 0:
            raise LinkerException("Function name conflicts: %s" %
                                  ", ".join(dups))

        self.allFunctions = {f.name: f for f in self.functions}

    def findLinkedFunctions(self):
        "Find all functions that must be linked"
        logger.info ("Finding functions that will be linked")
        from simplepos.api import findApiFunction
        if not self.mainModule:
            raise LinkerException("Undefined main module")
        allCalled = [ x for x in self.mainModule.calledFunctions ]
        while len(allCalled) > 0:
            fname = allCalled.pop()
            if fname in self.linkedFunctions:
                continue
            try:
                theFunction = findApiFunction(fname)
                logger.debug ("    API function %s", fname)
            except KeyError:
                if fname in self.allFunctions:
                    logger.debug ("    User defined %s", fname)
                    theFunction = self.allFunctions[fname]
                    if theFunction.returnType != VOID:
                        returnVarName = "%s_return" % theFunction.name
                        returnVar = Variable(returnVarName,
                                             theFunction.returnType)
                        self.globalVars[returnVarName] = returnVar
                    allCalled.extend(theFunction.calledFunctions)
                else:
                    raise LinkerException("Undefined function: %s" % fname)
            self.linkedFunctions[fname] = theFunction

    def resolveUnresolved(self):
        """
        Check if all unresolved functions on individual modules where linked
        together into the final module
        """
        logger.info ("Resolving function references")
        for i in self.unresolvedFunctions:
            logger.debug ("    %s", i.name)
            if i.name not in self.linkedFunctions:
                logger.info ("Undefined function %s referenced in some module." % i.name)

        for function in self.linkedFunctions.values():
            if isinstance(function, BuiltinFunction):
                continue
            for stm in self.statements:
                stm.replaceLinkedFunction(function)

            for lfunction in self.linkedFunctions.values():
                if isinstance(lfunction, BuiltinFunction):
                    continue
                lfunction.replaceLinkedFunction(function)

        logger.info ("Resolving constant references")
        for name,constant in self.definedConstants.items():
            logger.debug ("    %s = %s", name, constant)
            for statement in self.mainModule.statements:
                statement.resolveExternalConstant(name, constant)

            for function in self.linkedFunctions.values():
                function.resolveExternalConstant(name, constant)

    def _buildCallGraph(self, callGraph, visited):
        if callGraph.name == '__main__':
            function = self.mainModule
        else:
            function = self.linkedFunctions[callGraph.name]

        visited.append(callGraph.name)

        for calledName in function.calledFunctions:
            functionNode = callGraph.findNode(calledName)
            if not functionNode:
                if calledName not in self.linkedFunctions:
                    # not linked: must be API function
                    # and API functions do not go into
                    # call graph
                    continue
                functionNode = CallGraph(calledName)
            callGraph.addCall(functionNode)
            if calledName not in visited:
                self._buildCallGraph(functionNode, visited)

    @staticmethod
    def resolveNameConflictsForFunction(function, existingList,
                                        suffix=""):
        genCount = 0
        for argument in function.arguments.values():
            if argument.name in existingList:
                newName = function.name + '_' + str(genCount) + '_' + suffix
                genCount += 1
                oldName = argument.name
                var = argument.variable
                var.name = newName
                function.replaceVariableReferences(oldName,
                                                   argument.variable)
        for variable in function.variables.values():
            if variable.name in existingList:
                newName = function.name + '_' + str(genCount) + '_' + suffix
                genCount += 1
                oldName = variable.name
                variable.name = newName
                function.replaceVariableReferences(oldName, variable)

    def resolveLocalGlobalOveralp(self):
        for function in self.linkedFunctions.values():
            self.resolveNameConflictsForFunction(function,
                                                 self.globalVars.keys())

    def resolveLocalCalledOverlap(self, node, visitedNodes, localVars):
        # First, go to all functions on this level and rename based on
        # the local vars here. Only after that go down one level
        for item in node.called:
            function = self.linkedFunctions[item.name]
            self.resolveNameConflictsForFunction(function, localVars,
                                                 node.name)
        for item in node.called:
            function = self.linkedFunctions[item.name]
            # appending a node as visited will prevent the linker to
            # loop on recursive functions. On the other side, it can cause
            # overlaps on recursive and indirectly recursive functions with
            # unpredictable results because POSXML has no STACK!.
            self.resolveLocalCalledOverlap(item, [*visitedNodes, node],
                                           [*localVars, *function.argumentList,
                                            *(function.variables.keys())])

    def renameVariables(self):
        """
        Rename the variables to avoid conflicts within funcion calls
        """
        logger.info ("Renaming variables to avoid conflicts")
        self.resolveLocalGlobalOveralp()
        self.callGraph = CallGraph('__main__')
        self._buildCallGraph(self.callGraph, [])
        self.resolveLocalCalledOverlap(self.callGraph, [], [])

    def doLink(self):
        """
        execute the linking process
        """
        otherModulesStatements = []
        for module in self.linkedModules:
            self.loadAllGlobals(module)
            self.loadAllFunctions(module)
            self.loadAllConstants(module)
            if module == self.mainModule:
                # copy the statements to avoid modifying the module
                # during the optimization process
                self.statements = [stm for stm in module.statements]
            else:
                otherModulesStatements.extend(module.statements)
                for function in module.calledFunctions:
                    self.mainModule.callFunction(function)
        self.statements.extend(otherModulesStatements)

        self.checkDuplicateFunctions()
        self.findLinkedFunctions()
        self.resolveUnresolved()
        self.renameVariables()

    def genCode(self):
        """
        call the code generator in order to produce the output file
        """
        logger = logging.getLogger("codegen")
        logger.info ("Starting code generation")
        gen = POSXMLCode(name='__main__', linkedFunctions=self.linkedFunctions)
        # initialization of global variables
        allVars = {var.name: var for var in self.globalVars.values()}
        for functionName in self.linkedFunctions:
            function = self.linkedFunctions[functionName]
            if not isinstance(function, BuiltinFunction):
                allVars.update({arg.name: arg for arg in function.arguments.values()})

        logger.info ("Initialization of used variables")
        for variable in allVars.values():
            if variable.type_ == INT:
                value = IntConstant(0)
            else:
                value = StringConstant("")
            assign = Assignment(variable, value)
            logger.debug ("   %s", assign)
            gen.statement(assign)

        logger.info("__main__ statements")
        for stm in self.mainModule.statements:
            logger.debug ("    %s", stm)
            gen.statement(stm)

        logger.info ("functions")
        for function in self.linkedFunctions.values():
            if not isinstance(function, BuiltinFunction):
                logger.debug ("    %s", function.name)
                gen.function(function)
        gen.generate(self.finalName)
