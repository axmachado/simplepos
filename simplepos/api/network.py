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

    fcn = ApiFunction(INT, "predial", ("option", INT, False),
                      returnAttribute="variablestatus")
    functions.append(fcn)

    fcn = ApiFunction(INT, "preconnect", returnAttrbute="variablestatus")
    functions.append(fcn)

    fcn = ApiFunction(INT, "modem_init", returnAttribute="variablereturn",
                      tagName="network.start")
    functions.append(fcn)

    fcn = VoidApiFunction("modem_shutdown", tagName="shutdownmodem")
    functions.append(fcn)

    fcn = ApiFunction(INT, "gprs_signal_level",
                      returnAttribute="variablestatus",
                      tagName="network.checkgprssignal")
    functions.append(fcn)

    fcn = VoidApiFunction("disconnect", tagName="network.hostdisconnect")
    functions.append(fcn)

    fcn = ApiFunction(INT, "ping", ("host", STRING, False),
                      tagName="network.ping", returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "send", ("buffer", STRING, False),
                      ("size", INT, False), tagName="network.send",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "receive", ("maxsize", INT, False),
                      ("variablereceivedbytes", INT, True),
                      ("variablebuffer", STRING, True),
                      tagName="network.receive",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    return functions
