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

    Variable scope during code generation
"""

import logging
from .variables import Assignment
from ..objfile import typedefs

# pylint: disable=C0103
logger = logging.getLogger('link')

class POSXMLCodeScope(object):
    """
    Scope - determines which variables are visible in each context

    Properties:

    userVariables - set of user defined variables created in this scope

    autoIntVariables - set of integer variables automatically created in this
                       scope

    autoStringVariables - set of string variables automatically created in this
                          scope

    parentScope - parent scope on scope hierarchy

    codeBlock - code block where the automatic variables will be created

    """
    def __init__(self, codeBlock):
        self.userVariables = set()
        self.autoIntVariables = set()
        self.autoStringVariables = set()
        self.parentScope = None
        self.codeBlock = codeBlock

    def variableExists(self, varName):
        """
        Check if the variable exists
        """
        result = False
        result = result or varName in self.userVariables
        result = result or varName in self.autoIntVariables
        result = result or varName in self.autoStringVariables
        if not result and self.parentScope:
            # if necessary, look in the parent scope
            result = self.parentScope.variableExists(varName)
        return result

    def __str__(self):
        return "User Variables: %s\nautoInt: %s\nautoString: %s" % (repr(self.userVariables),
                                                                    repr(self.autoIntVariables),
                                                                    repr(self.autoStringVariables))

    def _autoVariable(self, storage, prefix):
        """
        Create an automatic variable

        storage: with set the variable will be inserted into

        prefix: name prefix for the variable
        """
        count = 0
        varName = prefix + str(count)
        while self.variableExists(varName):
            count += 1
            varName = prefix + str(count)

        storage.add(varName)
        logger.debug("Created automatic variable %s", varName)
        return varName

    def autoInt(self):
        """
        Create an automatic integer variable
        """
        prefix = 'isimpleposauto'
        varName = self._autoVariable(self.autoIntVariables, prefix)
        stmgen = Assignment(typedefs.INT, varName, "0")
        if self.codeBlock:
            self.codeBlock.addStatements(stmgen)
        return varName

    def autoString(self):
        """
        Create an automatic string variable
        """
        prefix = 'ssimpleposauto'
        varName = self._autoVariable(self.autoStringVariables, prefix)
        stmgen = Assignment(typedefs.STRING, varName, "")
        if self.codeBlock:
            self.codeBlock.addStatements(stmgen)
        return varName

    def addUserVariable(self, varName):
        """
        Add an user defined variable to the scope
        """
        self.userVariables.add(varName)
