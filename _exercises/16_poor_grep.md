---
title: Your own grep - using subprocess
status: finished
authors: [felix, felixw]
number: 16
lesson: 8
---

### Step 1

Use the script from the previous exercise and modify it.

Assign the return value of the `subprocess.run()` to an variable an print it after clearing the terminal.

What do you get? Does it return the expected value?

### Step 2

Determine how you could fetch the output which is now printed to `stdout` and store it in a variable.[^getoutput]  
The original `ls` (or `dir`) command has one new item every newline so you can store them easily in an list.[^split]

Grep shows you every element which contains the passed string. Since we don't know (yet) how to work with regular expressions,
we will implement a more rudimentary version of grep which only displays exact name matches. Go through your list of items and
print every item that contains the _exact_ search string. [^how]

[^getoutput]:
    You should use `subprocess.getoutput()` instead.

[^split]:
    Use `split()` on the saved output and split it at every newline character (`\n`).

[^how]:
    Best way is to iterate over the items and see if your search string is `in` your item... ;)


### Step 3

To be more flexible, your script should take a path for the directory and a string to search for as input.
The script should then run the command in the given directory[^dir] and search for your string.

[^dir]:
    Do you remember the `cwd` argument?

### Step 4

Make sure that you won't get trolled by any user and make sure, that the given directory is existing.[^osisdir]

If not, you should print an error message and quit the script.

[^osisdir]:
    You can use `os.path.isdir()` to check that. Also see the [docs](https://docs.python.org/3.5/library/os.path.html) for how this command works.
