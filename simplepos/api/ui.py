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

from ..objfile.functions import ApiFunction, VoidApiFunction
from ..objfile.typedefs import STRING, INT


def initApiFunctions():
    functions = []

    fcn = ApiFunction(INT, "menu", ("options", STRING, False),
                      returnAttribute="variable")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "menuwithheader",
                      ("header", STRING, False),
                      ("timeoutheader", INT, False),
                      ("options", STRING, False),
                      ("timeout", INT, False),
                      returnAttribute="variablereturn"
                      )
    functions.append(fcn)

    fcn = ApiFunction(INT, "displaybitmap",
                      ("filename", STRING, False),
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("display",
                          ("line", INT, False),
                          ("column", INT, False),
                          ("message", STRING, False))
    functions.append(fcn)

    fcn = VoidApiFunction("cleandisplay")
    functions.append(fcn)

    fcn = ApiFunction(INT, "gettouch", ("axisx", INT, True),
                      ("axisy", INT, True),
                      tagName="system.gettouchscreen",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "inputfloat", ("line", INT, False),
                      ("column", INT, False),
                      ("message", STRING, False),
                      tagName="inputfloat", returnAttribute="variable")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "inputformat", ("line", INT, False),
                      ("column", INT, False),
                      ("message", STRING, False),
                      ("format", STRING, False), tagName="inputformat",
                      returnAttribute="variable")
    functions.append(fcn)

    fcn = ApiFunction(INT, "inputint", ("line", INT, False),
                      ("column", INT, False),
                      ("message", STRING, False),
                      ("minimum", INT, False),
                      ("maximum", INT, False), tagName="inputinteger",
                      returnAttribute="variable")
    functions.append(fcn)

    fcn = ApiFunction(INT, "inputoption", ("line", INT, False),
                      ("column", INT, False),
                      ("message", STRING, False),
                      ("minimum", INT, False),
                      ("maximum", INT, False), tagName="inputoption",
                      returnAttribute="variable")
    functions.append(fcn)

    fcn = ApiFunction(INT, "inputmoney", ("line", INT, False),
                      ("column", INT, False),
                      ("message", STRING, False),
                      tagName="inputmoney", returnAttribute="variable")
    functions.append(fcn)

    return functions
