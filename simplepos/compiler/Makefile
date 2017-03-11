#
# Construir o fonte a partir das gramáticas
#
ANTLR=antlr4
ANTLR_OPT=-Dlanguage=Python3

.PHONY: clean

SimplePOSLexer.py: SimplePOS.g4
	$(ANTLR) $(ANTLR_OPT) $^

clean:
	-rm SimplePOS*.{py,tokens}
	-rm *~
	-rm *.pyc
