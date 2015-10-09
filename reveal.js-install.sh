source_url=https://codeload.github.com/hakimel/reveal.js/tar.gz/3.1.0

mkdir rbuild

curl "$source_url" -o reveal.js.tar.gz
tar -xf reveal.js.tar.gz
mv reveal.js-3.1.0 rbuild/reveal.js
rm reveal.js.tar.gz
