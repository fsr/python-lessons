# Python Lessons

This repository contains the __Python Lesson__ sources for the free student courses, held at the TU Dresden.

Exercises to go along with the courses can be found [on GitHub pages](http://fsr.github.io/python-lessons/) or on the `gh-pages` branch of this repository as Markdown sources.

## Compiling the markdown sources

The slides in the `md` folder need to be compiled with **reveal.js**.

Therefore, `pandoc` has to be installed on your computer. You can find these Instructions [here](http://pandoc.org/installing.html). Mac users can simply install it with *homebrew*:
`brew install pandoc`

Run `./install.sh` to initialize the html folder with reveal.js and copy the ifsr.css this only have to be done once

To build the slides simply run `./build_reveal.py`. The compiled html files are in the `html` folder.

If you add new slides don't forget to add them to `reveal.json`


## Instructions for teachers and contributors

If you want to contribute to these lessons, you should note that every topic exists as `.tex` file and as `.md` file because the tex files - rendered as PDF - offer a much more convenient way to look up something after a lesson while the rendered `reveal.js` slides are way better for presenting the slides in class.
The black background and the few lines per slide improve readability and help to focus on the subject. Plus they look much better :wink:

So if you are thinking about making some content-related changes, it would be nice if you apply those changes to both, the `md` and the `tex` slides.

For contributing to the tasks, have a look at the `gh-pages` branch of this repository.

### Teaching

As stated above, you should rely on the rendered Markdown slides for presenting. The `tex` files are automatically rendered and can be found at:  
[http://fsr.github.io/python-lessons/materials.html](http://fsr.github.io/python-lessons/materials.html)

Almost every task is linked to a lesson. The corresponding PDF is linked automatically at the beginning of every task.

Solutions for all tasks on this page can be found at [this repository](https://github.com/Feliix42/python-solutions).


These lessons are created and maintained by [@h4llow3En](https://github.com/h4llow3En), [@justusadam](https://github.com/justusadam) and [@feliix42](https://github.com/Feliix42).
