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
from simplepos.objfile.block import (NameScope, DuplicateVariableException,
                                     CallableBlock)
from simplepos.objfile.typedefs import INT, STRING


class NameScopeTest(unittest.TestCase):

    instance = None

    def setUp(self):
        self.instance = NameScope(None)

    def testVariablesSingleScope(self):
        self.instance.addVariable('v1', INT)
        self.instance.addVariable('v2', STRING)

        try:
            self.instance.addVariable('v1', STRING)
            self.fail("Supose to raise an DuplicateVariableExceptio")
        except DuplicateVariableException:
            pass  # ok, expected

        var = self.instance.findVariable('v1')
        self.assertEquals(INT, var.type_)

    def testVariablesMultipleLevels(self):
        child1 = NameScope(self.instance)
        child2 = NameScope(self.instance)
        child3 = NameScope(child1)

        self.instance.addVariable('v1', INT)
        child1.addVariable('v2', INT)
        child2.addVariable('v3', INT)
        child3.addVariable('v4', INT)

        self.assertIsNotNone(child1.findVariable('v1'))
        self.assertIsNotNone(child2.findVariable('v1'))
        self.assertIsNotNone(child3.findVariable('v1'))
        self.assertIsNotNone(child3.findVariable('v2'))

        try:
            child3.addVariable('v2', STRING)
            self.fail("DuplicateVariableException expected")
        except DuplicateVariableException:
            pass  # ok - expected

    def testCallFunctionMultipleLevels(self):
        child1 = NameScope(self.instance)
        child1.callFunction('f1')
        self.assertIn('f1', self.instance.calledFunctions)


class CallableBlockTest(unittest.TestCase):

    def setUp(self):
        self.instance = CallableBlock()

    def testArgument(self):
        self.instance.addArgument("arg1", INT, True)

        self.assertIsNotNone(self.instance.findVariable('arg1'))
