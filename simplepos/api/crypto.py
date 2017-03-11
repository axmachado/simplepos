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

    fcn = ApiFunction(INT, "crc", ("buffer", STRING, False),
                      ("size", INT, False),
                      returnAttribute="variablereturn", tagName="crypto.crc")
    fcn.addFixedAttribute("type", "CRC")
    functions.append(fcn)

    fcn = ApiFunction(INT, "crc_ccitt", ("buffer", STRING, False),
                      ("size", INT, False),
                      returnAttribute="variablereturn", tagName="crypto.crc")
    fcn.addFixedAttribute("type", "CRC-CCITT")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "cipher_block",
                      ("cryptotype", STRING, False),
                      ("key", STRING, False),
                      ("message", STRING, False),
                      returnAttribute="variablereturn",
                      tagname="crypto.encryptdecrypt")
    fcn.addFixedAttribute("type", "0")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "decipher_block",
                      ("cryptotype", STRING, False),
                      ("key", STRING, False),
                      ("message", STRING, False),
                      returnAttribute="variablereturn",
                      tagname="crypto.encryptdecrypt")
    fcn.addFixedAttribute("type", "1")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "lrc",
                      ("buffer", STRING, False),
                      ("size", INT, False),
                      returnAttribute="variablereturn",
                      tagname="crypto.lrc")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "xor", ("buffer1", STRING, False),
                      ("buffer2", STRING, False),
                      ("size", INT, False), tagName="crypto.xor",
                      returnAttribute="variablereturn")
    functions.append(fcn)
    return functions
