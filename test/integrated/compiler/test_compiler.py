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

import unittest
import os
import shutil
import pickle

from simplepos.compiler.frontend import Compiler
from simplepos.objfile.module import Module


class CompilerTest(unittest.TestCase):

    def setUp(self):
        absdir = os.path.dirname(os.path.abspath(__file__))
        self.datadir = os.path.join(absdir, 'data')
        self.tmpdir = os.path.join(absdir, 'tmp')

        if not os.path.exists(self.tmpdir):
            os.mkdir(self.tmpdir)

    def tearDown(self):
        if os.path.exists(self.tmpdir):
            shutil.rmtree(self.tmpdir, ignore_errors=True)

    def setupCompilerArguments(self, sourceFile):
        objFile = sourceFile.replace(".sps", ".spo")
        return ('compiler', '--quiet', '-o',
                os.path.join(self.tmpdir, objFile),
                os.path.join(self.datadir, sourceFile))

    def compileFile(self, sourceFile):
        args = self.setupCompilerArguments(sourceFile)
        compiler = Compiler(*args)
        compiler.run()
        with open(args[3], 'rb') as objData:
            objfile = pickle.load(objData)
            return objfile

    def testMinimal(self):
            objfile = self.compileFile('minimal-module.sps')
            self.assertIsNotNone(objfile)
            self.assertEquals(1, len(objfile.statements))
            self.assertEquals(0, len(objfile.variables))

    def testSimpleAssignment(self):
        objmodule = self.compileFile('simple-assignment.sps')
        self.assertIsInstance(objmodule, Module)
        self.assertIsNotNone(objmodule)
        self.assertEquals(3, len(objmodule.statements))
        self.assertEquals(3, len(objmodule.variables))

    def testExpression(self):
        objfile = self.compileFile('expression.sps')
        expectedStrings = ["x = 5",
                           "y = ((x ^ 2) + 3)",
                           "z = ((x ^ (y - x)) + (3 * (y - 10)))",
                           "w = ((z + ((z * z) / z)) - z)"]
        actualStrings = [str(x) for x in objfile.statements]
        pairs = zip(expectedStrings, actualStrings)
        for expected, actual in pairs:
            self.assertEquals(expected, actual)

    def checkExpectedFile(self, objfile, fileName):
        expectedFile = os.path.join(self.datadir, fileName)
        expectedLines = []
        with open(expectedFile, 'r') as expIn:
            for line in expIn:
                if len(line.strip()) > 0:
                    expectedLines.append(line.strip())
        actualLines = []
        for line in str(objfile).split('\n'):
            if len(line.strip()) > 0:
                actualLines.append(line.strip())

        pairs = zip(expectedLines, actualLines)
        for expected, actual in pairs:
            self.assertEquals(expected, actual)

    def testIf(self):
        objfile = self.compileFile('test-if.sps')
        self.checkExpectedFile(objfile, 'test-ifs.expected')

    def testWhile(self):
        objfile = self.compileFile('while.sps')
        self.checkExpectedFile(objfile, 'while.expected')

    def testFor(self):
        objfile = self.compileFile('for.sps')
        self.checkExpectedFile(objfile, 'for.expected')

    def testFunctions(self):
        objfile = self.compileFile('functions.sps')
        self.checkExpectedFile(objfile, 'functions.expected')
