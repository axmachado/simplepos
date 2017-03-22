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

    Code block
    @author: Alexandre Machado <axmachado@gmail.com>

"""

from .typedefs.statements import Statement
from .typedefs import Argument, Variable


class DuplicateVariableException(Exception):
    " A variable was declared twice in a scope "
    def __init__(self, variable, complementaryMessage=""):
        msg = "Duplicated'%s' variable in block %s. %s"
        containerName = ''
        if variable.container:
            try:
                containerName = variable.container.name
            except AttributeError:
                pass  # container has no name
        msg %= (variable.name, containerName, complementaryMessage)
        super(DuplicateVariableException, self).__init__(msg)


class NameScope(object):
    """A segment of a program where a name (variable) is defined"""

    def __init__(self, parentScope=None):
        super(NameScope, self).__init__()
        self.variables = {}
        self.statements = []
        self.parentScope = parentScope
        self.calledFunctions = set()

    def variableExists(self, varName):
        "check if a variable is defined"
        try:
            self.findVariable(varName)
            return True
        except KeyError:
            return False

    def isEmpty(self):
        "contains no statements"
        return len(self.statements) == 0

    def localExists(self, varName):
        "local variable exists?"
        return varName in self.variables

    def addVariable(self, varName, type_):
        "add a variable definition to the scope"
        var = Variable(varName, type_)
        var.container = self
        if self.localExists(varName):
            raise DuplicateVariableException(var)
        try:
            # check if the name was globally
            globalVarName = self.findVariable(varName)
            if globalVarName.type_ != type_:
                raise DuplicateVariableException(var, "Defined globally with "
                                                      "other type")
        except KeyError:
            # no global variable with the same name, we can define a local one
            self.variables[varName] = var

    def replaceVariableReferences(self, varName, variable):
        if varName in self.variables:
            self.variables[varName] = variable
        for stm in self.statements:
            stm.replaceVariableReferences(varName, variable)

    def replaceGlobalVariableReferences(self, varName, variable):
        if varName not in self.variables:
            for stm in self.statements:
                stm.replaceVariableReferences(varName, variable)

    def resolveExternalConstant(self, name, value):
        for stm in self.statements:
            stm.resolveExternalConstant(name, value)

    def replaceLinkedFunction(self, function):
        for stm in self.statements:
            stm.replaceLinkedFunction(function)

    def _getLocal(self, varName):
        return self.variables[varName]

    def findVariable(self, varName):
        "find a variable in this scope or any parent scope"
        if self.localExists(varName):
            return self._getLocal(varName)
        else:
            if self.parentScope:
                return self.parentScope.findVariable(varName)
        # if reaches here without a return, the variable is not defined
        raise KeyError('Undefined variable %s' % varName)

    def callFunction(self, name):
        """
        Add a called function to this scope and to all parent scopes.
        This ensures that the main scope (module) will contain a list
        of all called functions and only the called functions will be
        linked.
        """
        self.calledFunctions.add(name)
        if self.parentScope:
            self.parentScope.callFunction(name)

    def addStatement(self, stm):
        """
        Add a executable statement to this scope
        """
        self.statements.append(stm)

    def popStatement(self):
        """
        Pops out the last statement inserted.
        Used by block commands to extract the block
        from the statement list
        """
        return self.statements.pop()

    def containsReturn(self):
        for stm in self.statements:
            if stm.containsReturn():
                return True
        return False

    def _ifNotReturn(self, stmBlock):
        from .typedefs.values import NegatedValue, VarValue
        from .typedefs.statements import IfThenElse
        variable = self.findVariable("__must_return__")
        condition = NegatedValue(VarValue(variable))
        ifStm = IfThenElse()
        ifStm.condition = condition
        ifBlock = BlockStatement(self)
        ifBlock.statements = stmBlock
        ifStm.ifBlock = ifBlock
        return ifStm

    def processReturnStatement(self, insertBreak = False):
        """
        Generate an If block after the return statement
        """
        from .typedefs import (ReturnStatement, Assignment, IntConstant,
                               BreakStatement)
        # find the first statement that contains return.
        found = False
        for i in range(len(self.statements)):
            if self.statements[i].containsReturn():
                found = True
                break
        if not found:
            return
        if i < (len(self.statements)-1):
            # Found it before the last statement
            afterReturnBlock = self.statements[i+1:]
            self.statements = self.statements[:i+1]
            ifStatement = self._ifNotReturn(afterReturnBlock)
            self.addStatement(ifStatement)
            if ifStatement.containsReturn():
                ifStatement.processReturnStatement(insertBreak)
        if isinstance(self.statements[i], ReturnStatement):
            variable = self.findVariable("__must_return__")
            assignment = Assignment(variable, IntConstant(1))
            self.statements.insert(i+1, assignment)
            if (insertBreak):
                self.statements.insert(i+2, BreakStatement())
        else:
            self.statements[i].processReturnStatement(insertBreak)


    def _printVarList(self, prefix):
        """
        Print the list of variables for debugging and
        compiler stats
        """
        lines = [(prefix + str(x)) for x in self.variables.values()]
        return "\n".join(lines)

    def _printStatements(self, prefix):
        """
        Print the list of statements for debugging and
        compiler stats
        """
        lines = []
        for stm in self.statements:
            stmlines = str(stm).split("\n")
            lines.extend([prefix + x for x in stmlines])
        return "\n".join(lines)

    def printStats(self):
        """
        Print statistics of the scope
        """
        print("Defined variables:", len(self.variables))
        print(self._printVarList("    "))
        print("Called functions: ", len(self.calledFunctions))
        print("    " + ", ".join(self.calledFunctions))
        print("Defined statements:", len(self.statements))
        print(self._printStatements("    "))

    def __str__(self):
        lines = ['{']
        lines.extend(self._printStatements('    ').split('\n'))
        lines.append('}')
        return "\n".join(lines)


class CallableBlock(NameScope):
    """
    Any scope that can be called from elsewhere with arguments

    Attributes:

    argumentList : list of positional argument names, in the same order
                   declared in the source code

    arguments: dictionary containing all the argument objects, indexed by
               name.
    """

    def __init__(self):
        super(CallableBlock, self).__init__()
        self.argumentList = []
        self.arguments = {}
        self.name = None

    def localExists(self, varName):
        "An argument is a variable inside this block"
        return varName in self.arguments or \
            super(CallableBlock, self).localExists(varName)

    def _getLocal(self, varName):
        if varName in self.arguments:
            return self.arguments[varName].variable
        else:
            return super(CallableBlock, self)._getLocal(varName)

    def addArgument(self, argName, argType, isReference=False):
        "Add an argument to the list"
        arg = Argument(argName, argType, isReference)
        arg.container = self
        self.arguments[argName] = arg
        self.argumentList.append(argName)

    def orderedArgumentList(self):
        return [self.arguments[name] for name in self.argumentList]

    def _printArgList(self, prefix):
        "Print for debugging and statistics"
        lines = []
        for arg in self.arguments.values():
            argumentLine = '%s%s %s%s' % (prefix, arg.type_,
                                          '&' if arg.isReference else '',
                                          arg.name)
            lines.append(argumentLine)
        return "\n".join(lines)

    def __str__(self):
        argumentList = ", ".join([str(self.arguments[x])
                                  for x in self.argumentList])
        header = "%s (%s)" % (self.name, argumentList)
        return header + "\n" + super(CallableBlock, self).__str__()

    def printStats(self):
        """
        Print statistics of the scope
        """
        print("Defined arguments: ", len(self.arguments))
        self._printArgList("    ")
        super(CallableBlock, self).printStats()

    def replaceVariableReferences(self, varName, variable):
        if varName in self.arguments:
            if varName != variable.name:
                argListPosition = self.argumentList.index(varName)
                self.argumentList[argListPosition] = variable.name
                self.arguments[variable.name] = self.arguments[varName]
                del self.arguments[varName]

            self.arguments[variable.name].variable = variable
        super(CallableBlock, self).replaceVariableReferences(varName, variable)


class BlockStatement(NameScope, Statement):
    """
    A list of statements that is executed in sequence.

    Usually, represents a set of statements defined in source code
    between brackets ({})

    """
    def __init__(self, parentScope):
        super(BlockStatement, self).__init__(parentScope)

    def containsReturn(self):
        return NameScope.containsReturn(self)