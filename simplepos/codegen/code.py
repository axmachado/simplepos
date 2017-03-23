# -*- coding: utf-8 -*-
"""
    Copyright © 2017 - Alexandre Machado <axmachado@gmail.com>

    This file is part of Simple POS Compiler.

    Simnple POS Compiler is free software: you can redistribute it
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

    Code Generator
"""

import logging

from ..objfile import typedefs
from .variables import (Assignment, IncrementDecrement)
from .functions import (FunctionCall, MathematicalOperation,
                        FunctionDefinition)
from .scope import POSXMLCodeScope

# pylint: disable=C0103
logger = logging.getLogger("codegen")


class POSXMLCode(object):
    """
    Generated code block
    """
    def __init__(self, parentCodeBlock=None, name='main', linkedFunctions=None):
        self.scopes = []
        self.name = name
        self.functionDefinition = None
        self.linkedFunctions = linkedFunctions
        self.parentCodeBlock = parentCodeBlock
        if parentCodeBlock:
            # if we have a parent block, the first scope on our list
            # is the current scope of the parent block
            self.scopes.append(parentCodeBlock.currentScope())
            # we enter a new scope for this block.
            self.enterScope()
        else:
            # main block. Initializing the first scope
            self.scopes.append(POSXMLCodeScope(self))
        self.statements = []

    def __str__(self):
        return "CodeBlock (%s) - %d scopes" % (self.name, len(self.scopes))

    def addStatements(self, *args):
        " add one or more statements to the end of the block "
        self.statements.extend(args)

    def enterScope(self):
        " enter a new scope "
        scope = POSXMLCodeScope(self)
        scope.parentScope = self.currentScope()
        self.scopes.append(scope)
        return scope

    def currentScope(self):
        " get the current scope "
        return self.scopes[-1]

    def exitScope(self):
        """
        exit a scope, considering unused the automatic variables
        created in it.
        """
        scopeToExit = self.scopes.pop()
        current = self.currentScope()
        # push up the user variables defined in the scope
        # if we are not exiting the code block
        if scopeToExit.codeBlock == current.codeBlock:
            for var in scopeToExit.userVariables:
                current.userVariables.add(var)
        return scopeToExit

    def function(self, f):
        stmgen = FunctionDefinition(self, f)
        self.addStatements(stmgen)

    def findLinkedFunction(self, name):
        result = None
        if self.linkedFunctions:
            try:
                result = self.linkedFunctions[name]
            except KeyError:
                pass  # not found
        if not result:
            if self.parentCodeBlock:
                return self.parentCodeBlock.findLinkedFunction(name)
        return result

    def functionCall(self, callInstance, returnVariableName):
        " generate code for a function call "
        from ..objfile.typedefs import STRING, INT
        logger.debug ("      generating code for %s", callInstance)
        argValues = [self.procValue(i) for i in callInstance.arguments]
        theFunction = self.findLinkedFunction(callInstance.name)
        if returnVariableName is None:
            if theFunction.returnType == STRING:
                returnVariableName = self.currentScope().autoString()
            elif theFunction.returnType == INT:
                returnVariableName = self.currentScope().autoInt()
        stmgen = FunctionCall(callInstance,theFunction,
                              returnVariableName, *argValues)
        self.addStatements(*stmgen.beforeFunctionCall())
        self.addStatements(stmgen)
        self.addStatements(*stmgen.afterFunctionCall())

    def functionReturnVariable(self, value):
        " generate a return variable to a function call "
        functionCall = value.functionCall
        retval = None
        if functionCall.returnType == typedefs.INT:
            retval = self.currentScope().autoInt()
        elif functionCall.returnType == typedefs.STRING:
            retval = self.currentScope().autoString()

        self.functionCall(functionCall, retval)
        return retval

    def expressionReturnVariable(self, value):
        " generate a return variable to an expression "
        retval = self.currentScope().autoInt()
        # new scope to process the values
        self.enterScope()
        vleft = self.procValue(value.left)
        vright = self.procValue(value.right)
        op = value.operator
        stmgen = MathematicalOperation(vleft, op, vright, retval)
        self.addStatements(stmgen)
        self.exitScope()
        return retval

    def procValue(self, value):
        " processes a value and generate the intermediate code to compute it "
        from ..linker.linkedmodule import LinkerException
        if isinstance(value, typedefs.Constant):
            if isinstance(value, typedefs.ExternalConstant):
                raise LinkerException("Unresolved external constant " + value.name)
            return str(value)
        elif isinstance(value, typedefs.VarValue):
            return '$(%s)' % str(value.variable.name)
        elif isinstance(value, typedefs.FunctionReturnValue):
            return '$(%s)' % self.functionReturnVariable(value)
        elif isinstance(value, typedefs.ExpressionValue):
            return '$(%s)' % self.expressionReturnVariable(value)
        return ""

    def assignment(self, stm):
        "generate code for assignments"
        v = stm.value
        self.currentScope().addUserVariable(stm.variable.name)
        # enter a new scope to deal with the temporary created by the procValue
        self.enterScope()
        stmgen = Assignment(stm.variable.type_, stm.variable.name,
                            self.procValue(v))
        logger.debug ("      assignment: %s = '%s'", stm.variable, stmgen.value)
        self.addStatements(stmgen)
        # clean up the temporary variables created here.
        self.exitScope()

    def returnStatement(self, stm):
        v = stm.value
        self.enterScope()
        functionBlock = self
        while not functionBlock.functionDefinition:
            functionBlock = functionBlock.parentCodeBlock
        returnVarName = '%s_return' % functionBlock.name
        stmgen = Assignment(v.type_, returnVarName, self.procValue(v))
        logger.debug ("      assignment: %s %s = '%s'",
                      v.type_, returnVarName, stmgen.value)

        self.addStatements(stmgen)
        self.exitScope()

    def ifThenElse(self, stm):
        "generate code for if/then/else statement"
        # import here to avoid cyclic import problems
        from .control import IfStatement
        stmgen = IfStatement(self)
        stmgen.processIf(stm)
        self.addStatements(stmgen)

    def whileStatement(self, stm):
        "generate code for while statement"
        # import here to avoid cyclic import problems
        from .control import WhileStatement
        stmgen = WhileStatement(self)
        stmgen.processWhile(stm)
        self.addStatements(stmgen)

    def breakStatement(self):
        "generate code for break statement"
        # import here to avoid cyclic import problems
        from .control import BreakStatement
        stmgen = BreakStatement()
        self.addStatements(stmgen)

    def incrementDecrement(self, stm):
        "generate code for increment/decrement statement"
        v = stm.variable
        op = stm.operator
        stmgen = IncrementDecrement(v.name, op)
        self.addStatements(stmgen)

    def statement(self, stm):
        "Generate code for an object module statement"
        # create a scope to deal with statement temporary variables
        self.enterScope()
        if isinstance(stm, typedefs.Assignment):
            self.assignment(stm)
        elif isinstance(stm, typedefs.FunctionCall):
            self.functionCall(stm, None)
        elif isinstance(stm, typedefs.IfThenElse):
            self.ifThenElse(stm)
        elif isinstance(stm, typedefs.WhileStatement):
            self.whileStatement(stm)
        elif isinstance(stm, typedefs.BreakStatement):
            self.breakStatement()
        elif isinstance(stm, typedefs.IncDecStatement):
            self.incrementDecrement(stm)
        elif isinstance(stm, typedefs.ReturnStatement):
            self.returnStatement(stm)
        # exit the scope, allowing the reuse of the variables
        self.exitScope()

    def emitStatement(self):
        result = []
        for stm in self.statements:
            result.extend(stm.emitStatement())
        return result

    def removeDuplicateAssignments(self):
        toRemove = []
        lastAssignment = None
        for statement in self.statements:
            if isinstance(statement,Assignment):
                if lastAssignment and \
                                statement.variable == lastAssignment.variable:
                    logger.debug ("Removing assignment %s = %s",
                                  lastAssignment.variable, lastAssignment.value)
                    toRemove.append(lastAssignment)
                lastAssignment = statement
            else:
                lastAssignment = None
        for statement in toRemove:
            self.statements.remove(statement)

    def removeSpuriousTemporary(self):
        toRemove = []
        if len(self.statements) > 1:
            for i in range(len(self.statements) - 1):
                stm1 = self.statements[i]
                stm2 = self.statements[i+1]
                if (isinstance(stm1, Assignment) and
                        isinstance(stm2, Assignment)):
                    if stm2.value == '$(' + stm1.variable + ')':
                        logger.debug ("elimiating %s = %s", stm1.variable,
                                      stm1.value)
                        stm2.value = stm1.value
                        toRemove.append(stm1)
        for statement in toRemove:
            self.statements.remove(statement)

    def optimizeAssignments(self):
        logger.debug ("Removing duplicate assignments")
        self.removeDuplicateAssignments()
        self.removeSpuriousTemporary()

        logger.debug ("Optimizing inner blocks")
        for stm in self.statements:
            if stm.blocks():
                for block in stm.blocks():
                    block.optimizeAssignments()



    def generate(self, fileName):
        "Emits all POSXML instructions to a file"
        self.optimizeAssignments()

        from simplepos.codegen.writer import POSXMLWriter
        writer = POSXMLWriter(fileName, self.statements)
        writer.write()
