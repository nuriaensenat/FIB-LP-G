ANTLR_CMD=antlr4 -Dlanguage=Python3 -no-listener -visitor
GRAMMAR=g.g4
INDIR=jocs_proves
OUTDIR=outputs

.PHONY: all antlr outputs tests clean

all: outputs antlr tests

outputs:
	mkdir -p $(OUTDIR)

antlr: $(GRAMMAR)
	$(ANTLR_CMD) $(GRAMMAR)

tests: composicio_funcions operacions_adverbs operacions_basiques_verbs operacions_flip_fold operacions_operadors variables_i_funcions

composicio_funcions: outputs antlr
	python3 g.py $(INDIR)/composicio_funcions.j > $(OUTDIR)/composicio_funcions.out

operacions_adverbs: outputs antlr
	python3 g.py $(INDIR)/operacions_adverbs.j > $(OUTDIR)/operacions_adverbs.out

operacions_basiques_verbs: outputs antlr
	python3 g.py $(INDIR)/operacions_basiques_verbs.j > $(OUTDIR)/operacions_basiques_verbs.out

operacions_flip_fold: outputs antlr
	python3 g.py $(INDIR)/operacions_flip_fold.j > $(OUTDIR)/operacions_flip_fold.out

operacions_operadors: outputs antlr
	python3 g.py $(INDIR)/operacions_operadors.j > $(OUTDIR)/operacions_operadors.out

variables_i_funcions: outputs antlr
	python3 g.py $(INDIR)/variables_i_funcions.j > $(OUTDIR)/variables_i_funcions.out

clean:
	rm -f g.interp gParser.py g.tokens gVisitor.py gLexer.py gLexer.tokens gLexer.interp
	rm -rf $(OUTDIR)