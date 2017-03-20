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
import logging
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
       -v level | --verbose level
           Sets verbosity level:
           0: quiet (only errors)
           1: warnings
           2: info (default)
           3: debug
       -o file
           Sets the output file name. If omitted, the name will
           be the same of the source file, replacing the
           extension .sps for '.spo'
       -h
           Shows this help message
    """
    print(msg)
    sys.exit(1)


class ErrorCounter (antlr4.error.ErrorListener.ErrorListener):
    def __init__(self, fileName):
        super(ErrorCounter, self).__init__()
        self.fileName = fileName
        self.errorCount = 0;

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print ( "%s:%d:%d: %s" % (self.fileName, line, column, msg),
                file=sys.stderr)
        self.errorCount += 1

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


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
        self.logLevel = logging.INFO
        optlist, args = getopt.getopt(cmdline[1:], 'o:hv:', ['help'])
        for opt, param in optlist:
            if opt == '-h' or opt == '--help':
                usage()
            elif opt == '-o':
                self.outputFile = param
            elif opt == '-v' or opt == '--verbose':
                if param == '0':
                    self.quiet = True
                elif param == '1':
                    self.logLevel = logging.WARN
                elif param == '3':
                    self.logLevel = logging.DEBUG

        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(name)s : %(message)s',
            level=self.logLevel)

        logger = logging.getLogger("compiler")
        logger.info("Starting SPC")

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
        logger = logging.getLogger("compiler")
        if not self.quiet:
            print("SimplePOS Compiler")
            print("Compiling", self.inputFile, "to", self.outputFile)

        inputFile = antlr4.FileStream(self.inputFile, encoding="utf-8")
        lexer = SimplePOSLexer(inputFile)
        stream = antlr4.CommonTokenStream(lexer)

        parser = SimplePOSParser(stream)
        counter = ErrorCounter(self.inputFile)
        parser.removeErrorListeners()
        parser.addErrorListener(counter)
        logger.debug ("Starting ANTLR4 parser")
        tree = parser.sourcefile()
        if counter.errorCount > 0:
            sys.exit(-1)
        logger.debug ("Parsing complete without errors")

        listener = CompilerListener(self.inputFile, self.outputFile)
        walker = antlr4.ParseTreeWalker()
        logger.debug ("Walking syntax tree to generate "
                      "intermediate representation")
        walker.walk(listener, tree)

        if not self.quiet:
            listener.module.printStats()
        if self.logLevel == logging.DEBUG:
            print (listener.module)
        logger.debug ("Writing output file")
        with open(self.outputFile, "wb") as outFile:
            pickle.dump(listener.module, outFile)
