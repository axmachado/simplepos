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
import logging

from .base import POSXMLStatement
from . import boolean

# pylint: disable=C0103
logger = logging.getLogger("link")


class BreakStatement(POSXMLStatement):
    """
    Break an while loop
    """
    def __init__(self):
        super(BreakStatement, self).__init__()

    def emitStatement(self):
        "emits the POSXML instruction"
        return ('<break/>',)


class IfStatement(POSXMLStatement):
    """
    If/Then/Else statement
    """
    def __init__(self, ifCodeBlock):
        super(IfStatement, self).__init__()
        self.codeBlock = ifCodeBlock
        self.conditional = None
        self.ifCodeBlock = None
        self.elseCodeBlock = None

    def blocks(self):
        result = []
        if self.ifCodeBlock:
            result.append(self.ifCodeBlock)
        if self.elseCodeBlock:
            result.append(self.elseCodeBlock)
        return result

    def usesVariable(self, name):
        result = self.conditional.usesVariable(name)
        return result or super(IfStatement,self).usesVariable(name)

    def processIf(self, ifStatement):
        "Processes the IF statement"
        # import here to avoid cyclic import problems
        from .code import POSXMLCode

        logger.debug("Processing if: %s", str(ifStatement))
        # generate the conditional code
        factory = boolean.ConditionalFactory()
        self.conditional = factory.getConditional(ifStatement.condition)

        # adds the expression evaluation code to the block
        self.codeBlock.enterScope()
        self.conditional.preConditionalCode(self.codeBlock)
        self.codeBlock.exitScope()

        # if block
        self.ifCodeBlock = POSXMLCode(self.codeBlock, "if-block")
        self.codeBlock.enterScope()
        for stm in ifStatement.ifBlock.statements:
            self.ifCodeBlock.statement(stm)
        self.codeBlock.exitScope()

        # else block
        self.codeBlock.enterScope()
        if ifStatement.elseBlock:
            self.elseCodeBlock = POSXMLCode(self.codeBlock, "else-block")
            for stm in ifStatement.elseBlock.statements:
                self.elseCodeBlock.statement(stm)
        self.codeBlock.exitScope()


    def selfGenerated(self, conditional, ifBlockStatements,
                      elseBlockStatements=None):
        """
        add the statements for a self generated if to evaluate partial results
        of expressions
        """
        # import here to avoid cyclic import problems
        from .code import POSXMLCode

        # conditional (already as Conditional object, not expression)
        self.conditional = conditional
        self.codeBlock.enterScope()
        self.conditional.preConditionalCode(self.codeBlock)
        self.codeBlock.exitScope()

        # if block
        self.ifCodeBlock = POSXMLCode(self.codeBlock, 'if-block')
        self.codeBlock.enterScope()
        self.ifCodeBlock.addStatements(*ifBlockStatements)
        self.codeBlock.exitScope()

        # else block
        if elseBlockStatements:
            self.codeBlock.enterScope()
            self.elseCodeBlock = POSXMLCode(self.codeBlock, 'else-block')
            self.elseCodeBlock.addStatements(*elseBlockStatements)
            self.codeBlock.exitScope()
        else:
            elseBlockStatements = None

    def _emitIfBlock(self):
        "emits POSXML code for if block"
        result = []
        for stm in self.ifCodeBlock.statements:
            result.extend(['    ' + line for line in stm.emitStatement()])
        return result

    def _emitElseBlock(self):
        "emits POSXML code for else block"
        result = []
        for stm in self.elseCodeBlock.statements:
            result.extend(['    ' + line for line in stm.emitStatement()])
        return result

    def emitStatement(self):
        "emits the entire if statement"
        result = []

        if isinstance(self.conditional, boolean.ConstantConditional):
            result.append('<!-- if com condicional constante -->')
            if self.conditional.value:
                result.extend(self._emitIfBlock())
            else:
                if self.elseCodeBlock:
                    result.extend(self._emitElseBlock())
        else:
            result.append('<if %s>' % self.conditional.emit())
            result.extend(self._emitIfBlock())
            if self.elseCodeBlock:
                result.append('<else/>')
                result.extend(self._emitElseBlock())
            result.append("</if>")
        return result


class WhileStatement(POSXMLStatement):
    """
    While
    """
    def __init__(self, whileCodeBlock):
        super(WhileStatement, self).__init__()
        self.codeBlock = whileCodeBlock
        self.conditional = None
        self.internalBlock = None
        self.controlVariable = None

    def blocks(self):
        if self.internalBlock:
            return (self.internalBlock,)

    def usesVariable(self, name):
        return self.conditional.usesVariable(name) \
               or super(WhileStatement, self).usesVariable(name)

    def processWhile(self, whileStatement):
        """
        Process the while statement
        """
        # import here to avoid cyclic import problems
        from .code import POSXMLCode

        factory = boolean.ConditionalFactory()
        self.conditional = factory.getConditional(whileStatement.condition)
        self.controlVariable = self.codeBlock.currentScope().autoInt()
        self.codeBlock.enterScope()
        if hasattr(whileStatement, 'initialization'):
            # it's a for statement, the initialization code is the first
            # thig to be executed
            self.codeBlock.statement(whileStatement.initialization)

        self.conditional.preConditionalCode(self.codeBlock,
                                            self.controlVariable)
        self.codeBlock.exitScope()
        self.internalBlock = POSXMLCode(self.codeBlock)
        for stm in whileStatement.block.statements:
            self.internalBlock.statement(stm)

        # repeat the conditional code at the end of the loop in order to
        # evaluate the condition at the beginning of the next iteration
        self.codeBlock.enterScope()
        if hasattr(whileStatement, 'increment'):
            # it's a for loop, the increment must be executed before the
            # condition is evaluated again
            self.internalBlock.statement(whileStatement.increment)
        self.conditional.preConditionalCode(self.internalBlock,
                                            self.controlVariable)
        self.codeBlock.exitScope()

    def emitStatement(self):
        "emit the while statement"
        result = ['<while %s>' % self.conditional.emit()]
        for stm in self.internalBlock.statements:
            result.extend(['    ' + line for line in stm.emitStatement()])
        result.append('</while>')
        return result


class FunctionDefinition(POSXMLStatement):
    """
    User defined function
    """
    def __init__(self, moduleCodeBlock):
        super(FunctionDefinition, self).__init__()
        from .code import POSXMLCode
        self.parentBlock = moduleCodeBlock
        self.block = POSXMLCode(moduleCodeBlock)

    def blocks(self):
        return (self.block,)