---
title: Get me the file! - file(handle(r)s)
status: drafty
---

## Step 1

Open a (new) file for writing using `file = open(name)`.

Write the string `"hello"` to the file.

Don't forget to close the handle.

Check the result.

## Step 2

Get some lorem ipsum paragraphs and and them to the file (by hand).

Open the file in python using `with` and write the contents to the console.

## Step 3

Open the file, shorten every line to have it's size and write it to stderr[^stderr].

[^stderr]:
    `stderr` in python can be imported from `sys` and is a normal filehandler.

## Step 4

Open the file, read the lines, write them back in reverse.

## Step 5

Write the script so that it accepts a filepath as input[^args].

[^args]:
    Command line arguments can be read from `sys.argv`. Note that `sys.argv[0]` is always the name of the script.
    
Read `stdin`, half the lines and write the content into the file at the filepath we took as input.

Call the script with some input (unix pipeline is very useful). For example `lorem.txt | python3 script.py 'output.txt'`
