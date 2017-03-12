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

    Representation of values

    @author: Alexandre Machado <axmachado@gmail.com>

"""

from .types import (STRING, INT, UNDEF, usableInAssignment)


def valueSetter(setter):
    "Decorator to validate a value in a setter"
    def theSetter(self, value):
        "the real setter"
        if value and not isinstance(value, Value):
            raise ValueError("The value must be an instance of Value")
        try:
            if value.type_ != self.type_:
                if value.type_ == UNDEF:
                    value.type_ = self.type_
                else:
                    raise ValueError("Incorrect type. Expected " +
                                     self.type_)
        except AttributeError:
            # ignore, because self does not have a type_
            pass
        setter(self, value)
    return theSetter


class Value(object):
    """
    Any value that can be stored into a variable
    or passed as parameter

    Attributes:
        type_: the type of the value.
    """
    def __init__(self, type_=STRING):
        self.type_ = type_

    @property
    def type_(self):
        "The type of the value"
        return self._type_

    @type_.setter
    @usableInAssignment
    def type_(self, vType):
        self._type_ = vType

    def replaceVariableReferences(self, varName, variable):
        """
           replace variable references because the variable
           was linked with another
        """
        #  placeholder to be overwiten
        pass

    def resolveExternalConstant(self, name, value):
        """
        placeholder to be override by subclass
        """

class Constant(Value):
    """
    A generic constant value

    Attributes:
        type_: inherited - the type of the value

        value:  the value of the constant
    """

    def __init__(self, type_=STRING, theValue=None):
        super(Constant, self).__init__(type_)
        self.value = theValue

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.type_ == INT:
            self._value = str(int(value))
        else:
            self._value = str(value)

    def __str__(self):
        return str(self.value)


class ExternalConstant(Constant):
    """
    Externally defined constant
    """
    def __init__(self, name, type_=STRING):
        super(ExternalConstant, self).__init__(type_);
        self.name = name

    def __str__(self):
        return "external(%s)" % self.name

class IntConstant(Constant):
    "Integer constant"
    def __init__(self, intValue):
        super(IntConstant, self).__init__(INT, intValue)


class StringConstant(Constant):
    "String constant"
    def __init__(self, strValue):
        super(StringConstant, self).__init__(STRING, strValue)


class VarValue(Value):
    """
    The value of a variable

    Attributes:

        type_ (inherited): the type of the value

        variable: the variable whose value is represented here

        value: the value as represented in POSXML syntax
    """
    def __init__(self, variable):
        super(VarValue, self).__init__(variable.type_)
        self.variable = variable

    @property
    def value(self):
        "The value of the variable"
        return '$(%s)' % self.variable.name

    def __str__(self):
        return self.variable.name

    def replaceVariableReferences(self, varName, variable):
        if varName == self.variable.name:
            self.variable = variable


class FunctionReturnValue(Value):
    """
    The return value of a function call

    Attributes:

        type_ (inherited): the type of the value: the return type of the
                               function called.

        functionCall: the functionCall statement whose return value we
                      represent

    """
    def __init__(self, functionCall):
        self.functionCall = functionCall
        super(FunctionReturnValue, self).__init__(functionCall.returnType)

    @property
    def value(self):
        "the value"
        return self.functionCall

    @property
    def type_(self):
        return self.functionCall.returnType

    @type_.setter
    def type_(self, vtype):
        if self.type_ == UNDEF:
            self.functionCall.returnType = vtype
        else:
            if vtype != self.type_:
                raise ValueError("You can't change the return type of a "
                                 "defined function")

    def __str__(self):
        return str(self.functionCall)

    def replaceVariableReferences(self, varName, variable):
        if self.functionCall:
            self.functionCall.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, name, value):
        if self.functionCall:
            self.functionCall.resolveExternalConstant(name, value)

class BinaryExpressionValue(Value):
    """
    Return value of an expression

    Attributes:

        left: the left side value

        operator: the operator (as seen in the source code)

        right: the right side value
    """
    def __init__(self):
        super(BinaryExpressionValue, self).__init__(INT)
        self.left = None
        self.operator = None
        self.right = None

    @property
    def left(self):
        "Left side of the expression"
        return self._left

    @property
    def right(self):
        "Right site of the expression"
        return self._right

    @property
    def operator(self):
        "The operator"
        return self._operator

    @left.setter
    @valueSetter
    def left(self, value):
        "left side"
        self._left = value

    @right.setter
    @valueSetter
    def right(self, value):
        "right side"
        self._right = value

    @operator.setter
    def operator(self, value):
        "operator"
        if value is not None and (not self._validateOperator(value)):
            raise ValueError("Invalid operator " + str(value))
        self._operator = value

    def __str__(self):
        return "(%s %s %s)" % (str(self.left), self.operator, str(self.right))

    def _validateOperator(self, value):
        # pylint: disable=R0201
        "Check if the operator is valid for this kind of expression"
        # Any value except the empty string is valid here. The subclasses
        # will override this method to validate.
        if value:
            return len(str(value)) > 0
        else:
            return True

    def setAll(self, left, oper, right):
        "set all attributes at once"
        self.left = left
        self.operator = oper
        self.right = right

    def replaceVariableReferences(self, varName, variable):
        self.left.replaceVariableReferences(varName, variable)
        self.right.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, name, value):
        newValues = []
        for localValue in self.left, self.right:
            newValue = localValue
            if isinstance(localValue, ExternalConstant):
                if localValue.name == name:
                    newValue = value
            else:
                try:
                    self.left.resolveExternalConstant(name, value)
                except AttributeError:
                    pass
            newValues.append(newValue)

        self.left = newValues[0]
        self.right = newValues[1]


class ExpressionValue(BinaryExpressionValue):
    """
    Return value of an arithmetic expression

    @see BinaryExpressionValue
    """
    VALID_OPS = {'+', '-', '*', '/', '^', '%'}

    def __init__(self):
        super(ExpressionValue, self).__init__()

    def _validateOperator(self, value):
        return value in self.VALID_OPS


class NegatedValue(Value):
    """
    Negation of a logical value
    """
    def __init__(self, value):
        super(NegatedValue, self).__init__(INT)
        self.value = value

    @property
    def value(self):
        "the value"
        return self._value

    @value.setter
    @valueSetter
    def value(self, value):
        "the value"
        if value.type_ != INT:
            raise ValueError("Only int typed values can be negated")
        self._value = value

    def __str__(self):
        return '! %s' % str(self.value)

    def replaceVariableReferences(self, varName, variable):
        self.value.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, name, value):
        if isinstance(self.value, ExternalConstant):
            if self.value.name == name:
                self.value = value
        else:
            try:
                self.value.resolveExternalConstant(name, value)
            except AttributeError:
                pass


class LogicalExpressionValue(BinaryExpressionValue):
    "Logical expression A (AND|OR) B"
    def __init__(self):
        super(LogicalExpressionValue, self).__init__()

    def _validateOperator(self, value):
        return value == '&&' or value == '||'


class RelationalExpressionValue(BinaryExpressionValue):
    "Relational expression - comparison"

    VALID_OPS = {'>', '<', '>=', '<=', '==', '!='}

    def __init__(self):
        super(RelationalExpressionValue, self).__init__()

    def _validateOperator(self, value):
        return value in self.VALID_OPS
