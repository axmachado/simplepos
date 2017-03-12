# Generated from SimplePOS.g4 by ANTLR 4.6
# encoding: utf-8
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\62")
        buf.write("\u017e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\5\2P\n\2\3\2\5\2S\n\2\3\2\5\2V\n\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3_\n\3\3\3\5\3b\n\3\3\3\3\3\3")
        buf.write("\4\6\4g\n\4\r\4\16\4h\3\5\6\5l\n\5\r\5\16\5m\3\5\3\5\6")
        buf.write("\5r\n\5\r\5\16\5s\3\5\3\5\5\5x\n\5\3\6\3\6\5\6|\n\6\3")
        buf.write("\6\3\6\3\6\5\6\u0081\n\6\3\6\3\6\3\6\5\6\u0086\n\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\5\7\u008e\n\7\3\b\5\b\u0091\n\b\3")
        buf.write("\b\3\b\3\b\3\b\7\b\u0097\n\b\f\b\16\b\u009a\13\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a4\n\t\3\n\3\n\3\n\3")
        buf.write("\n\7\n\u00aa\n\n\f\n\16\n\u00ad\13\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u00b7\n\n\f\n\16\n\u00ba\13\n\3\n\3")
        buf.write("\n\5\n\u00be\n\n\3\13\3\13\3\f\3\f\5\f\u00c4\n\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\7\r\u00cb\n\r\f\r\16\r\u00ce\13\r\3\16")
        buf.write("\6\16\u00d1\n\16\r\16\16\16\u00d2\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00db\n\17\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00e9\n\21\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00ef\n\22\3\22\3\22\3\23\3\23\3")
        buf.write("\23\5\23\u00f6\n\23\3\23\3\23\3\24\3\24\3\24\7\24\u00fd")
        buf.write("\n\24\f\24\16\24\u0100\13\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\5\26\u0107\n\26\3\27\3\27\7\27\u010b\n\27\f\27\16\27")
        buf.write("\u010e\13\27\3\30\3\30\3\30\3\31\3\31\7\31\u0115\n\31")
        buf.write("\f\31\16\31\u0118\13\31\3\32\3\32\3\32\3\33\3\33\7\33")
        buf.write("\u011f\n\33\f\33\16\33\u0122\13\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0134\n\35\3\36\5\36\u0137\n\36\3\36\3\36\7")
        buf.write("\36\u013b\n\36\f\36\16\36\u013e\13\36\3\37\3\37\3\37\3")
        buf.write(" \3 \7 \u0145\n \f \16 \u0148\13 \3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\5#\u0153\n#\3#\7#\u0156\n#\f#\16#\u0159\13")
        buf.write("#\3#\3#\3$\5$\u015e\n$\3$\6$\u0161\n$\r$\16$\u0162\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\5%\u016c\n%\3&\3&\3&\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\2\2(\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJL\2\b\3\2\7\b\3\2*+\3\2\33\34\3\2\35\37\3\2\"#")
        buf.write("\3\2$)\u018d\2O\3\2\2\2\4Z\3\2\2\2\6f\3\2\2\2\bw\3\2\2")
        buf.write("\2\n{\3\2\2\2\f\u008a\3\2\2\2\16\u0090\3\2\2\2\20\u00a3")
        buf.write("\3\2\2\2\22\u00bd\3\2\2\2\24\u00bf\3\2\2\2\26\u00c1\3")
        buf.write("\2\2\2\30\u00c7\3\2\2\2\32\u00d0\3\2\2\2\34\u00da\3\2")
        buf.write("\2\2\36\u00dc\3\2\2\2 \u00e8\3\2\2\2\"\u00ea\3\2\2\2$")
        buf.write("\u00f2\3\2\2\2&\u00f9\3\2\2\2(\u0101\3\2\2\2*\u0106\3")
        buf.write("\2\2\2,\u0108\3\2\2\2.\u010f\3\2\2\2\60\u0112\3\2\2\2")
        buf.write("\62\u0119\3\2\2\2\64\u011c\3\2\2\2\66\u0123\3\2\2\28\u0133")
        buf.write("\3\2\2\2:\u0136\3\2\2\2<\u013f\3\2\2\2>\u0142\3\2\2\2")
        buf.write("@\u0149\3\2\2\2B\u014c\3\2\2\2D\u0150\3\2\2\2F\u015d\3")
        buf.write("\2\2\2H\u0164\3\2\2\2J\u016d\3\2\2\2L\u0173\3\2\2\2NP")
        buf.write("\5\4\3\2ON\3\2\2\2OP\3\2\2\2PR\3\2\2\2QS\5\6\4\2RQ\3\2")
        buf.write("\2\2RS\3\2\2\2SU\3\2\2\2TV\5\b\5\2UT\3\2\2\2UV\3\2\2\2")
        buf.write("VW\3\2\2\2WX\5\32\16\2XY\7\2\2\3Y\3\3\2\2\2Z[\7\3\2\2")
        buf.write("[a\7-\2\2\\^\7\23\2\2]_\5\30\r\2^]\3\2\2\2^_\3\2\2\2_")
        buf.write("`\3\2\2\2`b\7\24\2\2a\\\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd")
        buf.write("\7\30\2\2d\5\3\2\2\2eg\5\22\n\2fe\3\2\2\2gh\3\2\2\2hf")
        buf.write("\3\2\2\2hi\3\2\2\2i\7\3\2\2\2jl\5\16\b\2kj\3\2\2\2lm\3")
        buf.write("\2\2\2mk\3\2\2\2mn\3\2\2\2nx\3\2\2\2oq\7\25\2\2pr\5\16")
        buf.write("\b\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3\2\2\2tu\3\2\2\2")
        buf.write("uv\7\26\2\2vx\3\2\2\2wk\3\2\2\2wo\3\2\2\2x\t\3\2\2\2y")
        buf.write("|\5\24\13\2z|\7\t\2\2{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}~")
        buf.write("\7-\2\2~\u0080\7\23\2\2\177\u0081\5\30\r\2\u0080\177\3")
        buf.write("\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\7\24\2\2\u0083\u0085\7\25\2\2\u0084\u0086\5\b\5\2\u0085")
        buf.write("\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u0088\5\32\16\2\u0088\u0089\7\26\2\2\u0089\13\3")
        buf.write("\2\2\2\u008a\u008d\7-\2\2\u008b\u008c\7\32\2\2\u008c\u008e")
        buf.write("\5*\26\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e")
        buf.write("\r\3\2\2\2\u008f\u0091\7\4\2\2\u0090\u008f\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\5\24\13")
        buf.write("\2\u0093\u0098\5\f\7\2\u0094\u0095\7\27\2\2\u0095\u0097")
        buf.write("\5\f\7\2\u0096\u0094\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009b\3\2\2\2")
        buf.write("\u009a\u0098\3\2\2\2\u009b\u009c\7\30\2\2\u009c\17\3\2")
        buf.write("\2\2\u009d\u009e\7-\2\2\u009e\u009f\7\32\2\2\u009f\u00a4")
        buf.write("\7/\2\2\u00a0\u00a1\7-\2\2\u00a1\u00a2\7\32\2\2\u00a2")
        buf.write("\u00a4\5F$\2\u00a3\u009d\3\2\2\2\u00a3\u00a0\3\2\2\2\u00a4")
        buf.write("\21\3\2\2\2\u00a5\u00a6\7\5\2\2\u00a6\u00ab\5\20\t\2\u00a7")
        buf.write("\u00a8\7\27\2\2\u00a8\u00aa\5\20\t\2\u00a9\u00a7\3\2\2")
        buf.write("\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae")
        buf.write("\u00af\7\30\2\2\u00af\u00be\3\2\2\2\u00b0\u00b1\7\6\2")
        buf.write("\2\u00b1\u00b2\7\5\2\2\u00b2\u00b3\5\24\13\2\u00b3\u00b8")
        buf.write("\7-\2\2\u00b4\u00b5\7\27\2\2\u00b5\u00b7\7-\2\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00bb\u00bc\7\30\2\2\u00bc\u00be\3\2\2\2\u00bd")
        buf.write("\u00a5\3\2\2\2\u00bd\u00b0\3\2\2\2\u00be\23\3\2\2\2\u00bf")
        buf.write("\u00c0\t\2\2\2\u00c0\25\3\2\2\2\u00c1\u00c3\5\24\13\2")
        buf.write("\u00c2\u00c4\7\31\2\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\7-\2\2\u00c6")
        buf.write("\27\3\2\2\2\u00c7\u00cc\5\26\f\2\u00c8\u00c9\7\27\2\2")
        buf.write("\u00c9\u00cb\5\26\f\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce")
        buf.write("\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\31\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\5\34\17\2")
        buf.write("\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3")
        buf.write("\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\33\3\2\2\2\u00d4\u00db")
        buf.write("\5\36\20\2\u00d5\u00db\5D#\2\u00d6\u00db\5H%\2\u00d7\u00db")
        buf.write("\5J&\2\u00d8\u00db\5L\'\2\u00d9\u00db\5\n\6\2\u00da\u00d4")
        buf.write("\3\2\2\2\u00da\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2\u00da")
        buf.write("\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\35\3\2\2\2\u00dc\u00dd\5 \21\2\u00dd\u00de\7\30")
        buf.write("\2\2\u00de\37\3\2\2\2\u00df\u00e9\5$\23\2\u00e0\u00e9")
        buf.write("\5\"\22\2\u00e1\u00e9\5B\"\2\u00e2\u00e9\5(\25\2\u00e3")
        buf.write("\u00e9\7\17\2\2\u00e4\u00e5\7-\2\2\u00e5\u00e9\t\3\2\2")
        buf.write("\u00e6\u00e7\t\3\2\2\u00e7\u00e9\7-\2\2\u00e8\u00df\3")
        buf.write("\2\2\2\u00e8\u00e0\3\2\2\2\u00e8\u00e1\3\2\2\2\u00e8\u00e2")
        buf.write("\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e4\3\2\2\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e9!\3\2\2\2\u00ea\u00eb\7\22\2\2\u00eb")
        buf.write("\u00ec\7-\2\2\u00ec\u00ee\7\23\2\2\u00ed\u00ef\5&\24\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0\u00f1\7\24\2\2\u00f1#\3\2\2\2\u00f2\u00f3")
        buf.write("\7-\2\2\u00f3\u00f5\7\23\2\2\u00f4\u00f6\5&\24\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2")
        buf.write("\u00f7\u00f8\7\24\2\2\u00f8%\3\2\2\2\u00f9\u00fe\5*\26")
        buf.write("\2\u00fa\u00fb\7\27\2\2\u00fb\u00fd\5*\26\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe")
        buf.write("\u00ff\3\2\2\2\u00ff\'\3\2\2\2\u0100\u00fe\3\2\2\2\u0101")
        buf.write("\u0102\7\21\2\2\u0102\u0103\5*\26\2\u0103)\3\2\2\2\u0104")
        buf.write("\u0107\7/\2\2\u0105\u0107\5,\27\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0105\3\2\2\2\u0107+\3\2\2\2\u0108\u010c\5\60\31")
        buf.write("\2\u0109\u010b\5.\30\2\u010a\u0109\3\2\2\2\u010b\u010e")
        buf.write("\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("-\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\t\4\2\2\u0110")
        buf.write("\u0111\5\60\31\2\u0111/\3\2\2\2\u0112\u0116\5\64\33\2")
        buf.write("\u0113\u0115\5\62\32\2\u0114\u0113\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\61\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\t\5\2\2\u011a")
        buf.write("\u011b\5\64\33\2\u011b\63\3\2\2\2\u011c\u0120\58\35\2")
        buf.write("\u011d\u011f\5\66\34\2\u011e\u011d\3\2\2\2\u011f\u0122")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\65\3\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7 \2\2\u0124")
        buf.write("\u0125\58\35\2\u0125\67\3\2\2\2\u0126\u0134\7-\2\2\u0127")
        buf.write("\u0134\5F$\2\u0128\u0134\5$\23\2\u0129\u0134\7\n\2\2\u012a")
        buf.write("\u0134\7\13\2\2\u012b\u012c\7\23\2\2\u012c\u012d\5,\27")
        buf.write("\2\u012d\u012e\7\24\2\2\u012e\u0134\3\2\2\2\u012f\u0130")
        buf.write("\7\23\2\2\u0130\u0131\5:\36\2\u0131\u0132\7\24\2\2\u0132")
        buf.write("\u0134\3\2\2\2\u0133\u0126\3\2\2\2\u0133\u0127\3\2\2\2")
        buf.write("\u0133\u0128\3\2\2\2\u0133\u0129\3\2\2\2\u0133\u012a\3")
        buf.write("\2\2\2\u0133\u012b\3\2\2\2\u0133\u012f\3\2\2\2\u01349")
        buf.write("\3\2\2\2\u0135\u0137\7!\2\2\u0136\u0135\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013c\5> \2\u0139")
        buf.write("\u013b\5<\37\2\u013a\u0139\3\2\2\2\u013b\u013e\3\2\2\2")
        buf.write("\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d;\3\2\2")
        buf.write("\2\u013e\u013c\3\2\2\2\u013f\u0140\t\6\2\2\u0140\u0141")
        buf.write("\5> \2\u0141=\3\2\2\2\u0142\u0146\5*\26\2\u0143\u0145")
        buf.write("\5@!\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147?\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014a\t\7\2\2\u014a\u014b\5*\26\2\u014b")
        buf.write("A\3\2\2\2\u014c\u014d\7-\2\2\u014d\u014e\7\32\2\2\u014e")
        buf.write("\u014f\5*\26\2\u014fC\3\2\2\2\u0150\u0152\7\25\2\2\u0151")
        buf.write("\u0153\5\b\5\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\u0157\3\2\2\2\u0154\u0156\5\34\17\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u015a\u015b\7\26\2\2\u015bE\3\2\2\2\u015c\u015e\7\34")
        buf.write("\2\2\u015d\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160")
        buf.write("\3\2\2\2\u015f\u0161\7.\2\2\u0160\u015f\3\2\2\2\u0161")
        buf.write("\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163G\3\2\2\2\u0164\u0165\7\f\2\2\u0165\u0166\7\23\2")
        buf.write("\2\u0166\u0167\5:\36\2\u0167\u0168\7\24\2\2\u0168\u016b")
        buf.write("\5D#\2\u0169\u016a\7\r\2\2\u016a\u016c\5D#\2\u016b\u0169")
        buf.write("\3\2\2\2\u016b\u016c\3\2\2\2\u016cI\3\2\2\2\u016d\u016e")
        buf.write("\7\16\2\2\u016e\u016f\7\23\2\2\u016f\u0170\5:\36\2\u0170")
        buf.write("\u0171\7\24\2\2\u0171\u0172\5D#\2\u0172K\3\2\2\2\u0173")
        buf.write("\u0174\7\20\2\2\u0174\u0175\7\23\2\2\u0175\u0176\5 \21")
        buf.write("\2\u0176\u0177\7\30\2\2\u0177\u0178\5:\36\2\u0178\u0179")
        buf.write("\7\30\2\2\u0179\u017a\5 \21\2\u017a\u017b\7\24\2\2\u017b")
        buf.write("\u017c\5D#\2\u017cM\3\2\2\2*ORU^ahmsw{\u0080\u0085\u008d")
        buf.write("\u0090\u0098\u00a3\u00ab\u00b8\u00bd\u00c3\u00cc\u00d2")
        buf.write("\u00da\u00e8\u00ee\u00f5\u00fe\u0106\u010c\u0116\u0120")
        buf.write("\u0133\u0136\u013c\u0146\u0152\u0157\u015d\u0162\u016b")
        return buf.getvalue()


class SimplePOSParser ( Parser ):

    grammarFileName = "SimplePOS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'module'", "'global'", "'const'", "'extern'", 
                     "'int'", "'string'", "'void'", "'true'", "'false'", 
                     "'if'", "'else'", "'while'", "'break'", "'for'", "'return'", 
                     "'callmodule'", "'('", "')'", "'{'", "'}'", "','", 
                     "';'", "'&'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'^'", "'!'", "'&&'", "'||'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'++'", "'--'" ]

    symbolicNames = [ "<INVALID>", "MODULE", "GLOBAL", "CONST", "EXTERN", 
                      "INT", "STRING", "VOID", "TRUE", "FALSE", "IF", "ELSE", 
                      "WHILE", "BREAK", "FOR", "RETURN", "EXECMODULE", "LPAR", 
                      "RPAR", "LCURL", "RCURL", "COMMA", "SEMICOLOM", "REFMARK", 
                      "ASSIGN", "PLUS", "MINUS", "TIMES", "SLASH", "MOD", 
                      "EXP", "NOT", "AND", "OR", "GT", "LT", "GE", "LE", 
                      "EQ", "NE", "INCOPER", "DECOPER", "BLOCK_COMMENT", 
                      "ID", "DIGIT", "STRVALUE", "SINGLELINE_COMMENT", "MULTILINE_COMMENT", 
                      "WS" ]

    RULE_sourcefile = 0
    RULE_moduledef = 1
    RULE_constblock = 2
    RULE_vardefblock = 3
    RULE_functiondef = 4
    RULE_vardef_item = 5
    RULE_vardef = 6
    RULE_constdef_item = 7
    RULE_constdef = 8
    RULE_typename = 9
    RULE_argdef = 10
    RULE_arglist = 11
    RULE_stmlist = 12
    RULE_stm = 13
    RULE_simplestm = 14
    RULE_stmline = 15
    RULE_modulecall = 16
    RULE_functioncall = 17
    RULE_paramlist = 18
    RULE_returnstm = 19
    RULE_value = 20
    RULE_expression = 21
    RULE_add_sub = 22
    RULE_term = 23
    RULE_times_div = 24
    RULE_factor = 25
    RULE_rexp = 26
    RULE_atom = 27
    RULE_log_expression = 28
    RULE_log_oper = 29
    RULE_log_term = 30
    RULE_log_rel = 31
    RULE_assignment = 32
    RULE_blockstm = 33
    RULE_intvalue = 34
    RULE_ifelse = 35
    RULE_whilestm = 36
    RULE_forstm = 37

    ruleNames =  [ "sourcefile", "moduledef", "constblock", "vardefblock", 
                   "functiondef", "vardef_item", "vardef", "constdef_item", 
                   "constdef", "typename", "argdef", "arglist", "stmlist", 
                   "stm", "simplestm", "stmline", "modulecall", "functioncall", 
                   "paramlist", "returnstm", "value", "expression", "add_sub", 
                   "term", "times_div", "factor", "rexp", "atom", "log_expression", 
                   "log_oper", "log_term", "log_rel", "assignment", "blockstm", 
                   "intvalue", "ifelse", "whilestm", "forstm" ]

    EOF = Token.EOF
    MODULE=1
    GLOBAL=2
    CONST=3
    EXTERN=4
    INT=5
    STRING=6
    VOID=7
    TRUE=8
    FALSE=9
    IF=10
    ELSE=11
    WHILE=12
    BREAK=13
    FOR=14
    RETURN=15
    EXECMODULE=16
    LPAR=17
    RPAR=18
    LCURL=19
    RCURL=20
    COMMA=21
    SEMICOLOM=22
    REFMARK=23
    ASSIGN=24
    PLUS=25
    MINUS=26
    TIMES=27
    SLASH=28
    MOD=29
    EXP=30
    NOT=31
    AND=32
    OR=33
    GT=34
    LT=35
    GE=36
    LE=37
    EQ=38
    NE=39
    INCOPER=40
    DECOPER=41
    BLOCK_COMMENT=42
    ID=43
    DIGIT=44
    STRVALUE=45
    SINGLELINE_COMMENT=46
    MULTILINE_COMMENT=47
    WS=48

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SourcefileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmlist(self):
            return self.getTypedRuleContext(SimplePOSParser.StmlistContext,0)


        def EOF(self):
            return self.getToken(SimplePOSParser.EOF, 0)

        def moduledef(self):
            return self.getTypedRuleContext(SimplePOSParser.ModuledefContext,0)


        def constblock(self):
            return self.getTypedRuleContext(SimplePOSParser.ConstblockContext,0)


        def vardefblock(self):
            return self.getTypedRuleContext(SimplePOSParser.VardefblockContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_sourcefile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourcefile" ):
                listener.enterSourcefile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourcefile" ):
                listener.exitSourcefile(self)




    def sourcefile(self):

        localctx = SimplePOSParser.SourcefileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourcefile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.MODULE:
                self.state = 76
                self.moduledef()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.CONST or _la==SimplePOSParser.EXTERN:
                self.state = 79
                self.constblock()


            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 82
                self.vardefblock()


            self.state = 85
            self.stmlist()
            self.state = 86
            self.match(SimplePOSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModuledefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self):
            return self.getToken(SimplePOSParser.MODULE, 0)

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def SEMICOLOM(self):
            return self.getToken(SimplePOSParser.SEMICOLOM, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def arglist(self):
            return self.getTypedRuleContext(SimplePOSParser.ArglistContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_moduledef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuledef" ):
                listener.enterModuledef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuledef" ):
                listener.exitModuledef(self)




    def moduledef(self):

        localctx = SimplePOSParser.ModuledefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_moduledef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(SimplePOSParser.MODULE)
            self.state = 89
            self.match(SimplePOSParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.LPAR:
                self.state = 90
                self.match(SimplePOSParser.LPAR)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SimplePOSParser.INT or _la==SimplePOSParser.STRING:
                    self.state = 91
                    self.arglist()


                self.state = 94
                self.match(SimplePOSParser.RPAR)


            self.state = 97
            self.match(SimplePOSParser.SEMICOLOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstblockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constdef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.ConstdefContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.ConstdefContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_constblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstblock" ):
                listener.enterConstblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstblock" ):
                listener.exitConstblock(self)




    def constblock(self):

        localctx = SimplePOSParser.ConstblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.constdef()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimplePOSParser.CONST or _la==SimplePOSParser.EXTERN):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardefblockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.VardefContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.VardefContext,i)


        def LCURL(self):
            return self.getToken(SimplePOSParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(SimplePOSParser.RCURL, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_vardefblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardefblock" ):
                listener.enterVardefblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardefblock" ):
                listener.exitVardefblock(self)




    def vardefblock(self):

        localctx = SimplePOSParser.VardefblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardefblock)
        self._la = 0 # Token type
        try:
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePOSParser.GLOBAL, SimplePOSParser.INT, SimplePOSParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 104
                        self.vardef()

                    else:
                        raise NoViableAltException(self)
                    self.state = 107 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            elif token in [SimplePOSParser.LCURL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(SimplePOSParser.LCURL)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 110
                    self.vardef()
                    self.state = 113 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.GLOBAL) | (1 << SimplePOSParser.INT) | (1 << SimplePOSParser.STRING))) != 0)):
                        break

                self.state = 115
                self.match(SimplePOSParser.RCURL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctiondefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def LCURL(self):
            return self.getToken(SimplePOSParser.LCURL, 0)

        def stmlist(self):
            return self.getTypedRuleContext(SimplePOSParser.StmlistContext,0)


        def RCURL(self):
            return self.getToken(SimplePOSParser.RCURL, 0)

        def typename(self):
            return self.getTypedRuleContext(SimplePOSParser.TypenameContext,0)


        def VOID(self):
            return self.getToken(SimplePOSParser.VOID, 0)

        def arglist(self):
            return self.getTypedRuleContext(SimplePOSParser.ArglistContext,0)


        def vardefblock(self):
            return self.getTypedRuleContext(SimplePOSParser.VardefblockContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_functiondef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctiondef" ):
                listener.enterFunctiondef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctiondef" ):
                listener.exitFunctiondef(self)




    def functiondef(self):

        localctx = SimplePOSParser.FunctiondefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functiondef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePOSParser.INT, SimplePOSParser.STRING]:
                self.state = 119
                self.typename()
                pass
            elif token in [SimplePOSParser.VOID]:
                self.state = 120
                self.match(SimplePOSParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
            self.match(SimplePOSParser.ID)
            self.state = 124
            self.match(SimplePOSParser.LPAR)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.INT or _la==SimplePOSParser.STRING:
                self.state = 125
                self.arglist()


            self.state = 128
            self.match(SimplePOSParser.RPAR)
            self.state = 129
            self.match(SimplePOSParser.LCURL)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 130
                self.vardefblock()


            self.state = 133
            self.stmlist()
            self.state = 134
            self.match(SimplePOSParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vardef_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SimplePOSParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(SimplePOSParser.ValueContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_vardef_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardef_item" ):
                listener.enterVardef_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardef_item" ):
                listener.exitVardef_item(self)




    def vardef_item(self):

        localctx = SimplePOSParser.Vardef_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardef_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(SimplePOSParser.ID)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.ASSIGN:
                self.state = 137
                self.match(SimplePOSParser.ASSIGN)
                self.state = 138
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(SimplePOSParser.TypenameContext,0)


        def vardef_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Vardef_itemContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Vardef_itemContext,i)


        def SEMICOLOM(self):
            return self.getToken(SimplePOSParser.SEMICOLOM, 0)

        def GLOBAL(self):
            return self.getToken(SimplePOSParser.GLOBAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.COMMA)
            else:
                return self.getToken(SimplePOSParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_vardef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardef" ):
                listener.enterVardef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardef" ):
                listener.exitVardef(self)




    def vardef(self):

        localctx = SimplePOSParser.VardefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.GLOBAL:
                self.state = 141
                self.match(SimplePOSParser.GLOBAL)


            self.state = 144
            self.typename()
            self.state = 145
            self.vardef_item()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.COMMA:
                self.state = 146
                self.match(SimplePOSParser.COMMA)
                self.state = 147
                self.vardef_item()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(SimplePOSParser.SEMICOLOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Constdef_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SimplePOSParser.ASSIGN, 0)

        def STRVALUE(self):
            return self.getToken(SimplePOSParser.STRVALUE, 0)

        def intvalue(self):
            return self.getTypedRuleContext(SimplePOSParser.IntvalueContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_constdef_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstdef_item" ):
                listener.enterConstdef_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstdef_item" ):
                listener.exitConstdef_item(self)




    def constdef_item(self):

        localctx = SimplePOSParser.Constdef_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constdef_item)
        try:
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(SimplePOSParser.ID)
                self.state = 156
                self.match(SimplePOSParser.ASSIGN)
                self.state = 157
                self.match(SimplePOSParser.STRVALUE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(SimplePOSParser.ID)
                self.state = 159
                self.match(SimplePOSParser.ASSIGN)
                self.state = 160
                self.intvalue()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstdefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(SimplePOSParser.CONST, 0)

        def constdef_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Constdef_itemContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Constdef_itemContext,i)


        def SEMICOLOM(self):
            return self.getToken(SimplePOSParser.SEMICOLOM, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.COMMA)
            else:
                return self.getToken(SimplePOSParser.COMMA, i)

        def EXTERN(self):
            return self.getToken(SimplePOSParser.EXTERN, 0)

        def typename(self):
            return self.getTypedRuleContext(SimplePOSParser.TypenameContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.ID)
            else:
                return self.getToken(SimplePOSParser.ID, i)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_constdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstdef" ):
                listener.enterConstdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstdef" ):
                listener.exitConstdef(self)




    def constdef(self):

        localctx = SimplePOSParser.ConstdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constdef)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePOSParser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(SimplePOSParser.CONST)
                self.state = 164
                self.constdef_item()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimplePOSParser.COMMA:
                    self.state = 165
                    self.match(SimplePOSParser.COMMA)
                    self.state = 166
                    self.constdef_item()
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 172
                self.match(SimplePOSParser.SEMICOLOM)
                pass
            elif token in [SimplePOSParser.EXTERN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.match(SimplePOSParser.EXTERN)
                self.state = 175
                self.match(SimplePOSParser.CONST)
                self.state = 176
                self.typename()
                self.state = 177
                self.match(SimplePOSParser.ID)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SimplePOSParser.COMMA:
                    self.state = 178
                    self.match(SimplePOSParser.COMMA)
                    self.state = 179
                    self.match(SimplePOSParser.ID)
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 185
                self.match(SimplePOSParser.SEMICOLOM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(SimplePOSParser.INT, 0)

        def STRING(self):
            return self.getToken(SimplePOSParser.STRING, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_typename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypename" ):
                listener.enterTypename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypename" ):
                listener.exitTypename(self)




    def typename(self):

        localctx = SimplePOSParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typename)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==SimplePOSParser.INT or _la==SimplePOSParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgdefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typename(self):
            return self.getTypedRuleContext(SimplePOSParser.TypenameContext,0)


        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def REFMARK(self):
            return self.getToken(SimplePOSParser.REFMARK, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_argdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgdef" ):
                listener.enterArgdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgdef" ):
                listener.exitArgdef(self)




    def argdef(self):

        localctx = SimplePOSParser.ArgdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.typename()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.REFMARK:
                self.state = 192
                self.match(SimplePOSParser.REFMARK)


            self.state = 195
            self.match(SimplePOSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArglistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argdef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.ArgdefContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.ArgdefContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.COMMA)
            else:
                return self.getToken(SimplePOSParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_arglist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArglist" ):
                listener.enterArglist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArglist" ):
                listener.exitArglist(self)




    def arglist(self):

        localctx = SimplePOSParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.argdef()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.COMMA:
                self.state = 198
                self.match(SimplePOSParser.COMMA)
                self.state = 199
                self.argdef()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.StmContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.StmContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_stmlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmlist" ):
                listener.enterStmlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmlist" ):
                listener.exitStmlist(self)




    def stmlist(self):

        localctx = SimplePOSParser.StmlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 205
                self.stm()
                self.state = 208 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.INT) | (1 << SimplePOSParser.STRING) | (1 << SimplePOSParser.VOID) | (1 << SimplePOSParser.IF) | (1 << SimplePOSParser.WHILE) | (1 << SimplePOSParser.BREAK) | (1 << SimplePOSParser.FOR) | (1 << SimplePOSParser.RETURN) | (1 << SimplePOSParser.EXECMODULE) | (1 << SimplePOSParser.LCURL) | (1 << SimplePOSParser.INCOPER) | (1 << SimplePOSParser.DECOPER) | (1 << SimplePOSParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simplestm(self):
            return self.getTypedRuleContext(SimplePOSParser.SimplestmContext,0)


        def blockstm(self):
            return self.getTypedRuleContext(SimplePOSParser.BlockstmContext,0)


        def ifelse(self):
            return self.getTypedRuleContext(SimplePOSParser.IfelseContext,0)


        def whilestm(self):
            return self.getTypedRuleContext(SimplePOSParser.WhilestmContext,0)


        def forstm(self):
            return self.getTypedRuleContext(SimplePOSParser.ForstmContext,0)


        def functiondef(self):
            return self.getTypedRuleContext(SimplePOSParser.FunctiondefContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_stm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStm" ):
                listener.enterStm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStm" ):
                listener.exitStm(self)




    def stm(self):

        localctx = SimplePOSParser.StmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stm)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePOSParser.BREAK, SimplePOSParser.RETURN, SimplePOSParser.EXECMODULE, SimplePOSParser.INCOPER, SimplePOSParser.DECOPER, SimplePOSParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.simplestm()
                pass
            elif token in [SimplePOSParser.LCURL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.blockstm()
                pass
            elif token in [SimplePOSParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.ifelse()
                pass
            elif token in [SimplePOSParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.whilestm()
                pass
            elif token in [SimplePOSParser.FOR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.forstm()
                pass
            elif token in [SimplePOSParser.INT, SimplePOSParser.STRING, SimplePOSParser.VOID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.functiondef()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimplestmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmline(self):
            return self.getTypedRuleContext(SimplePOSParser.StmlineContext,0)


        def SEMICOLOM(self):
            return self.getToken(SimplePOSParser.SEMICOLOM, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_simplestm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimplestm" ):
                listener.enterSimplestm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimplestm" ):
                listener.exitSimplestm(self)




    def simplestm(self):

        localctx = SimplePOSParser.SimplestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_simplestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.stmline()
            self.state = 219
            self.match(SimplePOSParser.SEMICOLOM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functioncall(self):
            return self.getTypedRuleContext(SimplePOSParser.FunctioncallContext,0)


        def modulecall(self):
            return self.getTypedRuleContext(SimplePOSParser.ModulecallContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimplePOSParser.AssignmentContext,0)


        def returnstm(self):
            return self.getTypedRuleContext(SimplePOSParser.ReturnstmContext,0)


        def BREAK(self):
            return self.getToken(SimplePOSParser.BREAK, 0)

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def INCOPER(self):
            return self.getToken(SimplePOSParser.INCOPER, 0)

        def DECOPER(self):
            return self.getToken(SimplePOSParser.DECOPER, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_stmline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmline" ):
                listener.enterStmline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmline" ):
                listener.exitStmline(self)




    def stmline(self):

        localctx = SimplePOSParser.StmlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmline)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.functioncall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.modulecall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.assignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 224
                self.returnstm()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.match(SimplePOSParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 226
                self.match(SimplePOSParser.ID)
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==SimplePOSParser.INCOPER or _la==SimplePOSParser.DECOPER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==SimplePOSParser.INCOPER or _la==SimplePOSParser.DECOPER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.match(SimplePOSParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModulecallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXECMODULE(self):
            return self.getToken(SimplePOSParser.EXECMODULE, 0)

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(SimplePOSParser.ParamlistContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_modulecall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModulecall" ):
                listener.enterModulecall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModulecall" ):
                listener.exitModulecall(self)




    def modulecall(self):

        localctx = SimplePOSParser.ModulecallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_modulecall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(SimplePOSParser.EXECMODULE)
            self.state = 233
            self.match(SimplePOSParser.ID)
            self.state = 234
            self.match(SimplePOSParser.LPAR)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.TRUE) | (1 << SimplePOSParser.FALSE) | (1 << SimplePOSParser.LPAR) | (1 << SimplePOSParser.MINUS) | (1 << SimplePOSParser.ID) | (1 << SimplePOSParser.DIGIT) | (1 << SimplePOSParser.STRVALUE))) != 0):
                self.state = 235
                self.paramlist()


            self.state = 238
            self.match(SimplePOSParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctioncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def paramlist(self):
            return self.getTypedRuleContext(SimplePOSParser.ParamlistContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)




    def functioncall(self):

        localctx = SimplePOSParser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(SimplePOSParser.ID)
            self.state = 241
            self.match(SimplePOSParser.LPAR)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.TRUE) | (1 << SimplePOSParser.FALSE) | (1 << SimplePOSParser.LPAR) | (1 << SimplePOSParser.MINUS) | (1 << SimplePOSParser.ID) | (1 << SimplePOSParser.DIGIT) | (1 << SimplePOSParser.STRVALUE))) != 0):
                self.state = 242
                self.paramlist()


            self.state = 245
            self.match(SimplePOSParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.ValueContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.COMMA)
            else:
                return self.getToken(SimplePOSParser.COMMA, i)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_paramlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamlist" ):
                listener.enterParamlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamlist" ):
                listener.exitParamlist(self)




    def paramlist(self):

        localctx = SimplePOSParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.value()
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.COMMA:
                self.state = 248
                self.match(SimplePOSParser.COMMA)
                self.state = 249
                self.value()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnstmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(SimplePOSParser.RETURN, 0)

        def value(self):
            return self.getTypedRuleContext(SimplePOSParser.ValueContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_returnstm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstm" ):
                listener.enterReturnstm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstm" ):
                listener.exitReturnstm(self)




    def returnstm(self):

        localctx = SimplePOSParser.ReturnstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(SimplePOSParser.RETURN)
            self.state = 256
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRVALUE(self):
            return self.getToken(SimplePOSParser.STRVALUE, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePOSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SimplePOSParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_value)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimplePOSParser.STRVALUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(SimplePOSParser.STRVALUE)
                pass
            elif token in [SimplePOSParser.TRUE, SimplePOSParser.FALSE, SimplePOSParser.LPAR, SimplePOSParser.MINUS, SimplePOSParser.ID, SimplePOSParser.DIGIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(SimplePOSParser.TermContext,0)


        def add_sub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Add_subContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Add_subContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SimplePOSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.term()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.PLUS or _la==SimplePOSParser.MINUS:
                self.state = 263
                self.add_sub()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Add_subContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(SimplePOSParser.TermContext,0)


        def PLUS(self):
            return self.getToken(SimplePOSParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SimplePOSParser.MINUS, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_add_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd_sub" ):
                listener.enterAdd_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd_sub" ):
                listener.exitAdd_sub(self)




    def add_sub(self):

        localctx = SimplePOSParser.Add_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_add_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            _la = self._input.LA(1)
            if not(_la==SimplePOSParser.PLUS or _la==SimplePOSParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 270
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(SimplePOSParser.FactorContext,0)


        def times_div(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Times_divContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Times_divContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = SimplePOSParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.factor()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.TIMES) | (1 << SimplePOSParser.SLASH) | (1 << SimplePOSParser.MOD))) != 0):
                self.state = 273
                self.times_div()
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Times_divContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(SimplePOSParser.FactorContext,0)


        def TIMES(self):
            return self.getToken(SimplePOSParser.TIMES, 0)

        def SLASH(self):
            return self.getToken(SimplePOSParser.SLASH, 0)

        def MOD(self):
            return self.getToken(SimplePOSParser.MOD, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_times_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimes_div" ):
                listener.enterTimes_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimes_div" ):
                listener.exitTimes_div(self)




    def times_div(self):

        localctx = SimplePOSParser.Times_divContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_times_div)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.TIMES) | (1 << SimplePOSParser.SLASH) | (1 << SimplePOSParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 280
            self.factor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(SimplePOSParser.AtomContext,0)


        def rexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.RexpContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.RexpContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = SimplePOSParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.atom()
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.EXP:
                self.state = 283
                self.rexp()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXP(self):
            return self.getToken(SimplePOSParser.EXP, 0)

        def atom(self):
            return self.getTypedRuleContext(SimplePOSParser.AtomContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_rexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRexp" ):
                listener.enterRexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRexp" ):
                listener.exitRexp(self)




    def rexp(self):

        localctx = SimplePOSParser.RexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_rexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(SimplePOSParser.EXP)
            self.state = 290
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def intvalue(self):
            return self.getTypedRuleContext(SimplePOSParser.IntvalueContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(SimplePOSParser.FunctioncallContext,0)


        def TRUE(self):
            return self.getToken(SimplePOSParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SimplePOSParser.FALSE, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def expression(self):
            return self.getTypedRuleContext(SimplePOSParser.ExpressionContext,0)


        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def log_expression(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_expressionContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = SimplePOSParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_atom)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(SimplePOSParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.intvalue()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.functioncall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 295
                self.match(SimplePOSParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 296
                self.match(SimplePOSParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 297
                self.match(SimplePOSParser.LPAR)
                self.state = 298
                self.expression()
                self.state = 299
                self.match(SimplePOSParser.RPAR)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 301
                self.match(SimplePOSParser.LPAR)
                self.state = 302
                self.log_expression()
                self.state = 303
                self.match(SimplePOSParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Log_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_term(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_termContext,0)


        def NOT(self):
            return self.getToken(SimplePOSParser.NOT, 0)

        def log_oper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Log_operContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Log_operContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_log_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_expression" ):
                listener.enterLog_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_expression" ):
                listener.exitLog_expression(self)




    def log_expression(self):

        localctx = SimplePOSParser.Log_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_log_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.NOT:
                self.state = 307
                self.match(SimplePOSParser.NOT)


            self.state = 310
            self.log_term()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SimplePOSParser.AND or _la==SimplePOSParser.OR:
                self.state = 311
                self.log_oper()
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Log_operContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def log_term(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_termContext,0)


        def AND(self):
            return self.getToken(SimplePOSParser.AND, 0)

        def OR(self):
            return self.getToken(SimplePOSParser.OR, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_log_oper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_oper" ):
                listener.enterLog_oper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_oper" ):
                listener.exitLog_oper(self)




    def log_oper(self):

        localctx = SimplePOSParser.Log_operContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_log_oper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            _la = self._input.LA(1)
            if not(_la==SimplePOSParser.AND or _la==SimplePOSParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 318
            self.log_term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Log_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(SimplePOSParser.ValueContext,0)


        def log_rel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.Log_relContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.Log_relContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_log_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_term" ):
                listener.enterLog_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_term" ):
                listener.exitLog_term(self)




    def log_term(self):

        localctx = SimplePOSParser.Log_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_log_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.value()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.GT) | (1 << SimplePOSParser.LT) | (1 << SimplePOSParser.GE) | (1 << SimplePOSParser.LE) | (1 << SimplePOSParser.EQ) | (1 << SimplePOSParser.NE))) != 0):
                self.state = 321
                self.log_rel()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Log_relContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(SimplePOSParser.ValueContext,0)


        def GT(self):
            return self.getToken(SimplePOSParser.GT, 0)

        def LT(self):
            return self.getToken(SimplePOSParser.LT, 0)

        def GE(self):
            return self.getToken(SimplePOSParser.GE, 0)

        def LE(self):
            return self.getToken(SimplePOSParser.LE, 0)

        def EQ(self):
            return self.getToken(SimplePOSParser.EQ, 0)

        def NE(self):
            return self.getToken(SimplePOSParser.NE, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_log_rel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog_rel" ):
                listener.enterLog_rel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog_rel" ):
                listener.exitLog_rel(self)




    def log_rel(self):

        localctx = SimplePOSParser.Log_relContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_log_rel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.GT) | (1 << SimplePOSParser.LT) | (1 << SimplePOSParser.GE) | (1 << SimplePOSParser.LE) | (1 << SimplePOSParser.EQ) | (1 << SimplePOSParser.NE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 328
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimplePOSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(SimplePOSParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(SimplePOSParser.ValueContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SimplePOSParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(SimplePOSParser.ID)
            self.state = 331
            self.match(SimplePOSParser.ASSIGN)
            self.state = 332
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockstmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURL(self):
            return self.getToken(SimplePOSParser.LCURL, 0)

        def RCURL(self):
            return self.getToken(SimplePOSParser.RCURL, 0)

        def vardefblock(self):
            return self.getTypedRuleContext(SimplePOSParser.VardefblockContext,0)


        def stm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.StmContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.StmContext,i)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_blockstm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockstm" ):
                listener.enterBlockstm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockstm" ):
                listener.exitBlockstm(self)




    def blockstm(self):

        localctx = SimplePOSParser.BlockstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_blockstm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(SimplePOSParser.LCURL)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 335
                self.vardefblock()


            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimplePOSParser.INT) | (1 << SimplePOSParser.STRING) | (1 << SimplePOSParser.VOID) | (1 << SimplePOSParser.IF) | (1 << SimplePOSParser.WHILE) | (1 << SimplePOSParser.BREAK) | (1 << SimplePOSParser.FOR) | (1 << SimplePOSParser.RETURN) | (1 << SimplePOSParser.EXECMODULE) | (1 << SimplePOSParser.LCURL) | (1 << SimplePOSParser.INCOPER) | (1 << SimplePOSParser.DECOPER) | (1 << SimplePOSParser.ID))) != 0):
                self.state = 338
                self.stm()
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 344
            self.match(SimplePOSParser.RCURL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(SimplePOSParser.MINUS, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.DIGIT)
            else:
                return self.getToken(SimplePOSParser.DIGIT, i)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_intvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntvalue" ):
                listener.enterIntvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntvalue" ):
                listener.exitIntvalue(self)




    def intvalue(self):

        localctx = SimplePOSParser.IntvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_intvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.MINUS:
                self.state = 346
                self.match(SimplePOSParser.MINUS)


            self.state = 350 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 349
                self.match(SimplePOSParser.DIGIT)
                self.state = 352 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SimplePOSParser.DIGIT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfelseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(SimplePOSParser.IF, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def log_expression(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_expressionContext,0)


        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def blockstm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.BlockstmContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.BlockstmContext,i)


        def ELSE(self):
            return self.getToken(SimplePOSParser.ELSE, 0)

        def getRuleIndex(self):
            return SimplePOSParser.RULE_ifelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)




    def ifelse(self):

        localctx = SimplePOSParser.IfelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifelse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(SimplePOSParser.IF)
            self.state = 355
            self.match(SimplePOSParser.LPAR)
            self.state = 356
            self.log_expression()
            self.state = 357
            self.match(SimplePOSParser.RPAR)
            self.state = 358
            self.blockstm()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SimplePOSParser.ELSE:
                self.state = 359
                self.match(SimplePOSParser.ELSE)
                self.state = 360
                self.blockstm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhilestmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(SimplePOSParser.WHILE, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def log_expression(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_expressionContext,0)


        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def blockstm(self):
            return self.getTypedRuleContext(SimplePOSParser.BlockstmContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_whilestm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhilestm" ):
                listener.enterWhilestm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhilestm" ):
                listener.exitWhilestm(self)




    def whilestm(self):

        localctx = SimplePOSParser.WhilestmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_whilestm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(SimplePOSParser.WHILE)
            self.state = 364
            self.match(SimplePOSParser.LPAR)
            self.state = 365
            self.log_expression()
            self.state = 366
            self.match(SimplePOSParser.RPAR)
            self.state = 367
            self.blockstm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForstmContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(SimplePOSParser.FOR, 0)

        def LPAR(self):
            return self.getToken(SimplePOSParser.LPAR, 0)

        def stmline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimplePOSParser.StmlineContext)
            else:
                return self.getTypedRuleContext(SimplePOSParser.StmlineContext,i)


        def SEMICOLOM(self, i:int=None):
            if i is None:
                return self.getTokens(SimplePOSParser.SEMICOLOM)
            else:
                return self.getToken(SimplePOSParser.SEMICOLOM, i)

        def log_expression(self):
            return self.getTypedRuleContext(SimplePOSParser.Log_expressionContext,0)


        def RPAR(self):
            return self.getToken(SimplePOSParser.RPAR, 0)

        def blockstm(self):
            return self.getTypedRuleContext(SimplePOSParser.BlockstmContext,0)


        def getRuleIndex(self):
            return SimplePOSParser.RULE_forstm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForstm" ):
                listener.enterForstm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForstm" ):
                listener.exitForstm(self)




    def forstm(self):

        localctx = SimplePOSParser.ForstmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_forstm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(SimplePOSParser.FOR)
            self.state = 370
            self.match(SimplePOSParser.LPAR)
            self.state = 371
            self.stmline()
            self.state = 372
            self.match(SimplePOSParser.SEMICOLOM)
            self.state = 373
            self.log_expression()
            self.state = 374
            self.match(SimplePOSParser.SEMICOLOM)
            self.state = 375
            self.stmline()
            self.state = 376
            self.match(SimplePOSParser.RPAR)
            self.state = 377
            self.blockstm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





