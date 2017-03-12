# Generated from SimplePOS.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimplePOSParser import SimplePOSParser
else:
    from SimplePOSParser import SimplePOSParser
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


# This class defines a complete listener for a parse tree produced by SimplePOSParser.
class SimplePOSListener(ParseTreeListener):

    # Enter a parse tree produced by SimplePOSParser#sourcefile.
    def enterSourcefile(self, ctx:SimplePOSParser.SourcefileContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#sourcefile.
    def exitSourcefile(self, ctx:SimplePOSParser.SourcefileContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#moduledef.
    def enterModuledef(self, ctx:SimplePOSParser.ModuledefContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#moduledef.
    def exitModuledef(self, ctx:SimplePOSParser.ModuledefContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#constblock.
    def enterConstblock(self, ctx:SimplePOSParser.ConstblockContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#constblock.
    def exitConstblock(self, ctx:SimplePOSParser.ConstblockContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#vardefblock.
    def enterVardefblock(self, ctx:SimplePOSParser.VardefblockContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#vardefblock.
    def exitVardefblock(self, ctx:SimplePOSParser.VardefblockContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#functiondef.
    def enterFunctiondef(self, ctx:SimplePOSParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#functiondef.
    def exitFunctiondef(self, ctx:SimplePOSParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#vardef_item.
    def enterVardef_item(self, ctx:SimplePOSParser.Vardef_itemContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#vardef_item.
    def exitVardef_item(self, ctx:SimplePOSParser.Vardef_itemContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#vardef.
    def enterVardef(self, ctx:SimplePOSParser.VardefContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#vardef.
    def exitVardef(self, ctx:SimplePOSParser.VardefContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#constdef_item.
    def enterConstdef_item(self, ctx:SimplePOSParser.Constdef_itemContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#constdef_item.
    def exitConstdef_item(self, ctx:SimplePOSParser.Constdef_itemContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#constdef.
    def enterConstdef(self, ctx:SimplePOSParser.ConstdefContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#constdef.
    def exitConstdef(self, ctx:SimplePOSParser.ConstdefContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#typename.
    def enterTypename(self, ctx:SimplePOSParser.TypenameContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#typename.
    def exitTypename(self, ctx:SimplePOSParser.TypenameContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#argdef.
    def enterArgdef(self, ctx:SimplePOSParser.ArgdefContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#argdef.
    def exitArgdef(self, ctx:SimplePOSParser.ArgdefContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#arglist.
    def enterArglist(self, ctx:SimplePOSParser.ArglistContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#arglist.
    def exitArglist(self, ctx:SimplePOSParser.ArglistContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#stmlist.
    def enterStmlist(self, ctx:SimplePOSParser.StmlistContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#stmlist.
    def exitStmlist(self, ctx:SimplePOSParser.StmlistContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#stm.
    def enterStm(self, ctx:SimplePOSParser.StmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#stm.
    def exitStm(self, ctx:SimplePOSParser.StmContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#simplestm.
    def enterSimplestm(self, ctx:SimplePOSParser.SimplestmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#simplestm.
    def exitSimplestm(self, ctx:SimplePOSParser.SimplestmContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#stmline.
    def enterStmline(self, ctx:SimplePOSParser.StmlineContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#stmline.
    def exitStmline(self, ctx:SimplePOSParser.StmlineContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#modulecall.
    def enterModulecall(self, ctx:SimplePOSParser.ModulecallContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#modulecall.
    def exitModulecall(self, ctx:SimplePOSParser.ModulecallContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#functioncall.
    def enterFunctioncall(self, ctx:SimplePOSParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#functioncall.
    def exitFunctioncall(self, ctx:SimplePOSParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#paramlist.
    def enterParamlist(self, ctx:SimplePOSParser.ParamlistContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#paramlist.
    def exitParamlist(self, ctx:SimplePOSParser.ParamlistContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#returnstm.
    def enterReturnstm(self, ctx:SimplePOSParser.ReturnstmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#returnstm.
    def exitReturnstm(self, ctx:SimplePOSParser.ReturnstmContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#value.
    def enterValue(self, ctx:SimplePOSParser.ValueContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#value.
    def exitValue(self, ctx:SimplePOSParser.ValueContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#expression.
    def enterExpression(self, ctx:SimplePOSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#expression.
    def exitExpression(self, ctx:SimplePOSParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#add_sub.
    def enterAdd_sub(self, ctx:SimplePOSParser.Add_subContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#add_sub.
    def exitAdd_sub(self, ctx:SimplePOSParser.Add_subContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#term.
    def enterTerm(self, ctx:SimplePOSParser.TermContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#term.
    def exitTerm(self, ctx:SimplePOSParser.TermContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#times_div.
    def enterTimes_div(self, ctx:SimplePOSParser.Times_divContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#times_div.
    def exitTimes_div(self, ctx:SimplePOSParser.Times_divContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#factor.
    def enterFactor(self, ctx:SimplePOSParser.FactorContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#factor.
    def exitFactor(self, ctx:SimplePOSParser.FactorContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#rexp.
    def enterRexp(self, ctx:SimplePOSParser.RexpContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#rexp.
    def exitRexp(self, ctx:SimplePOSParser.RexpContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#atom.
    def enterAtom(self, ctx:SimplePOSParser.AtomContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#atom.
    def exitAtom(self, ctx:SimplePOSParser.AtomContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#log_expression.
    def enterLog_expression(self, ctx:SimplePOSParser.Log_expressionContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#log_expression.
    def exitLog_expression(self, ctx:SimplePOSParser.Log_expressionContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#log_oper.
    def enterLog_oper(self, ctx:SimplePOSParser.Log_operContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#log_oper.
    def exitLog_oper(self, ctx:SimplePOSParser.Log_operContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#log_term.
    def enterLog_term(self, ctx:SimplePOSParser.Log_termContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#log_term.
    def exitLog_term(self, ctx:SimplePOSParser.Log_termContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#log_rel.
    def enterLog_rel(self, ctx:SimplePOSParser.Log_relContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#log_rel.
    def exitLog_rel(self, ctx:SimplePOSParser.Log_relContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#assignment.
    def enterAssignment(self, ctx:SimplePOSParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#assignment.
    def exitAssignment(self, ctx:SimplePOSParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#blockstm.
    def enterBlockstm(self, ctx:SimplePOSParser.BlockstmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#blockstm.
    def exitBlockstm(self, ctx:SimplePOSParser.BlockstmContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#intvalue.
    def enterIntvalue(self, ctx:SimplePOSParser.IntvalueContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#intvalue.
    def exitIntvalue(self, ctx:SimplePOSParser.IntvalueContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#ifelse.
    def enterIfelse(self, ctx:SimplePOSParser.IfelseContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#ifelse.
    def exitIfelse(self, ctx:SimplePOSParser.IfelseContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#whilestm.
    def enterWhilestm(self, ctx:SimplePOSParser.WhilestmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#whilestm.
    def exitWhilestm(self, ctx:SimplePOSParser.WhilestmContext):
        pass


    # Enter a parse tree produced by SimplePOSParser#forstm.
    def enterForstm(self, ctx:SimplePOSParser.ForstmContext):
        pass

    # Exit a parse tree produced by SimplePOSParser#forstm.
    def exitForstm(self, ctx:SimplePOSParser.ForstmContext):
        pass


