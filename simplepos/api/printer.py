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

    fcn = VoidApiFunction("print", ("message", STRING, False))
    functions.append(fcn)

    fcn = VoidApiFunction("printbig", ("message", STRING, False))
    functions.append(fcn)

    fcn = ApiFunction(INT, "printbitmap",
                      ("filename", STRING, False),
                      returnAttribute="variablereturn", tagName="printbitmap")
    functions.append(fcn)

    fcn = VoidApiFunction("printbarcode", ("horizontal", INT, False),
                          ("number", STRING, False))
    functions.append(fcn)

    fcn = ApiFunction(INT, "checkpaper", returnAttribute="variableReturn",
                      tagName="checkpaperout")
    functions.append(fcn)

    fcn = VoidApiFunction("paperfeed", tagName="paperfeed")
    functions.append(fcn)

    return functions
