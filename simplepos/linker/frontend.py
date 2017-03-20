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

    Linker front-end
"""

import getopt
import sys
import pickle
import logging

from .linkedmodule import LinkedModule, LinkerException


class Linker(object):
    """
    Linker front end class
    """
    def __init__(self, *cmdline):
        self.inputFiles = None
        self.outputFile = None
        self.logLevel = logging.INFO
        optlist, args = getopt.getopt(cmdline[1:], 'o:hv:', [ 'help', 'verbose:'])
        for opt, param in optlist:
            if opt == '-h':
                self.help()
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

        logger = logging.getLogger("linker")
        logger.info("Starting SPL")
        if len(args) == 0:
            self.help()
        self.inputFiles = args
        if not self.outputFile:
            posExt = self.inputFiles[0].rfind('.')
            self.outputFile = self.inputFiles[0][0:posExt] + '.xml'

    @staticmethod
    def help():
        "usage"
        # pylint: disable=R0201
        mensagem = """
        SimplePOS Linker

        use spl [opcoes] arquivo1 arquivo2 ...

        opcoes:
           -v level | --verbose level
               Sets verbosity level:
               0: quiet (only errors)
               1: warnings
               2: info (default)
               3: debug
           -o arquivo
               Configura o nome do arquivo de saída. Se omitido, o
               nome no primeiro arquivo é utilizado, com a extensão .posxml
           -h | --help
               Mostra esta mensagem de help.
        """
        print(mensagem)
        sys.exit(1)

    def run(self):
        """
        Run the linker
        """
        linkModule = LinkedModule()
        linkModule.finalName = self.outputFile
        try:
            for arq in self.inputFiles:
                with open(arq, 'rb') as fileIn:
                    modulo = pickle.load(fileIn)
                    linkModule.addModule(modulo)

            linkModule.doLink()
            linkModule.genCode()
        except LinkerException as ex:
            print("Erro de ligação: ", ex)
            sys.exit(255)
