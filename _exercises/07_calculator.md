---
title: Calculator
status: reviewed
number: 7
authors: [justus, felix]
lesson: 3
---

### Step 1

Write a command line program, that accepts dual-operand infix-only mathematical equations and calculates the results, in an endless loop.[^while]

[^while]:
    A `while` loop would be appropriate here.

You may assume the user input has the structure: operand 1, space, operator, space, operand 2 like so `1 + 5` or `6 - 8`.[^input_structure]

[^input_structure]:
    Since we assume operands and operator are separated by spaces, we can split the string at the spaces. `input.split(' ')`

It should at least accept +, -, \*, / as operators.[^strategy] [^ifelse] [^exception]

[^strategy]:
    Remember to cast the operands to an int or even better float, once you have split it.

[^ifelse]:
    Also remember, that you can pack multiple if/else commands:

    ```python
    if condition1:
        # commands
    elif condition2:
        # commands
    #there is no limit to the number of elifs
    else:
        # normal case
    ```

[^exception]:
    Do not forget to catch the `ZeroDivisionError` Exception!

**Example:**

{% highlight sh %}
Enter your equation:
2 - 4  
-2
{% endhighlight %}

### Step 2

Log[^a] your calculations and their results in a textfile.  
Use the following format: `1 + 5 = 6` [^newline]

[^a]:
    You can log it using **append** mode: `open(filename, 'a')`

[^newline]:
    Do not forget to add a newline at the end of every line,
