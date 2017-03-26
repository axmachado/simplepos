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

from ..objfile.functions import ApiFunction
from ..objfile.typedefs import STRING, INT


def initApiFunctions():
    functions = []

    fcn = ApiFunction(STRING, "char_at", ("character_index", INT, False),
                      ("string", STRING, False), tagName="string.charat",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "delimited_element",
                      ("delimiter", STRING, False),
                      ("element_index", INT, False),
                      ("string", STRING, False),
                      tagName="string.elementat",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "delimited_count", ("delimiter", STRING, False),
                      ("string", STRING, False), tagName="string.elements",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "delimited_insert", ("delimiter", STRING, False),
                      ("element_index", INT, False), ("string", STRING, False),
                      ("string_to_be_inserted", STRING, False),
                      tagName="string.insertat",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "delimited_remove", ("delimiter", STRING, False),
                      ("element_index", INT, False), ("string", STRING, False),
                      tagName="string.removeat",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "delimited_replace",
                      ("delimiter", STRING, False),
                      ("element_index", INT, False),
                      ("new_element", STRING, False),
                      ("string", STRING, False), tagName="string.replaceat",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "str_find", ("start", INT, False),
                      ("string", STRING, False), ("substring", STRING, False),
                      tagName="string.find", returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "str_replace", ("new_substring", STRING, False),
                      ("old_substring", STRING, False),
                      ("original_string", STRING, False),
                      tagName="string.replace",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "strmap_get", ("key", STRING, False),
                      ("string", STRING, False),
                      tagName="string.getvaluebykey",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "trim", ("string", STRING, False),
                      tagName="string.trim", returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "strlen", ("value", STRING, False),
                      tagName="string.length",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "strpad", ("character", STRING, False),
                      ("length", INT, False), ("align", STRING, False),
                      ("origin", STRING, False), tagName="string.pad",
                      returnAttribute="destination")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "substr", ("start", INT, False),
                      ("length", INT, False), ("string", STRING, False),
                      tagName="string.substring",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "strcat", ("firstvalue", STRING, False),
                      ("secondvalue", STRING, False),
                      tagName="joinstring",
                      returnAttribute="variabledestination")
    functions.append(fcn)

    return functions
