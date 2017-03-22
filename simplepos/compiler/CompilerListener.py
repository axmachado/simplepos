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

    ANTLR4 listener to AST walker.

    It's the main code of the compiler, and does the semantic analysis and
    some of the synthesis of the code while constructing the Module object.
"""

import sys
import logging
from .SimplePOSListener import SimplePOSListener, SimplePOSParser
from ..objfile import (UndefinedFunction, InvalidCallException, Module,
                       DuplicateVariableException, BlockStatement,
                       Function)
from ..objfile.typedefs import (INT, STRING, VOID, UNDEF,
                                ExternalConstant,
                                StringConstant, IntConstant, VarValue,
                                FunctionReturnValue, ExpressionValue,
                                RelationalExpressionValue,
                                LogicalExpressionValue,
                                NegatedValue, Assignment, FunctionCall,
                                BreakStatement, IncDecStatement, IfThenElse,
                                WhileStatement, ForStatement, ReturnStatement)


logger = logging.getLogger("compiler")

# Utility functions:


def typeFromTypename(ctx: SimplePOSParser.TypenameContext):
    "Get the type from the input token"
    # we have only to real types: int, string and void
    text = ctx.getText();
    if text == 'int':
        return INT
    elif text == 'string':
        return STRING
    elif text == 'void':
        return VOID
    else:
        return UNDEF;


def firstNonNull(itemList):
    "Get the first non null item from an iterable"
    for item in itemList:
        if item is not None:
            return item
    return None


class CompilerListener(SimplePOSListener):
    # pylint: disable=R0904
    # disables pylint too many public methods warning
    """
    Main compiler class: traverses the AST from ANTLR4 to construct
    the Module object
    """

    def __init__(self, sourceFile, objFile):
        """
        Initializes the status of the listener

        Attrs initialized:
           module: the Module object that will be constructed
           scope: initially, its the empty module
           stacks used during the compilation
        """
        self.module = Module(sourceFile, objFile)
        self.scope = self.module
        # stack to compile multiple scopes
        self.scopeStack = []
        # stack to store values while compiling expressions and function calls
        self.valueStack = []
        # stack to store old values where compiling function calls
        self.callStack = []
        # current function when compiling functions
        self.currentFunction = None
        # constant definitions
        self.constants = {}

    def _enterScope(self, scope):
        if scope != self.scope:
            logger.debug ("Entering scope")
            self.scopeStack.append(self.scope)
            scope.parentScope = self.scope
            self.scope = scope

    def _exitScope(self):
        logger.debug ("Exiting scope")
        if len(self.scopeStack) == 0:
            self.scope = self.module
        else:
            self.scope = self.scopeStack.pop()

    def _printError(self, line, column, message):
        print("%s (%d,%d) ERROR: %s" % (self.module.sourceFile, line,
                                        column + 1, message))

    # Enter a parse tree produced by SimplePOSParser#moduledef.
    def enterModuledef(self, ctx: SimplePOSParser.ModuledefContext):
        self.module.name = ctx.ID().getText()
        self._enterScope(self.module)

    # Exit a parse tree produced by SimplePOSParser#moduledef.
    def exitModuledef(self, ctx: SimplePOSParser.ModuledefContext):
        self._exitScope()

    # Enter a parse tree produced by SimplePOSParser#functiondef.
    def enterFunctiondef(self, ctx: SimplePOSParser.FunctiondefContext):
        if ctx.typename():
            returnType = typeFromTypename(ctx.typename());
        else:
            returnType = VOID
        theFunction = Function(returnType)
        theFunction.name = ctx.ID().getText()
        self._enterScope(theFunction)

    # Exit a parse tree produced by SimplePOSParser#functiondef.
    def exitFunctiondef(self, ctx: SimplePOSParser.FunctiondefContext):
        theFunction = self.scope
        theFunction.processReturnStatement()
        self._exitScope()
        self.module.addFunction(theFunction)

    # Enter a parse tree produced by SimplePOSParser#argdef.
    def enterArgdef(self, ctx: SimplePOSParser.ArgdefContext):
        argType = typeFromTypename(ctx.typename())
        isRef = ctx.REFMARK() is not None
        argName = ctx.ID().getText()

        self.scope.addArgument(argName, argType, isRef)

    # Enter a parse tree produced by SimplePOSParser#vardef.
    def enterVardef(self, ctx: SimplePOSParser.VardefContext):
        self.valueStack.append([])

    # Exit a parse tree produced by SimplePOSParser#vardef.
    def exitVardef(self, ctx: SimplePOSParser.VardefContext):
        definedVars = self.valueStack.pop()
        for (varName, value) in definedVars:
            try:
                self.scope.addVariable(varName,
                                       typeFromTypename(ctx.typename()))
                variable = self.scope.findVariable(varName)
                if value:
                    statement = Assignment(variable, value)
                    self.scope.addStatement(statement)
            except DuplicateVariableException as ex:
                self._printError(ctx.start.line, ctx.start.column, str(ex))
                sys.exit(1)

    # Exit a parse tree produced by SimplePOSParser#vardef_item.
    def exitVardef_item(self, ctx: SimplePOSParser.Vardef_itemContext):
        varName = ctx.ID().getText()
        value = None
        if ctx.ASSIGN():
            value = self.valueStack.pop()
        self.valueStack[-1].append((varName, value))

    # Exit a parse tree produced by SimplePOSParser#value.
    def exitValue(self, ctx: SimplePOSParser.ValueContext):
        value = None
        if ctx.STRVALUE():
            # we have a string constant
            strVal = ctx.STRVALUE().getText()[1:-1]
            value = StringConstant(strVal)

        if value:
            self.valueStack.append(value)

    # Exit a parse tree produced by SimplePOSParser#atom.
    def exitAtom(self, ctx: SimplePOSParser.AtomContext):
        value = None
        if ctx.TRUE():
            value = IntConstant(1)
        elif ctx.FALSE():
            value = IntConstant(0)
        elif ctx.ID():
            # we have an ID - it's a variable
            varName = ctx.ID().getText()
            if varName in self.constants:
                value = self.constants[varName]
            else:
                try:
                    var = self.scope.findVariable(varName)
                except KeyError:
                    self._printError(ctx.start.line, ctx.start.column,
                                     "undefined variable %s" % varName)
                    # this error aborts the compiler
                    sys.exit(1)
                value = VarValue(var)
        elif ctx.intvalue():
            # we have an integer constant
            intVal = int(ctx.intvalue().getText())
            value = IntConstant(intVal)
        elif ctx.functioncall():
            # we have a function call
            fcall = self.callStack.pop()
            value = FunctionReturnValue(fcall)

        if value:
            self.valueStack.append(value)

    def expressionOperation(self, ctx, expConstructor=ExpressionValue):
        "Generate an value from an expression"
        rvalue = self.valueStack.pop()
        lvalue = self.valueStack.pop()
        value = expConstructor()
        value.left = lvalue
        value.right = rvalue
        value.operator = ctx.getText()
        self.valueStack.append(value)

    # Exit a parse tree produced by SimplePOSParser#rexp.
    def exitRexp(self, ctx: SimplePOSParser.RexpContext):
        if ctx.EXP():
            self.expressionOperation(ctx.EXP())

    # Exit a parse tree produced by SimplePOSParser#log_rel.
    def exitLog_rel(self, ctx: SimplePOSParser.Log_relContext):
        opContext = firstNonNull([ctx.GT(), ctx.LT(), ctx.GE(),
                                  ctx.LE(), ctx.EQ(), ctx.NE()])
        if opContext:
            self.expressionOperation(opContext, RelationalExpressionValue)

    # Exit a parse tree produced by SimplePOSParser#log_oper.
    def exitLog_oper(self, ctx: SimplePOSParser.Log_operContext):
        opContext = firstNonNull([ctx.AND(), ctx.OR()])
        if opContext:
            self.expressionOperation(opContext, LogicalExpressionValue)

    # Exit a parse tree produced by SimplePOSParser#log_expression.
    def exitLog_expression(self, ctx: SimplePOSParser.Log_expressionContext):
        if ctx.NOT():
            logVal = self.valueStack.pop()
            value = NegatedValue(logVal)
            self.valueStack.append(value)

    # Exit a parse tree produced by SimplePOSParser#times_div.
    def exitTimes_div(self, ctx: SimplePOSParser.Times_divContext):
        opContext = firstNonNull([ctx.TIMES(), ctx.SLASH(), ctx.MOD()])
        if opContext:
            self.expressionOperation(opContext)

    # Exit a parse tree produced by SimplePOSParser#add_sub.
    def exitAdd_sub(self, ctx: SimplePOSParser.Add_subContext):
        opContext = firstNonNull([ctx.PLUS(), ctx.MINUS()])
        if opContext:
            self.expressionOperation(opContext)

    # Exit a parse tree produced by SimplePOSParser#Assignment.
    def exitAssignment(self, ctx: SimplePOSParser.AssignmentContext):
        if not self.scope:
            # ensures that the scope exists
            self.scope = self.module

        varName = ctx.ID().getText()
        try:
            var = self.scope.findVariable(varName)
        except KeyError:
            self._printError(ctx.start.line, ctx.start.column,
                             "undefined variable %s" % varName)
            sys.exit(1)

        value = self.valueStack.pop()
        if not value:
            self._printError(ctx.start.line, ctx.start.column,
                             "empty assignment")
            sys.exit(1)

        if var.type_ != value.type_:
            if value.type_ == UNDEF:
                value.type_ = var.type_
            else:
                self._printError(ctx.start.line, ctx.start.column,
                                 "Wrong type assignment: (%s = %s) %s = %s." %
                                 (var.type_, value.type_, var.name,
                                  value))
                sys.exit(1)
        stm = Assignment(var, value)
        self.scope.addStatement(stm)

    # Exit a parse tree produced by SimplePOSParser#returnstm.
    def exitReturnstm(self, ctx: SimplePOSParser.ReturnstmContext):
        value = self.valueStack.pop()
        stm = ReturnStatement(value)
        self.scope.addStatement(stm)

    # Enter a parse tree produced by SimplePOSParser#functioncall.
    def enterFunctioncall(self, ctx: SimplePOSParser.FunctioncallContext):
        self.callStack.append(self.valueStack)
        self.valueStack = []

    # Exit a parse tree produced by SimplePOSParser#functioncall.
    def exitFunctioncall(self, ctx: SimplePOSParser.FunctioncallContext):
        functionName = ctx.ID().getText()
        function = self.module.findFunction(functionName)
        args = self.valueStack
        self.valueStack = self.callStack.pop()
        if isinstance(function, UndefinedFunction):
            function.infereArgumentTypes(args)
        else:
            try:
                function.validateCall(*args)
            except InvalidCallException as ex:
                self._printError(ctx.start.line, ctx.start.column, str(ex))
                sys.exit(1)
        callInstance = FunctionCall(function, *args)
        self.callStack.append(callInstance)
        self.scope.callFunction(functionName)

    # Exit a parse tree produced by SimplePOSParser#stmline.
    def exitStmline(self, ctx: SimplePOSParser.StmlineContext):
        if ctx.functioncall():
            stm = self.callStack.pop()
            self.scope.addStatement(stm)
        elif ctx.BREAK():
            stm = BreakStatement()
            self.scope.addStatement(stm)
        elif ctx.INCOPER() or ctx.DECOPER():
            varName = ctx.ID().getText()
            operator = ctx.INCOPER() if ctx.INCOPER() else ctx.DECOPER()
            variable = self.scope.findVariable(varName)
            stm = IncDecStatement(variable, operator.getText())
            self.scope.addStatement(stm)
            # we will not addStatement for an attribution because the
            # attribution method already does it.

    # Enter a parse tree produced by SimplePOSParser#blockstm.
    def enterBlockstm(self, ctx: SimplePOSParser.BlockstmContext):
        block = BlockStatement(self.scope)
        self._enterScope(block)

    # Exit a parse tree produced by SimplePOSParser#blockstm.
    def exitBlockstm(self, ctx: SimplePOSParser.BlockstmContext):
        block = self.scope
        self._exitScope()
        self.scope.addStatement(block)

    # Exit a parse tree produced by SimplePOSParser#ifelse.
    def exitIfelse(self, ctx: SimplePOSParser.IfelseContext):
        elseBlock = None
        if ctx.ELSE():
            elseBlock = self.scope.popStatement()
        ifBlock = self.scope.popStatement()
        condition = self.valueStack.pop()
        ifStm = IfThenElse()
        ifStm.ifBlock = ifBlock
        ifStm.elseBlock = elseBlock
        ifStm.condition = condition
        self.scope.addStatement(ifStm)

    # Exit a parse tree produced by SimplePOSParser#whilestm.
    def exitWhilestm(self, ctx: SimplePOSParser.WhilestmContext):
        block = self.scope.popStatement()
        condition = self.valueStack.pop()
        whileStm = WhileStatement()
        whileStm.condition = condition
        whileStm.block = block
        self.scope.addStatement(whileStm)

    # Exit a parse tree produced by SimplePOSParser#forstm.
    def exitForstm(self, ctx: SimplePOSParser.ForstmContext):
        block = self.scope.popStatement()
        increment = self.scope.popStatement()
        condition = self.valueStack.pop()
        initialization = self.scope.popStatement()

        stm = ForStatement()
        stm.initialization = initialization
        stm.condition = condition
        stm.increment = increment
        stm.block = block
        self.scope.addStatement(stm)

    # Exit a parse tree produced by SimplePOSParser#constdef_item.
    def exitConstdef_item(self, ctx: SimplePOSParser.Constdef_itemContext):
        constName = ctx.ID().getText()
        if ctx.intvalue():
            constValue = IntConstant(ctx.intvalue().getText())
        else:
            constValue = StringConstant(ctx.STRVALUE().getText()[1:-1])
        self.constants[constName] = constValue
        self.module.addLocalConstant(constName, constValue)

    # Exit a parse tree produced by SimplePOSParser#constdef.
    def exitConstdef(self, ctx: SimplePOSParser.ConstdefContext):
        if ctx.EXTERN():
            names = [x.getText() for x in ctx.ID()]
            type = typeFromTypename(ctx.typename())
            for item in names:
                constant = ExternalConstant(item, type)
                self.module.addExternalConstant(item, constant)
                self.constants[item] = constant
