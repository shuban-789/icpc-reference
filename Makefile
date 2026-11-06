LATEXMK ?= latexmk
PYTHON ?= python3

.PHONY: all generate check check-kactl clean cpp

all: generate
	mkdir -p build/latex
	cd doc && $(LATEXMK) -pdf -outdir=../build/latex -interaction=nonstopmode -halt-on-error reference.tex
	cd doc && $(LATEXMK) -pdf -outdir=../build/latex -interaction=nonstopmode -halt-on-error topics.tex
	$(PYTHON) scripts/check_pdf.py
	cp build/latex/reference.pdf doc/reference.pdf
	cp build/latex/topics.pdf doc/topics.pdf

generate:
	$(PYTHON) scripts/render_reference.py

doc/reference.pdf doc/topics.pdf: all

check: generate
	$(PYTHON) scripts/check_snippets.py

check-kactl: generate
	$(PYTHON) scripts/check_kactl.py

cpp:
	mkdir -p build
	$(CXX) -std=c++17 -O2 -Wall -Wextra cpp/template.cpp -o build/sol

clean:
	cd doc && $(LATEXMK) -outdir=../build/latex -c reference.tex
	cd doc && $(LATEXMK) -outdir=../build/latex -c topics.tex
