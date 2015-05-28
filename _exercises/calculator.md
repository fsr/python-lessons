---
title: Calculator
status: drafty
---

### Description

Write a command line program, that accepts dual-operand infix-only mathematical equations and calculates the result. In an endless loop.[^while]

[^while]:
    A `while` loop would be appropriate here.

You may assume the user input has the structure operand 1, space, operator, space, operand 2 like so `1 + 5` or `6 - 8`.[^input_structure]

[^input_structure]:
    Since we assume operands and operator are separated by spaces, we can split the string at the spaces.

It should at least accept +, -, \*, / as operators.

### Example:

    Enter your equation:
    2 - 4  
    -2

