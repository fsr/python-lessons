#!/bin/bash
source_url=https://github.com/hakimel/reveal.js.git

mkdir html

git clone $source_url html/reveal.js
cp src/ifsr.css html/reveal.js/css/theme/ifsr.css
cp src/ifsr.css.map html/reveal.js/css/theme/ifsr.css.map
cp -r src/css html/css
cp -r src/js html/js
