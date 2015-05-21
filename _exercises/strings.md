---
title: Strings
number: 2
---

We want to explore string concatenation and formatting.

*Hint: Test after every step whether the code is working as intended*

### Step 1

A very useful function for the beginning is `input()` which reads a line from the command line, that can then be saved to a variable like so `var = input()`.

Write a script that reads an input string from the command line and then prints a message `"Hello "` with the input string appended. Make sure it works.

### Step 2

Modify the script so it asks for the name using input, `input("message")`, and then greet the person `"Hello NAME, welcome to python"` using string formatting with the `format` method.

### Step 3

Now ask for first and last name separately and this time greet by using named fields `"{firstname}"`. Remember, that for named fields `format` has to be called with keyword arguments `format(varname=value)`.

### Step 3

Mix both by asking some input and then printing a formatted string with at least two named and two unnamed fields.
