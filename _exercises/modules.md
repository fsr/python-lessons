---
title: Modules and Packages
status: reviewed
# number: 10
authors: felix
lesson: 4
---

### Step 1

Write a module `basicmath.py` with functions to add, subtract, multiply and divide two values.

Write a script that uses this module [^import] and call some functions of this module.

[^import]:
    You can import this using `import`

Run this script.

### Step 2

Write a second module `stringopts.py` and group this and the first one in a Package.[^package]
`stringopts` should include functions that are called `get_length`, `reverse`[^reverse] and `does_include`

[^package]:
    Do not forget to add a `__init__.py`

[^reverse]:
    To reverse Strings you could use `myString[::-1]` or `reversed(myString)`

Edit your script and use functions of both.

Run and test your script.
