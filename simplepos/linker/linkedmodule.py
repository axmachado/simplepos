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

from ..objfile.typedefs import (INT, VOID, Variable, Assignment,
                                IntConstant, StringConstant)
from ..codegen import POSXMLCode
from .callgraph import CallGraph


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
                self.mainModule = module
                if not self.finalName:
                    self.finalName = module.name + ".posxml"
        self.linkedModules.append(module)

    def loadAllGlobals(self, module):
        "Load all module variables as globals"
        for var in module.variables.values():
            if var.name in self.globalVars:
                existingVar = self.globalVars[var.name]
                if existingVar.type_ != var.type_:
                    raise LinkerException("Global variable with conflicting "
                                          "type in module" + module.name)
                module.replaceVariableReferences(var.name, existingVar)
            else:
                self.globalVars[var.name] = var

    def loadAllFunctions(self, module):
        "Load all module functions"
        for function in module.functions.values():
            self.functions.append(function)
        for function in module.externalFunctions.values():
            self.unresolvedFunctions.append(function)

    def checkDuplicateFunctions(self):
        "Check duplicate function names"
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
        from simplepos.api import findApiFunction
        if not self.mainModule:
            raise LinkerException("Undefined main module")
        for fname in self.mainModule.calledFunctions:
            try:
                theFunction = findApiFunction(fname)
            except KeyError:
                if fname in self.allFunctions:
                    theFunction = self.allFunctions[fname]
                else:
                    raise LinkerException("Undefined function: %s" % fname)
            self.linkedFunctions[fname] = theFunction
            if theFunction.returnType != VOID:
                returnVarName = "%s_return" % theFunction.name
                returnVar = Variable(returnVarName, theFunction.returnType)
                self.globalVars[returnVarName] = returnVar

    def resolveUnresolved(self):
        """
        Check if all unresolved functions on individual modules where linked
        together into the final module
        """
        for i in self.unresolvedFunctions:
            if i.name not in self.linkedFunctions:
                raise LinkerException("Undefined function %s" % i)

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
        self.resolveLocalGlobalOveralp()
        self.callGraph = CallGraph('__main__')
        self._buildCallGraph(self.callGraph, [])
        self.resolveLocalCalledOverlap(self.callGraph, [], [])

    def doLink(self):
        """
        execute the linking process
        """
        for module in self.linkedModules:
            self.loadAllGlobals(module)
            self.loadAllFunctions(module)
            if module == self.mainModule:
                # copy the statements to avoid modifying the module
                # during the optimization process
                self.statements = [stm for stm in module.statements]

        self.checkDuplicateFunctions()
        self.findLinkedFunctions()
        self.resolveUnresolved()
        self.renameVariables()

    def genCode(self):
        """
        call the code generator in order to produce the output file
        """
        gen = POSXMLCode(name='__main__', linkedFunctions=self.linkedFunctions)
        # initialization of global variables
        for variable in self.globalVars.values():
            if variable.type_ == INT:
                value = IntConstant(0)
            else:
                value = StringConstant("")

            assign = Assignment(variable, value)
            gen.statement(assign)

        for stm in self.mainModule.statements:
            gen.statement(stm)
        for function in self.linkedFunctions.values():
            gen.function(function)
        gen.generate(self.finalName)
