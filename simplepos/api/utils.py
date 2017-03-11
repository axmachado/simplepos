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

    fcn = ApiFunction(INT, "backlight", ("level", INT, False),
                      tagName="system.backlight",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("qrcode", ("filename", STRING, False),
                          ("input", STRING, False),
                          ("size", STRING, False),
                          ("version", STRING, False),
                          tagName="system.rqcode")
    functions.append(fcn)

    fcn = VoidApiFunction("beep", tagName="system.beep")
    functions.append(fcn)

    fcn = ApiFunction(INT, "check_battery",
                      tagName="system.checkbattery",
                      returnAttribute="variablestatus")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "system_info",
                      ("type", STRING, False),
                      tagName="system.info",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("system_restart", tagName="system.restart")
    functions.append(fcn)

    fcn = ApiFunction(INT, "unzip", ("filename", STRING, False),
                      tagName="unzipfile",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("waitkey")
    functions.append(fcn)

    fcn = VoidApiFunction("waitkey_timeout", ("seconds", INT, False),
                          tagName="waitkeytimeout")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "readkey", ("miliseconds", INT, False),
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("wait", ("milliseconds", INT, False))
    functions.append(fcn)

    return functions
