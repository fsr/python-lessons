---
title: Get me the file! - file(handle(r)s)
status: reviewed
# number: 6
authors: [justus, felixw]
lesson: 3
---

### Step 1

Open a (new) file for writing using `file = open(name)`.

Write the string `"hello"` to the file.

Don't forget to close the handle.

Check the result.

### Step 2

Get some _lorem ipsum_ paragraphs (you can use [this](http://www.loremipsum.de) page) and add them to the file (by hand).

Open the file in python using `with` and write the contents to the console.

### Step 3

Open the file, read the lines, write them back in reverse.

Since opening a file using `open(filename, 'w')` clears the file, you will often have to do this when you want to modify the contents of a file without overwriting everything.

### Step 4

Often, you just want to add some content to a file, e.g. when you are logging the activitiy of your program.

Therefore, you can use `open(filename, 'a')`. This opens the file in _append_ mode, which leaves the previous contents of the file untouched and simply appends your new content to the file.

Try now to append some text to the lorem ipsum file.

Decide on your own wether you want to use the _context manager_ or manually open/close the file handle.

### Step 5

Write the script so that it accepts a filepath as input[^args].

[^args]:
    Command line arguments can be read from `sys.argv`. Note that `sys.argv[0]` is always the name of the script.

Read `stdin`, half the lines and write the content into the file at the filepath we took as input.

Call the script with some input (unix pipeline is very useful). For example `less lorem.txt | python3 script.py 'output.txt'` with lorem.txt being the file containing test text.
