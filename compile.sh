#!/usr/bin/env bash 

latex mcm.tex
bibtex mcm
latex mcm.tex
latex mcm.tex
dvipdf mcm.dvi mcm.pdf
