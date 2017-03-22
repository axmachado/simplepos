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

    Handling of functions:

    * Built in functions (Simple POS Language)
    * POSXML API functions
    * User defined functions

"""
from .block import CallableBlock
from .typedefs import (VOID, UNDEF, INT)

class InvalidCallException(Exception):
    """
    Exception raised when you try to call a function with wrong arguments
    """
    def __init__(self, functionName, invalidArgs):
        msg = "wrong arguments calling function %s: " % functionName
        if not isinstance(invalidArgs, str):
            args = []
            for argName, expType, actualType in invalidArgs:
                args.append("expected: %s %s - actual value of type %s" % \
                            (expType, argName, actualType))
            msg += "; ".join(args)
        else:
            msg += invalidArgs
        super(InvalidCallException, self).__init__(msg)


class Function(CallableBlock):
    """
    Generic Function

    A function is a callable block with a optional return type.

    Functions with no return type must be market as VOID
    """
    def __init__(self, returnType=VOID):
        super(Function, self).__init__()
        self.returnType = returnType

    def validateCall(self, *actualArgs):
        " Check if a function call uses the correct arguments "
        invalid = []
        if len(self.argumentList) != len(actualArgs):
            msg = "Incorrect argument count. Expected: %d ; actual count: %d"
            msg %= (len(self.argumentList), len(actualArgs))
            raise InvalidCallException(self.name, msg)
        else:
            for i in range(len(self.argumentList)):
                argName = self.argumentList[i]
                argument = self.arguments[argName]
                value = actualArgs[i]
                if value.type_ == UNDEF:
                    # functionReturnValue of an undefined function.
                    value.type_ = argument.type_
                if argument.type_ != value.type_:
                    invalid.append((argument.name, argument.type_, value.type_))
        if len(invalid) > 0:
            raise InvalidCallException(self.name, invalid)

    def __str__(self):
        " For debugging and logging purposes "
        return "%s %s" % (self.returnType, super(Function, self).__str__())

    def callFunction(self, name):
        # will not call superclass because it
        # the calls must not be propagated to the
        # module unless the function is actually called.
        self.calledFunctions.add(name)

    def processReturnStatement(self, insertBreak = False):
        """
        Finds out if is there any return statement inside the function body,
        and if it is not the last statement, generates an If block to
        jump to the end after the return value is setted.
        """
        # first, we will try to find a return statement before the last
        # statement
        from .typedefs import Assignment, IntConstant
        hasReturn = False
        for i in range(len(self.statements)-1):
            if self.statements[i].containsReturn():
                hasReturn = True
                break
        if hasReturn:
            # sets the __must_return__ variable to false
            self.addVariable("__must_return__", INT)
            self.statements.insert (0, Assignment(
                self.findVariable("__must_return__"), IntConstant(0)))
            super(Function,self).processReturnStatement(False)


class BuiltinFunction(Function):
    " Function build into the compiler "

    def __init__(self, returnType=VOID):
        super(BuiltinFunction, self).__init__(returnType)

class UndefinedFunction(Function):

    " Placeholder for functions not yet defined "
    def __init__(self, name):
        super(UndefinedFunction, self).__init__(UNDEF)
        self.name = name

    def infereArgumentTypes(self, argValues):
        "try do find out how many arguments and of which type"
        if len(self.argumentList) == 0:
            # already defined
            return

        argc = 0
        for v in argValues:
            argName = "arg%d" % argc
            argType = v.type_
            self.addArgument(argName, argType)
            argc += 1


class ApiFunction(BuiltinFunction):

    " POSXML Api function or command "

    def __init__(self, returnType, name, *arguments, **kargs):
        """
        function arguments are expected to be tuples
        containing: (type, name, isReference)

        Keyword arguments allowed:
        tagName - POSXML tag to be generated
        returnAttribute - POSXML tag attribute that represents
                          the return value of the function.
        """
        super(ApiFunction, self).__init__(returnType)
        self.tagName = name
        self.name = name
        self.returnAttribute = None
        self.fixedAttributes = {}
        if kargs:
            if 'tagName' in kargs:
                self.tagName = kargs['tagName']
            if 'returnAttribute' in kargs:
                self.returnAttribute = kargs['returnAttribute']

        for argument in arguments:
            self.addArgument(*argument)

    def addFixedAttribute(self, attrName, value):
        self.fixedAttributes[attrName] = value


class VoidApiFunction(ApiFunction):
    """
    Special case of API function with no return value but
    with optional arguments
    """
    def __init__(self, name, *arguments, **kwargs):
        super(VoidApiFunction, self).__init__(VOID, name, *arguments,
                                              **kwargs)

class NoArgumentApiFunction(VoidApiFunction):
    " Special case of API function with no attribute and no return value"
    def __init__(self, name):
        super(NoArgumentApiFunction, self).__init__(name)
