LATEXMK ?= latexmk

.PHONY: all clean

all: doc/reference.pdf

doc/reference.pdf: doc/reference.tex
	cd doc && $(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error reference.tex

clean:
	cd doc && $(LATEXMK) -C reference.tex
