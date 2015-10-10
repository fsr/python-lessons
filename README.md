# Python Lessons

Python lesson sources for TU Dresden free student courses.

Exercises to go along with the courses can be found [on GitHub pages](http://fsr.github.io/python-lessons/) or on the `gh-pages` branch of this repository as Markdown sources.

## Compiling the markdown sources

The slides in the `md` folder need to be compiled with **reveal.js**. 

Therefore, `pandoc` has to be installed on your computer. Mac users can simply install it with *homebrew*:
`brew install pandoc`


Make the install script and the build script executable, using `chmod +x filename.sh`, then install reveal.js once by running `./reveal.js-install.sh`.

After the installation you can compile the Markdown files by running the build script. The compiled html files are in the `rbuild` folder.
