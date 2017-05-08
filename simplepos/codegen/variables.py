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

    Code Generator - Variables related statement
"""

from ..objfile.typedefs import INT
from .base import POSXMLStatement, quotedValue


class Assignment(POSXMLStatement):
    "Variable assignment"

    def __init__(self, type_, variable, value):
        super(Assignment, self).__init__()
        self.variable = variable
        self.type_ = type_
        self.value = value

    def usesVariable(self, name):
        return self.variable == name or ('$(' + name + ')') in self.value

    def assignsVariable(self, name):
        return self.variable == ('$(' + name + ')')

    def emitStatement(self):
        tag = "integervariable" if self.type_ == INT else "stringvariable"
        return ('<%s value=%s variable="%s" />' % (tag, quotedValue(self.value), self.variable), )


class IncrementDecrement(POSXMLStatement):
    "Increment or decrement an integer variable"
    def __init__(self, var, operator):
        super(IncrementDecrement, self).__init__()
        self.variable = var if var.startswith('$') else '$(%s)' % var
        self.operator = operator

    def usesVariable(self, name):
        return self.variable == ('$(' + name + ')')

    def assignsVariable(self, name):
        return self.usesVariable(name)

    def emitStatement(self):
        "Emits the statement"
        return ('<integeroperator operator="%s" variablesource="%s" />' % \
               (self.operator, self.variable),)
