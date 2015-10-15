---
title: Important importing - path path path
status: finished
# number: 10
authors: justus
---

## Step 1

Write two python files `foo.py` and `bar.py`. The `foo` module will contain the main function, the `bar` module will contain a function that takes two numbers and adds them, then divides the result by the first one, and a variable called `MY_CONST` with the value `[4, 2]`.

In `foo` import `bar`. In the `foo.main` function print the constant from `bar` and a value calculated by the function in `bar`.

Run it.

## Step 2

Change the directory and call the `foo.py` script from within another directory. What happens?

## Step 3

There are three ways of fixing this problem, of which we learned two[^path]. Try using both once.

[^path]:
    `PYTHONPATH` and `sys.path`
