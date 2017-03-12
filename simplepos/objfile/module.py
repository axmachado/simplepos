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

    Module definition code

    A Module is the result of a SimplePOS source file compilation.

    Modules can be named (main modules) or
    anonymous (linked along with main modules)

"""

from .block import CallableBlock


class Module(CallableBlock):
    """
    The main construct of the intermediate representation
    of the program, a Module is an image of a source code file

    Attributes:

    sourceFile: the source file name

    objectFile: the object file name

    functions: name indexed dictionary of functions defined in this module

    externalFunctions: list of function names defined in other modules and that
                       must be linked with this one.
    """

    def __init__(self, sourceFile, objFile):
        super(Module, self).__init__()
        self.sourceFile = sourceFile
        self.objFile = objFile
        self.functions = {}
        self.externalFunctions = {}
        self.constants = {}
        self.externalConstants = {}

    def printStats(self):
        print("Module name:", self.name)
        print("Source file: ", self.sourceFile)
        print("Object file: ", self.objFile)
        super(Module, self).printStats()
        print("Defined functions:", len(self.functions))
        print("    " + ", ".join(self.functions[x].name
                                 for x in self.functions))

    def findFunction(self, name):
        """
        Find a function on the scope of the module.

        This method will find all functions defined inside the module,
        and all built in functions.
        """
        from .functions import UndefinedFunction
        from ..api import findApiFunction
        try:
            # first, try to find it as an API functions
            func = findApiFunction(name)
        except KeyError:
            if name in self.functions:
                # defined here
                func = self.functions[name]
            elif name in self.externalFunctions:
                # already used and defined as external
                func = self.externalFunctions[name]
            else:
                # not found, adding as an external reference
                func = UndefinedFunction(name)
                self.externalFunctions[name] = func
        return func

    def canResolveUndefined(self, function):
        from .typedefs import UNDEF

        theUndef = self.externalFunctions[function.name]
        if len(theUndef.arguments) > 0:
            if len(function.arguments) != len(theUndef.arguments):
                return False
            combo = zip(function.arguments, theUndef.arguments)
            for (argf, argu) in combo:
                if argf.type_ != argu.type_:
                    return False
        if theUndef.returnType != UNDEF:
            if theUndef.returnType != function.returnType:
                return False
        return True

    def addFunction(self, function):
        fname = function.name
        if fname in self.externalFunctions:
            if self.canResolveUndefined(function):
                del self.externalFunctions[fname]
            else:
                raise ValueError('Defined function incompatible with '
                                 'previous calls: ' + fname)

        if fname in self.functions:
            raise ValueError('Duplicated function definition: ' + fname)

        self.functions[fname] = function

    def addExternalConstant(self, name, value):
        self.externalConstants[name] = value

    def addLocalConstant(self, name, value):
        self.constants[name] = value

    def replaceVariableReferences(self, varName, variable):
        super(Module, self).replaceVariableReferences(varName, variable)
        for function in self.functions.values():
            function.replaceGlobalVariableReferences(varName, variable)

    def resolveExternalConstant(self, name, value):
        if name in self.externalConstants:
            super(Module, self).resolveExternalConstant(name, value)
            for function in self.functions.values():
                function.resolveExternalConstant(name, value)
            del self.externalConstants[name]

    def __str__(self):
        partial = super(Module, self).__str__()
        if len(self.functions) > 0:
            partial += "\n\n"
            for fcn in self.functions:
                partial += str(self.functions[fcn])
                partial += "\n"

        return partial
