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
from simplepos.objfile.typedefs.types import usableInExpression
from simplepos.objfile.typedefs.values import valueSetter
from simplepos.objfile.typedefs import (INT, VOID, IntConstant)


class UsableInExpressionTestClass(object):

    def __init__(self):
        self.setterCalled = False

    @usableInExpression
    def setType(self, value):
        self.setterCalled = True


class ValueSetterTestClass(object):

    def __init__(self):
        self.setterCalled = False

    @valueSetter
    def setValue(self, value):
        self.setterCalled = True


class TypesModuleTest(unittest.TestCase):

    def setUp(self):
        pass

    def testUsableInExpression(self):
        instance = UsableInExpressionTestClass()

        try:
            instance.setType(VOID)
            self.fail("It was supossed to raise an exception")
        except ValueError:
            # Ok, we where expecting it
            pass

        self.assertFalse(instance.setterCalled)

        try:
            instance.setType(INT)
        except ValueError as err:
            self.fail(err)

        self.assertTrue(instance.setterCalled)

    def testValueSetter(self):
        instance = ValueSetterTestClass()
        try:
            instance.setValue(VOID)
            self.fail("It was suposed to raise an exception")
        except ValueError:
            # ok - expected
            pass
        self.assertFalse(instance.setterCalled)

        try:
            instance.setValue(IntConstant(1))
            self.assertTrue(instance.setterCalled)
        except ValueError as err:
            self.failt(err)
