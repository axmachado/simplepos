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

    Boolean and logical expressions and conditions

    @author: Alexandre Machado <axmachado@gmail.com>
"""
import logging

from .base import CodeGenerationError
from .variables import Assignment
from ..objfile import typedefs

# pylint: disable=C0103
# it's not a constant
logger = logging.getLogger("link")


# noinspection PyMethodMayBeStatic
class Conditional(object):
    """
    If and While - statements that require an conditional
    evaluation before the main block
    """
    def __init__(self):
        super(Conditional, self).__init__()

    def preConditionalCode(self, codeBlock, controlVariable=None):
        # pylint: disable=W0613
        """
        generate into the codeBlock the code to compute the conditional
        before emitting the comparison
        """
        pass

    def emit(self):
        # pylint: disable=R0201
        " emit the comparison attributes to the conditional instruction "
        return ""

    def negate(self):
        " Negate the expression, inverting it's logical value "
        pass

    def usesVariable(self, name):
        "check if condition uses a variable"
        return False

    def assignVariable(self, name):
        "check if condition assigns a value to a variable"
        return False

class ConstantConditional(Conditional):
    """
    The use of as Integer or Logical constant as condition.
    Zero is considered false, any other value is true
    """
    def __init__(self, value):
        super(ConstantConditional, self).__init__()
        self.value = value

    def negate(self):
        self.value = not self.value


class SimpleComparison(Conditional):
    """
    Compare the value of a variable to any value
    """

    # POSXML conditional operators constants
    # pylint: disable=C0103
    # those are really constants, but pylint thinks they are class attributes
    LT = 'lessthan'
    GT = 'greaterthan'
    EQ = 'equalto'
    NE = 'notequalto'
    GE = 'greaterthanorequalto'
    LE = 'lessthanorequalto'

    def __init__(self, left, op, right):
        super(SimpleComparison, self).__init__()

        if op == '<':
            self.operator = self.LT
        elif op == '>':
            self.operator = self.GT
        elif op == '==':
            self.operator = self.EQ
        elif op == '!=':
            self.operator = self.NE
        elif op == '>=':
            self.operator = self.GE
        elif op == '<=':
            self.operator = self.LE
        else:
            raise CodeGenerationError('Invalid operator "%s"', op)

        self.originalOperator = self.operator

        self._updateValues(left, right)

    def _updateValues(self, vLeft, vRight):
        """
        Update the values of the expression.

        Used by subclasses and when the simple comparison is used inside
        complex logical expression, when the values of the expression must
        be evaluated before the comparison
        """

        # in POSXML, the left side of a comparison must always be
        # a variable. So, if the left side of our expression is not a
        # variable, we must "invert" the expression
        invert = False
        if vLeft.startswith('$'):
            self.variable = vLeft
            self.value = vRight
        else:
            self.variable = vRight
            self.value = vLeft
            invert = True

        self.operator = self.originalOperator
        if invert:
            if self.operator == self.LT:
                self.operator = self.GT
            elif self.operator == self.GT:
                self.operator = self.LT
            elif self.operator == self.GE:
                self.operator = self.LE
            elif self.operator == self.LE:
                self.operator = self.GE

    def negate(self):
        """
        Negate the result of the comparison"
        """
        if self.operator == self.LT:
            self.operator = self.GE
        elif self.operator == self.GT:
            self.operator = self.LE
        elif self.operator == self.EQ:
            self.operator = self.NE
        elif self.operator == self.NE:
            self.operator = self.EQ
        elif self.operator == self.GE:
            self.operator = self.LT
        elif self.operator == self.LE:
            self.operator = self.GT
        self.originalOperator = self.operator

    def usesVariable(self, name):
        varInExpression = '$(' + name + ')'
        return (self.variable == varInExpression) \
               or (varInExpression in self.value)

    def emit(self):
        "emits the attributes for the POSXML tag"
        return 'variable="%s" operator="%s" value="%s"' % \
               (self.variable, self.operator, self.value)


class LogicalValueContext(object):
    """
    Context to process intermediate code generation for logical
    expressions and values
    """
    def __init__(self, codeBlock):
        super(LogicalValueContext, self).__init__()
        self.codeBlock = codeBlock

    def procNegatedValue(self, value):
        """
        Processes the negation of an expression value: !(expression)
        """
        # import here to avoid cyclic import problems
        from .control import IfStatement
        valueToNegate = self.procValue(value.value)
        if valueToNegate.startswith('$'):
            # the value is a variable. It's necessary to produce
            # an "if" statement
            condition = SimpleComparison('$(%s)' % valueToNegate, '==', '0')
            ifBlock = [Assignment(typedefs.INT, valueToNegate, '1')]
            elseBlock = [Assignment(typedefs.INT, valueToNegate, '0')]
            ifStm = IfStatement(self.codeBlock)
            ifStm.selfGenerated(condition, ifBlock, elseBlock)
            self.codeBlock.addStatements(ifStm)
            return valueToNegate
        else:
            return '1' if int(valueToNegate) == 0 else '0'

    def procRelationalExpression(self, value):
        "processes a relational expression"
        # import here to avoid cyclic import problems
        from .control import IfStatement

        exprResult = self.codeBlock.currentScope().autoInt()
        leftVal = self.procValue(value.left)
        rightVal = self.procValue(value.right)
        conditional = SimpleComparison(leftVal, value.operator, rightVal)

        ifBlock = [Assignment(typedefs.INT, exprResult, '1')]
        elseBlock = [Assignment(typedefs.INT, exprResult, '0')]

        ifStm = IfStatement(self.codeBlock)
        ifStm.selfGenerated(conditional, ifBlock, elseBlock)

        self.codeBlock.addStatements(ifStm)

        return "$(%s)" % exprResult

    def procLogicalExpression(self, value):
        "processes a logical expression"
        exprResult = self.codeBlock.currentScope().autoInt()
        logExpr = LogicalExpr(value.left, value.operator, value.right)
        logExpr.preConditionalCode(self.codeBlock, exprResult)
        return "$(%s)" % exprResult

    def procValue(self, value):
        "processes a logical value, generating intermediate code"
        result = None
        if not isinstance(value, typedefs.Value):
            result = str(value)
        elif isinstance(value, typedefs.Constant):
            result = str(value)
        elif isinstance(value, typedefs.VarValue):
            result = value.value
        elif isinstance(value, typedefs.FunctionReturnValue):
            varName = self.codeBlock.functionReturnVariable(value)
            result = '$(%s)' % varName
        elif isinstance(value, typedefs.ExpressionValue):
            varName = self.codeBlock.expressionReturnVariable(value)
            result = '$(%s)' % varName
        elif isinstance(value, typedefs.NegatedValue):
            result = self.procNegatedValue(value)
        elif isinstance(value, typedefs.RelationalExpressionValue):
            result = self.procRelationalExpression(value)
        elif isinstance(value, typedefs.LogicalExpressionValue):
            result = self.procLogicalExpression(value)
        return result


class SingleVariableCondition(SimpleComparison):
    """
    Condition represented by a single variable value
    """
    def __init__(self, variable):
        super(SingleVariableCondition, self).__init__(variable, '!=', '0')


class ConditionalFactory(object):
    """
    Factory to generate code for the condition
    """
    def __init__(self):
        super(ConditionalFactory, self).__init__()

    @staticmethod
    def canBeSimple(condition):
        # pylint: disable=R0201
        # It can really be a function (pylint-R0201), but I prefer it as a
        # method in order to encapsulate the conditional creation code
        # into the factory
        "Can the condition be a SimpleCoparison?"
        left = condition.left
        right = condition.right
        if isinstance(left, typedefs.VarValue):
            return isinstance(right, typedefs.Constant) \
                   or isinstance(right, typedefs.VarValue)

        elif isinstance(right, typedefs.VarValue):
            return isinstance(left, typedefs.Constant)

        else:
            return False

    @staticmethod
    def simpleValue(value):
        # pylint: disable=R0201
        # It can really be a function (pylint-R0201), but I prefer it as a
        # method in order to encapsulate the conditional creation code
        # into the factory
        "The condition is a single value"
        if isinstance(value, typedefs.Constant):
            return str(value.value)
        elif isinstance(value, typedefs.VarValue):
            return value.value
        return None

    def getConditional(self, condition):
        """
        Builds and return the Conditional object that represents
        this condition
        """
        if isinstance(condition, typedefs.Constant):
            try:
                value = int(condition.value) != 0
            except ValueError:
                value = False
            return ConstantConditional(value)
        elif isinstance(condition, typedefs.VarValue):
            return SingleVariableCondition('$(%s)' % condition.variable.name)
        elif isinstance(condition, typedefs.FunctionReturnValue):
            leftValue = condition
            rightValue = typedefs.IntConstant(0)
            return ValueComparison(leftValue, "!=", rightValue)
        elif isinstance(condition, typedefs.NegatedValue):
            cond = self.getConditional(condition.value)
            cond.negate()
            return cond
        elif isinstance(condition, typedefs.RelationalExpressionValue):
            if self.canBeSimple(condition):
                leftValue = self.simpleValue(condition.left)
                rightValue = self.simpleValue(condition.right)
                return SimpleComparison(leftValue, condition.operator,
                                        rightValue)
            else:
                return ValueComparison(condition.left, condition.operator,
                                       condition.right)
        elif isinstance(condition, typedefs.LogicalExpressionValue):
            return LogicalExpr(condition.left, condition.operator,
                               condition.right)


class ValueComparison(SimpleComparison):
    """
    Condition that represents the comparison of two values
    """
    def __init__(self, leftValue, op, rightValue):
        self.codeBlock = None
        self.leftValue = leftValue
        self.rightValue = rightValue
        super(ValueComparison, self).__init__("$(left)", op, "$(right)")

    def preConditionalCode(self, codeBlock, controlVariable=None):
        ctx = LogicalValueContext(codeBlock)
        leftValue = ctx.procValue(self.leftValue)
        rightValue = ctx.procValue(self.rightValue)
        self._updateValues(leftValue, rightValue)


class LogicalExpr(Conditional):
    """
    Logical expression - AND and OR operations
    """

    # pylint: disable=C0103
    # pylint thinks of OR and AND as class attributes, but they are constants
    OR = "||"
    AND = "&&"

    """
    Logical operation - AND, OR
    """
    def __init__(self, left, op, right):
        super(LogicalExpr, self).__init__()
        self.operator = op
        self.negated = False
        self.resultVar = None
        self.left = left
        self.right = right
        self.isNegated = False

    def orCode(self, codeBlock, cond1, cond2):
        """
        result = False
        if cond1:
            result = True
        else:
            if cond2:
               result = True
        """
        # import here to avoid cyclic import problems
        from .control import IfStatement
        codeBlock.addStatements(Assignment(typedefs.INT, self.resultVar,
                                           '0'))
        if1 = IfStatement(codeBlock)
        if2 = IfStatement(codeBlock)

        trueBlock = [Assignment(typedefs.INT, self.resultVar, '1')]
        if2.selfGenerated(cond2, trueBlock)

        elseBlock = [if2]
        if1.selfGenerated(cond1, trueBlock, elseBlock)
        codeBlock.addStatements(if1)

    def andCode(self, codeBlock, cond1, cond2):
        """
        result = False
        if cond1:
           if cond2:
              result = True
        """
        # import here to avoid cyclic import problems
        from .control import IfStatement

        codeBlock.addStatements(Assignment(typedefs.INT, self.resultVar, '0'))
        if1 = IfStatement(codeBlock)
        if2 = IfStatement(codeBlock)

        if2Block = [Assignment(typedefs.INT, self.resultVar, '1')]
        if2.selfGenerated(cond2, if2Block)

        if1Block = [if2]
        if1.selfGenerated(cond1, if1Block)
        codeBlock.addStatements(if1)

    def preConditionalCode(self, codeBlock, controlVariable=None):
        self.resultVar = (controlVariable, None) \
                         if controlVariable \
                         else codeBlock.currentScope().autoInt()

        ctx = LogicalValueContext(codeBlock)
        leftValue = ctx.procValue(self.left)
        rightValue = ctx.procValue(self.right)
        cond1 = SingleVariableCondition(leftValue)
        cond2 = SingleVariableCondition(rightValue)
        if self.operator == self.OR:
            self.orCode(codeBlock, cond1, cond2)
        else:
            self.andCode(codeBlock, cond1, cond2)

    def emit(self):
        operator = "notequals" if not self.isNegated else "equals"
        return 'variable="$(%s)" operator="%s" value="%s"' % \
               (self.resultVar, operator, "0")

    def negate(self):
        self.isNegated = not self.isNegated
