---
title: Calculator
status: finished
number: 6
author: justus
---

### Description

Write a command line program, that accepts dual-operand infix-only mathematical equations and calculates the results, in an endless loop.[^while]

[^while]:
    A `while` loop would be appropriate here.

You may assume the user input has the structure: operand 1, space, operator, space, operand 2 like so `1 + 5` or `6 - 8`.[^input_structure]

[^input_structure]:
    Since we assume operands and operator are separated by spaces, we can split the string at the spaces. `input.split(' ')`

It should at least accept +, -, \*, / as operators.[^strategy]

[^strategy]:
    Remember to cast the operands to an int or even better float, once you have split it.

### Example:

    Enter your equation:
    2 - 4  
    -2
