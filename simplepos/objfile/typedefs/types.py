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

    Data types allowed in the language

    @author: Alexandre Machado <axmachado@gmail.com>

"""

STRING = 'str'
INT = 'int'
VOID = 'void'
UNDEF = 'undef'


def usableInExpression(method):
    "decorator - setter of values that are usable in expressions"
    def theSetter(self, typeName):
        "setter"
        if typeName != INT:
            raise ValueError("The type must be int")
        method(self, typeName)
    return theSetter


def usableInAssignment(method):
    "decorator - setter of values that are usable in assgnments"
    def theSetter(self, typeName):
        "setter"
        if typeName not in (INT, STRING):
            raise ValueError("The type must be int or string")
        method(self, typeName)
    return theSetter
