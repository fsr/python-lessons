#!/bin/bash

ALL=`ls md/slides/*.md`

for path in $ALL
do
  file=${path##*/}

  pandoc -t revealjs -s --template md/template.html $path --no-highlight -o html/${file%.md}.html
done
