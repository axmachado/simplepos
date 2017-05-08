/* -*- antlr -*- */
grammar SimplePOS;

options {
    language = Python3;
}

@header {# -*- coding: utf-8 -*-
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
}

sourcefile
    : moduledef? constblock? vardefblock? stmlist EOF
    ;
moduledef
    : MODULE ID (LPAR arglist? RPAR)? SEMICOLOM
    ;
constblock
    : constdef+
    ;
vardefblock
    : vardef+
    | LCURL vardef+ RCURL
    ;
functiondef
    : (typename | VOID) ID LPAR arglist? RPAR LCURL vardefblock? stmlist RCURL
    ;
vardef_item
    : ID (ASSIGN value)?
    ;
vardef
    : GLOBAL? typename vardef_item (COMMA vardef_item)* SEMICOLOM
    ;
constdef_item
    : ID ASSIGN STRVALUE
    | ID ASSIGN intvalue
    ;
constdef
    : CONST constdef_item (COMMA constdef_item)* SEMICOLOM
    | EXTERN CONST typename ID (COMMA ID)* SEMICOLOM
    ;
typename
    : INT
    | STRING
    ;
argdef
    : typename REFMARK? ID
    ;
arglist
    : argdef (COMMA argdef)*
    ;
stmlist
    : stm+
    ;
stm
    : simplestm
    | blockstm
    | ifelse
    | whilestm
    | forstm
    | functiondef
    ;
simplestm
    : stmline SEMICOLOM
    ;
stmline
    : functioncall
    | modulecall
    | assignment
    | returnstm
    | BREAK
    | ID (INCOPER|DECOPER)
    | (INCOPER|DECOPER) ID
    ;
modulecall
    : EXECMODULE ID LPAR paramlist? RPAR
    ;
functioncall
    : ID LPAR paramlist? RPAR
    ;
paramlist
    : value (COMMA value)*
    ;
returnstm
    : RETURN value
    ;
value
    : STRVALUE
    | expression
    ;
expression
    : term add_sub*
    ;
add_sub
    : (PLUS | MINUS) term
    ;
term
    : factor times_div*
    ;
times_div
    : (TIMES | SLASH | MOD) factor
    ;
factor
    : atom rexp*
    ;
rexp
    : EXP atom
    ;
atom
    : ID
    | intvalue
    | functioncall
    | TRUE
    | FALSE
    | LPAR expression RPAR
    | LPAR log_expression RPAR
    ;
log_expression
    : NOT? log_term log_oper*
    ;
log_oper
    : (AND | OR) log_term
    ;
log_term
    : value log_rel*
    ;
log_rel
    : (GT | LT | GE | LE | EQ | NE) value
    ;
assignment
    : ID ASSIGN  value
    ;
blockstm
    : LCURL vardefblock? stm* RCURL
    ;
intvalue
    : MINUS? DIGIT+
    ;
ifelse
    : IF LPAR log_expression RPAR blockstm (ELSE blockstm)?
    ;
whilestm
    : WHILE LPAR log_expression RPAR blockstm
    ;
forstm
    : FOR LPAR stmline SEMICOLOM log_expression SEMICOLOM stmline RPAR blockstm
    ;

// Token definitions:

/* keywords */
MODULE: 'module';
GLOBAL: 'global';
CONST: 'const';
EXTERN: 'extern';
INT: 'int';
STRING: 'string';
VOID: 'void';
TRUE: 'true';
FALSE: 'false';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
BREAK: 'break';
FOR: 'for';
RETURN: 'return';
EXECMODULE: 'callmodule';
/* punctuation */
LPAR: '(';
RPAR: ')';
LCURL: '{';
RCURL: '}';
COMMA: ',';
SEMICOLOM: ';';
/* operators */
REFMARK: '&';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
TIMES: '*';
SLASH: '/';
MOD: '%';
EXP: '^';
NOT: '!';
AND: '&&';
OR: '||';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';
INCOPER: '++';
DECOPER: '--';
/* constructs */
BLOCK_COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
DIGIT: [0-9]+ ;
STRVALUE
    : '"' (~[\r\n"])*? '"'
    | '\'' (~[\r\n"])*? '\''
    ;
SINGLELINE_COMMENT: '//' (~[\r\n]*) [\r\n] -> skip;
MULTILINE_COMMENT: '/*' (.*?) '*/' -> skip;
WS : [ \t\r\n]+ -> skip ;
