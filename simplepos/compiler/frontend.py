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

    ANTLR4 listener to AST walker.

    SimplePOS Compiler front end
"""

import getopt
import sys
import pickle
import antlr4
from .SimplePOSLexer import SimplePOSLexer
from .SimplePOSParser import SimplePOSParser
from .CompilerListener import CompilerListener

def usage():
    """
    Shows the usage message and exits
    """
    msg = """
    SimplePOS Compiler

    use spc [options] source-file

    opcoes:
       -q | --quiet
           suppress output messages
       -o file
           Sets the output file name. If ommited, the name will
           be the same of the source file, replacing the
           extension .sps for '.spo'
       -h
           Shows this help message
    """
    print(msg)
    sys.exit(1)


class Compiler(object):
    """
    Main compiler class
    """

    def __init__(self, *cmdline):
        """
        Initializes the compiler.
        Takes the arguments from command line.
        """
        self.inputFile = None
        self.outputFile = None
        self.quiet = False
        optlist, args = getopt.getopt(cmdline[1:], 'o:hq', ['quiet'])
        for opt, param in optlist:
            if opt == '-h':
                usage()
            elif opt == '-o':
                self.outputFile = param
            elif opt in ('-q', '--quiet'):
                self.quiet = True
        if len(args) != 1:
            usage()
        self.inputFile = args[0]
        if not self.outputFile:
            posExt = self.inputFile.rfind('.')
            self.outputFile = self.inputFile[0:posExt] + '.spo'

    def run(self):
        """
        Runs the compiler
        """
        if not self.quiet:
            print("SimplePOS Compiler")
            print("Compiling", self.inputFile, "to", self.outputFile)
        inputFile = antlr4.FileStream(self.inputFile)
        lexer = SimplePOSLexer(inputFile)
        stream = antlr4.CommonTokenStream(lexer)
        parser = SimplePOSParser(stream)

        tree = parser.sourcefile()

        listener = CompilerListener(self.inputFile, self.outputFile)
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)
        if not self.quiet:
            listener.module.printStats()
        with open(self.outputFile, "wb") as outFile:
            pickle.dump(listener.module, outFile)
