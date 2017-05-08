#-*- coding: utf-8
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

    POSXML Language Statement (emits a series or xml tags)
"""
import re
import logging

logger = logging.getLogger("linker")


def quotedValue(value):
    if '"' in str(value):
        return "'%s'" % str(value)
    else:
        return '"%s"' % str(value)

def emitTag(tagName, attributes, values):
    " Utilitty: Emit a single tag with attributes "
    attrVal = ['%s=%s' % val for val in zip(attributes,
                                            [quotedValue(v) for v in values])]
    return ('<%s %s />' % (tagName, ' '.join(attrVal)), )


class POSXMLStatement(object):
    """
    Statement of POSXML language - xml tag
    """
    def __init__(self):
        super(POSXMLStatement, self).__init__()

    def emitStatement(self):
        " emit the POSXML tags as a sequence "
        result = str(self)
        reSingleTag = re.compile(r'<[a-z]+ [^>]*/>')
        if reSingleTag.match(result):
            return result
        else:
            raise CodeGenerationError('the emitStatement method must be overrided by sub class')

    def emit(self, output, prefix):
        " emit the code of the statement into the output file "
        logger.debug("Emiting code for " + repr(self.__class__))
        for linha in self.emitStatement():
            output.write(prefix)
            output.write(linha)
            output.write("\n")

    def assignsVariable(self, name):
        result = False
        if self.blocks():
            for block in self.blocks():
                if result:
                    break
                for statement in block.statements:
                    if statement.assignsVariable(name):
                        result = True
                        break

        return result

    def usesVariable(self, name):
        "Check if statement uses the value of a variable"
        result = False
        if self.blocks():
            for block in self.blocks():
                if result:
                    break
                for statement in block.statements:
                    if statement.usesVariable(name):
                        result = True
                        break
        return result

    def blocks(self):
        "Get all the code blocks of the statement"
        return None

class CodeGenerationError(Exception):
    """
    General code generation error
    """
    def __init__(self, msg):
        super(CodeGenerationError, self).__init__(msg)
