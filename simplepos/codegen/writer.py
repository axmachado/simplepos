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

    POSXML Language Writer
"""

import os


class POSXMLWriter(object):
    """The output file writer"""

    def __init__(self, fileName, statements):
        self.statements = statements
        self.fileName = fileName
        self.moduleName = os.path.basename(fileName).replace('.posxml', '')

    def _header(self, output):
        "XML header"
        # will not be generated because the POSXML IDE does not accept it.
        if False:
            output.write('<?xml version="1.0" encoding="utf-8"?>\n')
            output.write('<!-- SimplePOSLanguage - generated for module %s -->\n' % \
                         self.moduleName)
            output.write('<posxml>\n')


    @staticmethod
    def _trailer(output):
        "XML Trailer"
        # pylint: disable=R0201
        # it can be a function, but stays in the class for interface consistency
        # will not be generated because the POSXML ide does not support it.
        if False:
            output.write('</posxml>\n')

    def write(self):
        "Write the code to a file"
        with open(self.fileName, 'w') as output:
            self._header(output)
            for stm in self.statements:
                stm.emit(output, '    ')
            self._trailer(output)
