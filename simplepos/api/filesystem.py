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

    fcn = ApiFunction(INT, "listfiles", ("dir", STRING, False),
                      ("listfilename", STRING, False),
                      tagName="filesystem.listfiles",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "rename", ("oldname", STRING, False),
                      ("newname", STRING, False),
                      tagName="filesystem.renamefile",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesize", ("filename", STRING, False),
                      tagName="filesystem.filesize",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesystem_space",
                      ("dir", STRING, False),
                      ("type", STRING, False),
                      tagName="filesystem.space",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesystem_total",
                      ("dir", STRING, False),
                      tagName="filesystem.space",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "total")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesystem_used",
                      ("dir", STRING, False),
                      tagName="filesystem.space",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "used")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesystem_free",
                      ("dir", STRING, False),
                      tagName="filesystem.space",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "free")
    functions.append(fcn)

    fcn = ApiFunction(INT, "filesystem_countfiles",
                      ("dir", STRING, False),
                      tagName="filesystem.space",
                      returnAttribute="variablereturn")
    fcn.addFixedAttribute("type", "countfiles")
    functions.append(fcn)

    fcn = ApiFunction(INT, "open", ("filename", STRING, False),
                      ("mode", STRING, False), tagName="file.open",
                      returnAttribute="variablehandle")
    functions.append(fcn)

    fcn = ApiFunction(INT, "read", ("handle", INT, False),
                      ("size", INT, False),
                      ("variablebuffer", STRING, True),
                      tagName="file.read", returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("write", ("handle", INT, False),
                          ("size", INT, False),
                          ("buffer", STRING, False), tagName="file.write")
    functions.append(fcn)

    fcn = VoidApiFunction("close", ("handle", INT, False),
                          tagName="file.close")
    functions.append(fcn)

    fcn = ApiFunction(STRING, "dbread", ("filename", STRING, False),
                      ("key", STRING, False), tagName="readfile",
                      returnAttribute="variabledestination")
    functions.append(fcn)

    fcn = ApiFunction(INT, "dbread_index",
                      ("filename", STRING, False),
                      ("index", INT, False),
                      ("variablekey", STRING, True),
                      ("variablevalue", STRING, True),
                      tagName="readfilebyindex",
                      returnAttribute="variablereturn")
    functions.append(fcn)

    fcn = VoidApiFunction("dbupdate", ("filename", STRING, False),
                          ("key", STRING, False),
                          ("value", STRING, False), tagName="editfile")
    functions.append(fcn)

    fcn = VoidApiFunction("delete", ("filename", STRING, False),
                          tagName="deletefile")
    functions.append(fcn)

    fcn = ApiFunction(INT, "downloadfile",
                      ("filename", STRING, False),
                      ("remotepath", STRING, False),
                      tagName="downloadfile", returnAttribute="variablereturn")
    functions.append(fcn)

    return functions
