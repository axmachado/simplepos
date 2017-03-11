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

import unittest
from simplepos.objfile.typedefs import (INT, IntConstant,
                                        StringConstant, Variable, VarValue,
                                        FunctionCall, FunctionReturnValue,
                                        ExpressionValue, NegatedValue,
                                        LogicalExpressionValue,
                                        RelationalExpressionValue)
from simplepos.objfile import Function


class ValuesModuleTest(unittest.TestCase):

    def setUp(self):
        pass

    def testConstants(self):
        intConstant = IntConstant('10')
        self.assertEquals('10', intConstant.value)
        try:
            intConstant = IntConstant('x')
            self.fail("ValueError expected")
        except ValueError:
            # ok, expected
            pass
        strConstant = StringConstant("x101")
        self.assertEquals("x101", strConstant.value)

    def testVarValue(self):
        variable = Variable("test", INT)
        value = VarValue(variable)
        self.assertEquals(INT, value.type_)

    def testFunctionReturnValue(self):
        theFunction = Function(INT)
        theFunction.name = "testeFunction"
        fcall = FunctionCall(theFunction)
        fval = FunctionReturnValue(fcall)
        self.assertEquals(INT, fval.type_)

    def testExpressionValue(self):
        ic1 = IntConstant(1)
        ic2 = IntConstant(2)
        is1 = StringConstant("s")

        expr = ExpressionValue()
        expr.setAll(ic1, "+", ic2)
        self.assertEquals("+", expr.operator)
        self.assertEquals(INT, expr.type_)

        try:
            expr.right = is1
            self.fail("ValueError expected")
        except ValueError:
            # ok - expected
            pass

        try:
            expr.operator = '>'
            self.fail("ValueError expected")
        except ValueError:
            pass

    def testNegatedValue(self):
        ic1 = IntConstant(10)
        negValue = NegatedValue(ic1)
        self.assertIsNotNone(negValue)

        is1 = StringConstant("s")
        try:
            negValue = NegatedValue(is1)
            self.fail("ValueError expected")
        except ValueError:
            pass

    def testLogicalExpression(self):
        ic1 = IntConstant(1)
        ic2 = IntConstant(2)
        expr = LogicalExpressionValue()
        expr.setAll(ic1, '&&', ic2)
        self.assertEquals("&&", expr.operator)
        try:
            expr.operator = '!='
            self.fail("ValueError expected")
        except ValueError:
            pass

    def testRelationalExpression(self):
        ic1 = IntConstant(1)
        ic2 = IntConstant(2)
        expr = RelationalExpressionValue()
        expr.setAll(ic1, '>=', ic2)
        self.assertEquals(">=", expr.operator)

        try:
            expr.operator = '+'
            self.fail("ValueError expected")
        except ValueError:
            pass
