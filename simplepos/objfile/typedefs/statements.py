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


    Source level statements

    @author: Alexandre Machado <axmachado@gmail.com>

"""

from .types import INT, STRING, VOID, UNDEF
from .values import IntConstant, valueSetter, ExternalConstant
from .variables import variableSetter


def statementSetter(setter):
    "Decorator to validate a statement in a setter"
    def theSetter(self, value):
        "the real setter"
        if value and not isinstance(value, Statement):
            raise ValueError("The value must be an instance of Statement")
        setter(self, value)
    return theSetter


class Statement(object):
    "Any executable statement"
    def __init__(self):
        super(Statement, self).__init__()
        self.name = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name

    def replaceVariableReferences(self, varName, variable):
        """
        Replace all references of varName with variable.
        Used during the link phase to unify references to variables
        defined in other modules.

        :param varName: variable name
        :param variable: variable to be used.
        """
        pass

    def resolveExternalConstant(self, constantName, constantValue):
        """
        Resolve references to externally defined constants, replacing them
        with the value defined in the other module.

        Used in link phase.

        :param constantName: The name of the constant
        :param constantValue:  The value to be replaced
        """
        pass

    def replaceLinkedFunction(self, function):
        """
        Replace all references to function name with the linked function.

        Used in link time to resolve functions defined in other modules or
        after the call in this module.

        :param function: linked function
        """
        pass

    def containsReturn(self):
        """
        Check if the statement contains a "return" instruction and shoud
        end the current function;

        It makes sense only in block statements, but is defined here to
        provide an uniform interface to all statements.

        :return:
        """
        return False

class BreakStatement(Statement):
    "break statement"
    def __init__(self):
        super(BreakStatement, self).__init__()
        self.name = 'break'


class IncDecStatement(Statement):
    """
    Increment (ID++) or Decrement (ID--)
    """

    def __init__(self, variable, operator='++'):
        """
        Initializes the statement
        :param variable:  The variable to be incremented/decremented
        :param operator: the operator
        """
        super(IncDecStatement, self).__init__()
        self.variable = variable
        self.operator = operator

    @property
    def variable(self):
        "the variable"
        return self._variable

    @property
    def operator(self):
        "the operator"
        return self._operator

    @variable.setter
    @variableSetter
    def variable(self, variable):
        "sets the variable"
        self._variable = variable

    @operator.setter
    def operator(self, oper):
        if oper:
            if oper not in ('++', '--'):
                raise ValueError("Invalid unary operator: " + oper)
        self._operator = oper

    def __str__(self):
        return "%s%s" % (self.variable.name, self.operator)

    def replaceVariableReferences(self, varName, variable):
        if self.variable.name == varName:
            self.variable = variable


class ReturnStatement(Statement):
    """
    Return value from a function
    """
    def __init__(self, value):
        super(Statement, self).__init__()
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    @valueSetter
    def value(self, value):
        self._value = value

    def __str__(self):
        return "return %s" % str(self.value)

    def replaceVariableReferences(self, varName, variable):
        self.value.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        if isinstance(self.value, ExternalConstant):
            if self.value.name == constantName:
                self.value = constantValue

    def replaceLinkedFunction(self, function):
        self.value.replaceLinkedFunction(function)

    def containsReturn(self):
        return True # the return statement contains itself

class Assignment(Statement):
    """
    Assignment statement.
    variable = expression
    """
    def __init__(self, variable, value):
        super(Assignment, self).__init__()
        self._variable = None
        self._value = None
        self.variable = variable
        self.value = value

    @property
    def variable(self):
        return self._variable

    @variable.setter
    @variableSetter
    def variable(self, value):
        self._variable = value

    @property
    def value(self):
        return self._value

    @value.setter
    @valueSetter
    def value(self, value):
        self._value = value

    def __str__(self):
        return "%s = %s" % (self.variable.name, self.value)

    def replaceVariableReferences(self, varName, variable):
        if self.variable.name == varName:
            self.variable = variable
        self.value.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        if isinstance(self.value, ExternalConstant):
            if self.value.name == constantName:
                self.value = constantValue
        else:
            try:
                self.value.resolveExternalConstant(constantName, constantValue)
            except AttributeError:
                # não tem o método, ignorar
                pass

    def replaceLinkedFunction(self, function):
        self.value.replaceLinkedFunction(function)


class FunctionCall(Statement):
    """
    Function call statement.
    It's the calling of a "void" function, or the calling of a
    function without using the return value.
    """

    def __init__(self, function, *args):
        super(FunctionCall, self).__init__()
        self._returnType = None
        self._arguments = []
        self.name = function.name
        self.returnType = function.returnType
        self.arguments = args

    @property
    def returnType(self):
        "the return type of the function"
        return self._returnType

    @property
    def arguments(self):
        "the actual parameter values passed to the function call"
        return self._arguments

    @returnType.setter
    def returnType(self, value):
        "the return type"
        if value:
            if value not in (INT, STRING, VOID, UNDEF):
                raise ValueError("Invalid return type for function " +
                                 self.name)
        self._returnType = value

    @arguments.setter
    def arguments(self, value):
        "the parameters"
        self._arguments.clear()
        if value:
            if not hasattr(value, '__iter__'):
                raise ValueError("The argument list must be iterable")
            for arg in value:
                self.addArgument(arg)

    @valueSetter
    def addArgument(self, arg):
        "add one argument to the arguments list"
        if arg is not None:
            self.arguments.append(arg)

    def __str__(self):
        return "%s (%s)" % (self.name, ", ".join([
                                            str(x) for x in self.arguments]))

    def replaceVariableReferences(self, varName, variable):
        for argument in self.arguments:
            argument.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        for i in range(len(self.arguments)):
            argument = self.arguments[i]
            if isinstance(argument, ExternalConstant):
                if argument.name == constantName:
                    self.arguments[i] = constantValue
            else:
                try:
                    argument.resolveExternalConstant(constantName,
                                                     constantValue)
                except AttributeError:
                    pass

    def replaceLinkedFunction(self, function):
        if self.name == function.name:
            self.returnType = function.returnType

        for argument in self.arguments:
            argument.replaceLinkedFunction(function)

class IfThenElse(Statement):
    """
    if/then/else construction

    conditional block of statements
    """
    def __init__(self):
        super(IfThenElse, self).__init__()
        self.condition = IntConstant(1)
        self.ifBlock = None
        self.elseBlock = None

    @property
    def condition(self):
        "the condition"
        return self._condition

    @property
    def ifBlock(self):
        "the block executed if the condition is true"
        return self._ifBlock

    @property
    def elseBlock(self):
        "the block executed if the condition if false"
        return self._elseBlock

    @condition.setter
    @valueSetter
    def condition(self, value):
        "condition"
        self._condition = value

    @ifBlock.setter
    def ifBlock(self, value):
        "if block"
        from ..block import BlockStatement
        if value:
            if not isinstance(value, BlockStatement):
                raise ValueError("The IF block must be a "
                                 "BlockStatement instance")
        self._ifBlock = value

    @elseBlock.setter
    def elseBlock(self, value):
        "else block"
        from ..block import BlockStatement
        if value:
            if not isinstance(value, BlockStatement):
                raise ValueError("The else block must be a "
                                 "BlockStatement instance")
        self._elseBlock = value

    def createIfBlock(self, namedScope):
        "create an empty if block"
        from ..block import BlockStatement
        self.ifBlock = BlockStatement(namedScope)
        return self.ifBlock

    def createElseBlock(self, namedScope):
        "create an empty else block"
        from ..block import BlockStatement
        self.elseBlock = BlockStatement(namedScope)
        return self.elseBlock

    def prefixedPrint(self, prefix):
        "print the statement in human readable form"
        lines = ['if %s' % self.condition]
        blockLines = str(self.ifBlock).split("\n")
        lines.extend(blockLines)
        if self.elseBlock:
            lines.append('else')
            blockLines = str(self.elseBlock).split("\n")
            lines.extend(blockLines)
        prefixed = [prefix + x for x in lines]
        return "\n".join(prefixed)

    def replaceVariableReferences(self, varName, variable):
        self.condition.replaceVariableReferences(varName, variable)
        if self.ifBlock:
            self.ifBlock.replaceVariableReferences(varName, variable)
        if self.elseBlock:
            self.elseBlock.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        self.condition.resolveExternalConstant(constantName, constantValue)
        if self.ifBlock:
            self.ifBlock.resolveExternalConstant(constantName, constantValue)
        if self.elseBlock:
            self.elseBlock.resolveExternalConstant(constantName, constantValue)

    def replaceLinkedFunction(self, function):
        self.condition.replaceLinkedFunction(function)
        if self.ifBlock:
            self.ifBlock.replaceLinkedFunction(function)
        if self.elseBlock:
            self.elseBlock.replaceLinkedFunction(function)

    def containsReturn(self):
        if (self.ifBlock):
            if self.ifBlock.containsReturn():
                return True
        if (self.elseBlock):
            if self.elseBlock.containsReturn():
                return True
        return False

    def processReturnStatement(self, insertBreak = False):
        if self.ifBlock:
            self.ifBlock.processReturnStatement(insertBreak)
        if self.elseBlock:
            self.elseBlock.processReturnStatement(insertBreak)

    def __str__(self):
        return self.prefixedPrint("")


class WhileStatement(Statement):
    """
    while - repetition
    """

    def __init__(self):
        super(WhileStatement, self).__init__()
        self._condition = None
        self._block = None
        self.condition = IntConstant(1)

    @property
    def condition(self):
        "the condition"
        return self._condition

    @property
    def block(self):
        "the repeated block"
        return self._block

    @condition.setter
    @valueSetter
    def condition(self, value):
        self._condition = value

    @block.setter
    def block(self, value):
        from ..block import BlockStatement
        if value:
            if not isinstance(value, BlockStatement):
                raise ValueError("The IF block must be a "
                                 "BlockStatement instance")
        self._block = value

    def __str__(self):
        return ('while %s\n' % self.condition) + str(self.block)

    def replaceVariableReferences(self, varName, variable):
        self.condition.replaceVariableReferences(varName, variable)
        self.block.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        self.condition.resolveExternalConstant(constantName, constantValue)
        self.block.resolveExternalConstant(constantName, constantValue)

    def replaceLinkedFunction(self, function):
        self.condition.replaceLinkedFunction(function)
        self.block.replaceLinkedFunction(function)

    def containsReturn(self):
        return self.block.containsReturn()

    def processReturnStatement(self, insertBreak):
        if self.block:
            self.block.processReturnStatement(True)

class ForStatement(WhileStatement):
    """
    for - repetition
    for ( initialization; condition; increment)
    """

    def __init__(self):
        super(ForStatement, self).__init__()
        self._initialization = None
        self._increment = None

    @property
    def initialization(self):
        return self._initialization

    @initialization.setter
    @statementSetter
    def initialization(self, value):
        self._initialization = value

    @property
    def increment(self):
        return self._increment

    @increment.setter
    @statementSetter
    def increment(self, value):
        self._increment = value

    def __str__(self):
        return ('for (%s, %s, %s)\n' % (self.initialization, self.condition,
                                        self.increment)) + str(self.block)

    def replaceVariableReferences(self, varName, variable):
        super(ForStatement, self).replaceVariableReferences(varName, variable)
        if self.initialization:
            self.initialization.replaceVariableReferences(varName, variable)
        if self.increment:
            self.increment.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, constantName, constantValue):
        super(ForStatement, self).resolveExternalConstant(constantName,
                                                          constantValue)
        if self.initialization:
            self.initialization.resolveExternalConstant(constantName,
                                                        constantValue)
        if self.increment:
            self.increment.resolveExternalConstant(constantName, constantValue)

    def replaceLinkedFunction(self, function):
        super(ForStatement,self).replaceLinkedFunction(function)
        if self.initialization:
            self.initialization.replaceLinkedFunction(function)
        if self.increment:
            self.increment.replaceLinkedFunction(function)
