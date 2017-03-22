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

    fcn = ApiFunction (INT, "iso8583_loadconfig",
                       ("filename", STRING, False),
                       tagName="iso8583.initfieldtable",
                       returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_init_message",
                      ("format", STRING, False),
                      ("id", STRING, False),
                      ("variablemessage", STRING, True),
                      tagName="iso8583.initmessage",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_put_string",
                      ("fieldnumber", INT, False),
                      ("value", STRING, False),
                      tagName="iso8583.putfield",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "string")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_put_int",
                      ("fieldnumber", INT, False),
                      ("value", INT, False),
                      tagName="iso8583.putfield",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "integer")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_end_message",
                      ("variablesize", INT, True),
                      tagName="iso8583.endmessage",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_transact",
                      ("channel", STRING, False),
                      ("header", STRING, False),
                      ("trailler", STRING, False),
                      ("isomsg", STRING, False),
                      ("variableresponse", STRING, True),
                      tagName="iso8583.transactmessage",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_analyse",
                      ("format", STRING, False),
                      ("size", INT, False),
                      ("variableid", STRING, True),
                      ("variablemessage", STRING, True),
                      tagName="iso8583.analyzemessage",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_get_int",
                      ("fieldnumber", INT, False),
                      ("variablevalue", INT, True),
                      tagName="iso8583.getfield",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "integer")
    functions.append(fcn)

    fcn = ApiFunction(INT, "iso8583_get_string",
                      ("fieldnumber", INT, False),
                      ("variablevalue", STRING, True),
                      tagName="iso8583.getfield",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "string")
    functions.append(fcn)

    return functions
