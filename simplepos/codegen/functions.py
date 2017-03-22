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

"""
import logging
from ..api import findApiFunction
from .base import POSXMLStatement, emitTag
from ..objfile.typedefs import INT, STRING

logger = logging.getLogger("linker")


class FunctionCall(POSXMLStatement):
    """
    Function call statement, with the return value processing
    """
    def __init__(self, functionCall, calledFunction, returnVariable, *args):
        super(FunctionCall, self).__init__()
        self.functionCall = functionCall
        self.calledFunction = calledFunction
        self.returnVariable = returnVariable
        self.paramValues = args
        try:
            fcn = findApiFunction(functionCall.name)
            self.isApiFunction = True
        except KeyError:
            self.isApiFunction = False

    def usesVariable(self, name):
        result = False
        varReference = '$(' + name + ')'
        for value in self.paramValues:
            if varReference in value:
                result = True
                break
        return result

    def assignsVariable(self, name):
        return name == self.returnVariable

    def _emitApiFunctionCall(self, apiFcn):
        """
        Emits a function call to a POSXML api function
        """
        attributes = {}
        if apiFcn.returnAttribute:
            attributes[apiFcn.returnAttribute] = '$(%s)' % self.returnVariable

        if apiFcn.fixedAttributes:
            for attr, value in apiFcn.fixedAttributes.items():
                attributes[attr] = str(value)

        for i in range(len(self.paramValues)):
            argument = apiFcn.arguments[apiFcn.argumentList[i]]
            attributes[argument.name] = self.paramValues[i]

        attributesPart = []
        for attr in attributes:
            attributesPart.append('%s="%s"' % (attr, attributes[attr]))

        return ('<%s %s />' % (apiFcn.tagName, " ".join(attributesPart)),)

    def beforeFunctionCall(self):
        from .variables import Assignment
        result = []
        if not self.isApiFunction:
            assignInit = None
            if (self.functionCall.returnType == STRING):
                assignInit = ""
            elif (self.functionCall.returnType == INT):
                assignInit = 0

            if assignInit is not None:
                assign = Assignment(self.functionCall.returnType,
                                    self.returnVariable, assignInit)
                result.append(assign)

            for (param, value) in zip(self.calledFunction.orderedArgumentList(),
                                      self.paramValues):
                assign = Assignment(param.type_, param.name, value)
                result.append(assign)
        return result

    def afterFunctionCall(self):
        from .variables import Assignment
        result = []
        if not self.isApiFunction:
            if self.returnVariable:
                functionReturn = "$(%s_return)" % self.calledFunction.name
                assign = Assignment(self.functionCall.returnType,
                                    self.returnVariable, functionReturn)
                result.append(assign)
        return result

    def _emitUserFunctionCall(self):
        """
        Emits a function call to a user defined function
        """
        logger.info ("Emitting function call for function %s",
                     self.functionCall.name)
        return ['<callfunction name="%s" />' % self.functionCall.name]

    def emitStatement(self):
        """
        Generates the function call statement
        """
        try:
            fcn = findApiFunction(self.functionCall.name)
            return self._emitApiFunctionCall(fcn)
        except KeyError:
            return self._emitUserFunctionCall()


class MathematicalOperation(POSXMLStatement):
    "Arithmetic operation"
    def __init__(self, left, operator, right, returnVariable):
        super(MathematicalOperation, self).__init__()
        self.left = left
        self.operator = operator
        self.right = right
        self.returnVariable = returnVariable

    def usesVariable(self, name):
        varReference = '$(' + name + ')'
        return varReference in self.left or varReference in self.right

    def assignsVariable(self, name):
        return name == self.returnVariable

    def emitStatement(self):
        "emits the statement"
        attributes = ['firstvalue', 'operator', 'secondvalue',
                      'variabledestination']

        values = [self.left, self.operator, self.right, "$(%s)" %
                  self.returnVariable]
        return emitTag('mathematicaloperation', attributes, values)


class FunctionDefinition(POSXMLStatement):

    def __init__(self, mainModule, function):
        from .code import POSXMLCode
        from .variables import Assignment
        super(FunctionDefinition, self).__init__()
        self.function = function
        self.name = function.name
        self.functionCode = POSXMLCode(mainModule, self.name)
        self.functionCode.functionDefinition = self
        for variable in function.variables.values():
            initVal = "0" if variable.type_ == INT else ""
            self.functionCode.addStatements(Assignment(variable.type_,
                                                       variable.name, initVal))

        for stm in self.function.statements:
            self.functionCode.statement(stm)

    def blocks(self):
        return (self.functionCode,)

    def emitStatement(self):
        result = []
        logger.debug("Emiting function %s", self.function.name)
        result.append('<function name="%s">' % self.function.name)
        codeBlock = self.functionCode.emitStatement()
        result.extend(["    " + line for line in codeBlock])
        result.append('</function>')
        logger.debug("End function %s", self.function.name)
        return result
