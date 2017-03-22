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

    Internal functions - POSXML code generated directly
"""

from .functions import Function, InvalidCallException
from .typedefs import INT, STRING, IntConstant, StringConstant

_INLINE = { }


def findInlineFunction(name):
    if name in _INLINE:
        return _INLINE[name]

    return None

class InlineFunction(Function):
    """
    Function without a body: the function call evaluates as an Value os Statement,
    depending on the context
    """
    def __init__(self, returnType):
        super(InlineFunction,self).__init__(returnType)

    def callStatements(self, scope):
        """
        Generates into the scope the statements that compute the
        function call result in a statement context.
        """
        pass

    def callValue(self, scope, *args):
        """
        Generates in the scope the statements that compute the
        function call result in a value context, and returns a
        value object with this result.
        """
        pass


class DelimitedInit(InlineFunction):
    """
    Inits an delimited buffer with n elements
    """
    def __init__(self):
        super(DelimitedInit, self).__init__(STRING)
        self.name = 'delimited_init'
        self.addArgument('delimiter', STRING, False)
        self.addArgument('length', INT, False)

    def validateCall(self, *actualArgs):
        super(DelimitedInit,self).validateCall(*actualArgs)
        if isinstance(actualArgs[0],StringConstant):
            if len(actualArgs[0].value) != 1:
                raise InvalidCallException(self.name, "The delimiter must be a single character")
        else:
            raise InvalidCallException(self.name, "The delimiter must be a constant")
        if not isinstance(actualArgs[1],IntConstant):
            raise ValueError(self.name, "The legth must be a constant")

    def callValue(self, scope, *args):
        delimiter = args[0].value
        length = int(args[1].value)
        strVal = ""
        for i in range(length):
            strVal = strVal + delimiter
        return StringConstant(strVal)


_INLINE = { "delimited_init": DelimitedInit() }
