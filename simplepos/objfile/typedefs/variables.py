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

    Variable data structures

    @author: Alexandre Machado <axmachado@gmail.com>

"""

from .types import STRING, usableInAssignment


class Variable(object):
    """
    Internal representation of a Variable

    Contains:
       name: name of the variable, as declared

       type_: STRING | INT

       container: scope that declared the variable

    """

    def __init__(self, name, type_=STRING):
        """
        name: the name of the variable

        type_: the type (STRING or INT)

        """
        super(Variable, self).__init__()
        self._type = None
        self.type_ = type_
        self.name = name
        self.container = None

    @property
    def type_(self):
        "type"
        return self._type

    @type_.setter
    @usableInAssignment
    def type_(self, theType):
        "type"
        self._type = theType

    def __str__(self):
        return "%s %s" % (self.type_, self.name)


def variableSetter(setter):
    "Decorator to validate a Variable in a setter"
    def theSetter(self, value):
        "the real setter"
        if value and not (isinstance(value, Variable)
                          or isinstance(value, Argument)):
            raise ValueError("The value must be an instance of Variable")
        setter(self, value)
    return theSetter


class Argument(object):
    """
    An argument for a module or function

    Attributes:

       name: name of the argument

       type: STRING or INT

       isReference: true if the argument is passed by reference.
                    the default is to pass by value

    """
    def __init__(self, name=None, argtype=STRING, isReference=False):
        super(Argument, self).__init__()
        self.variable = Variable(name, argtype)
        self.isReference = isReference

    @property
    def variable(self):
        return self._variable

    @variable.setter
    @variableSetter
    def variable(self, var):
        self._variable = var

    @property
    def name(self):
        return self.variable.name

    @name.setter
    def name(self, value):
        self.variable.name = value

    @property
    def type_(self):
        return self.variable.type_

    @type_.setter
    def type_(self, value):
        self.variable.type_ = value

    def __str__(self):
        return '%s %s%s' % (self.type_, '&' if self.isReference else '',
                            self.name)
