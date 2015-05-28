---
title: Your own unix, with blackjack and ... python
status: drafty
---

We want to recreate (parts of) `cp`, `mv`, `cd` and `ls` in python.


### `cd`

This is probably the easiest one.

Create a python file `cd.py`.

This file should be executable[^executable]. 

[^executable]:
    Permissions have to be set appropriately and the line `#! /usr/bin/env python3` has to appear at the top of the file.
    
It will take one input (verify that not more than one have been given) and change the current working directory to that location, if it is valid and exists, otherwise print an error message and terminate.


### `cp`

Create a file `cp.py` and make it executable.

It will take two inputs, source (one file) and target (one folder) and it will create a copy of the file in the target directory.

You'll have to verify that the source is a file and the target a directory.
    
Try by executing it `./filename.py`.


### `mv`

Create a file `mv.py` and make it executable.

It also takes two inputs, but here both have to be valid filenames. If the second (target) file exists you have to warn the user that he'll be overwriting it and wait for a yes/no input.

Also in this case the file has to be moved instead of copied.


### `ls`

Create a file `ls.py` and make it executable.

#### Step 1

Take a path as an input.

If it is a file, print only the filename and terminate.

If it is a directory, print all files contained in a vertical list and terminate, like so:

```
file.json
document.docx
folder/
website.html
```

#### Step 2

Only print files not starting with '.'[^filter].

[^filter]:
    A good option would be 
    
    ```
    filter(lambda a: not a.startswith('.'), files)
    ```
    
    or, if you'd want to be very fancy you could use the equivalent 
    
    ```
    itertools.filterfalse(
        functools.partial(str.startswith, prefix='.')
        , files
    )
    ```
    
    which makes use of the more functional features of `itertools` and `functools`.
    

#### Step 3

Parse the command line arguments using `argparse`.

If the `-a` switch is provided also print files starting with '.'.

#### Step 4

If the switch `-r` is provided, recursively print contents of all subdirectories, **after** printing the contents of the directory itself, with each files paths relative to the original input directory.

#### Step 5

If the `-l` switch is provided print not only the filenames but some extra information. This could be filesize, owner, group, permissions etc. Whatever you can find. (Remember that string formatting can be very useful for creating good looking output).