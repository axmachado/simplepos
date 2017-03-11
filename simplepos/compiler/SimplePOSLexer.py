# Generated from SimplePOS.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO

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


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2.")
        buf.write("\u0113\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\7)\u00ed\n)\f)\16)\u00f0\13)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\7*\u00f9\n*\f*\16*\u00fc\13*\3+\6+\u00ff\n+\r")
        buf.write("+\16+\u0100\3,\3,\3,\7,\u0106\n,\f,\16,\u0109\13,\3,\3")
        buf.write(",\3-\6-\u010e\n-\r-\16-\u010f\3-\3-\3\u00ee\2.\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\f\f\17")
        buf.write("\17$$\5\2\13\f\17\17\"\"\u0118\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\3[\3\2\2\2\5b\3\2\2\2\7i\3\2\2\2\tm\3\2\2")
        buf.write("\2\13t\3\2\2\2\ry\3\2\2\2\17~\3\2\2\2\21\u0084\3\2\2\2")
        buf.write("\23\u0087\3\2\2\2\25\u008c\3\2\2\2\27\u0092\3\2\2\2\31")
        buf.write("\u0098\3\2\2\2\33\u009c\3\2\2\2\35\u00a3\3\2\2\2\37\u00ae")
        buf.write("\3\2\2\2!\u00b0\3\2\2\2#\u00b2\3\2\2\2%\u00b4\3\2\2\2")
        buf.write("\'\u00b6\3\2\2\2)\u00b8\3\2\2\2+\u00ba\3\2\2\2-\u00bc")
        buf.write("\3\2\2\2/\u00be\3\2\2\2\61\u00c0\3\2\2\2\63\u00c2\3\2")
        buf.write("\2\2\65\u00c4\3\2\2\2\67\u00c6\3\2\2\29\u00c8\3\2\2\2")
        buf.write(";\u00ca\3\2\2\2=\u00cc\3\2\2\2?\u00cf\3\2\2\2A\u00d2\3")
        buf.write("\2\2\2C\u00d4\3\2\2\2E\u00d6\3\2\2\2G\u00d9\3\2\2\2I\u00dc")
        buf.write("\3\2\2\2K\u00df\3\2\2\2M\u00e2\3\2\2\2O\u00e5\3\2\2\2")
        buf.write("Q\u00e8\3\2\2\2S\u00f6\3\2\2\2U\u00fe\3\2\2\2W\u0102\3")
        buf.write("\2\2\2Y\u010d\3\2\2\2[\\\7o\2\2\\]\7q\2\2]^\7f\2\2^_\7")
        buf.write("w\2\2_`\7n\2\2`a\7g\2\2a\4\3\2\2\2bc\7i\2\2cd\7n\2\2d")
        buf.write("e\7q\2\2ef\7d\2\2fg\7c\2\2gh\7n\2\2h\6\3\2\2\2ij\7k\2")
        buf.write("\2jk\7p\2\2kl\7v\2\2l\b\3\2\2\2mn\7u\2\2no\7v\2\2op\7")
        buf.write("t\2\2pq\7k\2\2qr\7p\2\2rs\7i\2\2s\n\3\2\2\2tu\7x\2\2u")
        buf.write("v\7q\2\2vw\7k\2\2wx\7f\2\2x\f\3\2\2\2yz\7v\2\2z{\7t\2")
        buf.write("\2{|\7w\2\2|}\7g\2\2}\16\3\2\2\2~\177\7h\2\2\177\u0080")
        buf.write("\7c\2\2\u0080\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\20\3\2\2\2\u0084\u0085\7k\2\2\u0085\u0086")
        buf.write("\7h\2\2\u0086\22\3\2\2\2\u0087\u0088\7g\2\2\u0088\u0089")
        buf.write("\7n\2\2\u0089\u008a\7u\2\2\u008a\u008b\7g\2\2\u008b\24")
        buf.write("\3\2\2\2\u008c\u008d\7y\2\2\u008d\u008e\7j\2\2\u008e\u008f")
        buf.write("\7k\2\2\u008f\u0090\7n\2\2\u0090\u0091\7g\2\2\u0091\26")
        buf.write("\3\2\2\2\u0092\u0093\7d\2\2\u0093\u0094\7t\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7c\2\2\u0096\u0097\7m\2\2\u0097\30")
        buf.write("\3\2\2\2\u0098\u0099\7h\2\2\u0099\u009a\7q\2\2\u009a\u009b")
        buf.write("\7t\2\2\u009b\32\3\2\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u009f\7v\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7p\2\2\u00a2\34\3\2\2\2\u00a3\u00a4")
        buf.write("\7e\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7")
        buf.write("\7n\2\2\u00a7\u00a8\7o\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7f\2\2\u00aa\u00ab\7w\2\2\u00ab\u00ac\7n\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\36\3\2\2\2\u00ae\u00af\7*\2\2\u00af \3\2")
        buf.write("\2\2\u00b0\u00b1\7+\2\2\u00b1\"\3\2\2\2\u00b2\u00b3\7")
        buf.write("}\2\2\u00b3$\3\2\2\2\u00b4\u00b5\7\177\2\2\u00b5&\3\2")
        buf.write("\2\2\u00b6\u00b7\7.\2\2\u00b7(\3\2\2\2\u00b8\u00b9\7=")
        buf.write("\2\2\u00b9*\3\2\2\2\u00ba\u00bb\7(\2\2\u00bb,\3\2\2\2")
        buf.write("\u00bc\u00bd\7?\2\2\u00bd.\3\2\2\2\u00be\u00bf\7-\2\2")
        buf.write("\u00bf\60\3\2\2\2\u00c0\u00c1\7/\2\2\u00c1\62\3\2\2\2")
        buf.write("\u00c2\u00c3\7,\2\2\u00c3\64\3\2\2\2\u00c4\u00c5\7\61")
        buf.write("\2\2\u00c5\66\3\2\2\2\u00c6\u00c7\7\'\2\2\u00c78\3\2\2")
        buf.write("\2\u00c8\u00c9\7`\2\2\u00c9:\3\2\2\2\u00ca\u00cb\7#\2")
        buf.write("\2\u00cb<\3\2\2\2\u00cc\u00cd\7(\2\2\u00cd\u00ce\7(\2")
        buf.write("\2\u00ce>\3\2\2\2\u00cf\u00d0\7~\2\2\u00d0\u00d1\7~\2")
        buf.write("\2\u00d1@\3\2\2\2\u00d2\u00d3\7@\2\2\u00d3B\3\2\2\2\u00d4")
        buf.write("\u00d5\7>\2\2\u00d5D\3\2\2\2\u00d6\u00d7\7@\2\2\u00d7")
        buf.write("\u00d8\7?\2\2\u00d8F\3\2\2\2\u00d9\u00da\7>\2\2\u00da")
        buf.write("\u00db\7?\2\2\u00dbH\3\2\2\2\u00dc\u00dd\7?\2\2\u00dd")
        buf.write("\u00de\7?\2\2\u00deJ\3\2\2\2\u00df\u00e0\7#\2\2\u00e0")
        buf.write("\u00e1\7?\2\2\u00e1L\3\2\2\2\u00e2\u00e3\7-\2\2\u00e3")
        buf.write("\u00e4\7-\2\2\u00e4N\3\2\2\2\u00e5\u00e6\7/\2\2\u00e6")
        buf.write("\u00e7\7/\2\2\u00e7P\3\2\2\2\u00e8\u00e9\7\61\2\2\u00e9")
        buf.write("\u00ea\7,\2\2\u00ea\u00ee\3\2\2\2\u00eb\u00ed\13\2\2\2")
        buf.write("\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ef\3")
        buf.write("\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f1\u00f2\7,\2\2\u00f2\u00f3\7\61\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u00f5\b)\2\2\u00f5R\3\2\2\2\u00f6")
        buf.write("\u00fa\t\2\2\2\u00f7\u00f9\t\3\2\2\u00f8\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3")
        buf.write("\2\2\2\u00fbT\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff")
        buf.write("\t\4\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101V\3\2\2\2\u0102")
        buf.write("\u0107\7$\2\2\u0103\u0106\n\5\2\2\u0104\u0106\7$\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3")
        buf.write("\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\7$\2\2\u010bX\3")
        buf.write("\2\2\2\u010c\u010e\t\6\2\2\u010d\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\b-\3\2\u0112Z\3\2\2\2\t\2\u00ee")
        buf.write("\u00fa\u0100\u0105\u0107\u010f\4\2\3\2\b\2\2")
        return buf.getvalue()


class SimplePOSLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    MODULE = 1
    GLOBAL = 2
    INT = 3
    STRING = 4
    VOID = 5
    TRUE = 6
    FALSE = 7
    IF = 8
    ELSE = 9
    WHILE = 10
    BREAK = 11
    FOR = 12
    RETURN = 13
    EXECMODULE = 14
    LPAR = 15
    RPAR = 16
    LCURL = 17
    RCURL = 18
    COMMA = 19
    SEMICOLOM = 20
    REFMARK = 21
    ASSIGN = 22
    PLUS = 23
    MINUS = 24
    TIMES = 25
    DIV = 26
    MOD = 27
    EXP = 28
    NOT = 29
    AND = 30
    OR = 31
    GT = 32
    LT = 33
    GE = 34
    LE = 35
    EQ = 36
    NE = 37
    INCOPER = 38
    DECOPER = 39
    BLOCK_COMMENT = 40
    ID = 41
    DIGIT = 42
    STRVALUE = 43
    WS = 44

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'module'", "'global'", "'int'", "'string'", "'void'", "'true'", 
            "'false'", "'if'", "'else'", "'while'", "'break'", "'for'", 
            "'return'", "'callmodule'", "'('", "')'", "'{'", "'}'", "','", 
            "';'", "'&'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
            "'!'", "'&&'", "'||'", "'>'", "'<'", "'>='", "'<='", "'=='", 
            "'!='", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>",
            "MODULE", "GLOBAL", "INT", "STRING", "VOID", "TRUE", "FALSE", 
            "IF", "ELSE", "WHILE", "BREAK", "FOR", "RETURN", "EXECMODULE", 
            "LPAR", "RPAR", "LCURL", "RCURL", "COMMA", "SEMICOLOM", "REFMARK", 
            "ASSIGN", "PLUS", "MINUS", "TIMES", "DIV", "MOD", "EXP", "NOT", 
            "AND", "OR", "GT", "LT", "GE", "LE", "EQ", "NE", "INCOPER", 
            "DECOPER", "BLOCK_COMMENT", "ID", "DIGIT", "STRVALUE", "WS" ]

    ruleNames = [ "MODULE", "GLOBAL", "INT", "STRING", "VOID", "TRUE", "FALSE", 
                  "IF", "ELSE", "WHILE", "BREAK", "FOR", "RETURN", "EXECMODULE", 
                  "LPAR", "RPAR", "LCURL", "RCURL", "COMMA", "SEMICOLOM", 
                  "REFMARK", "ASSIGN", "PLUS", "MINUS", "TIMES", "DIV", 
                  "MOD", "EXP", "NOT", "AND", "OR", "GT", "LT", "GE", "LE", 
                  "EQ", "NE", "INCOPER", "DECOPER", "BLOCK_COMMENT", "ID", 
                  "DIGIT", "STRVALUE", "WS" ]

    grammarFileName = "SimplePOS.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


