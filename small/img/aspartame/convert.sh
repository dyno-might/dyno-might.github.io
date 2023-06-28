#!/bin/bash

for f in *.pdf;
do
    e="$(basename $f .pdf)"
    echo "$e"
    pdf2svg $e.pdf $e.svg
done
