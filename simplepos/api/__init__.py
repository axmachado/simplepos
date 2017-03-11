# -*- coding: utf-8
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

    Façade to available POSXML functions and commands.
"""

from ..objfile.functions import (ApiFunction, NoArgumentApiFunction,
                                 VoidApiFunction)
from ..objfile.typedefs import (INT, STRING)

import importlib

__all__ = ['getApiFunctions', 'findApiFunction']


def initApiFunctions():
    " Init the global function dictionary "
    additionalModules = [".control", ".card", ".ui", ".printer", ".crypto",
                         ".filesystem", ".iso8583", ".datetime", ".network",
                         ".conversions", ".strings", ".utils"]

    functions = []
    # User Interface

    for moduleName in additionalModules:
        theModule = importlib.import_module(moduleName, "simplepos.api")
        functions.extend(theModule.initApiFunctions())

    return {item.name: item for item in functions}

API = initApiFunctions()


def getApiFunctions():
    " Get a dictionary with all available API functions "
    return API


def findApiFunction(name):
    " Find one API function by name "
    functions = getApiFunctions()
    return functions[name]
