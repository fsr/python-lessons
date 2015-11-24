---
title: Functions as Values
status: finished
authors: [justus, felixw]
number: 14
lesson: 7
---

### Regular

Create a function that takes two numbers as arguments and multiplies them, returning the result.

### Assignment

Rename the function.[^renaming] Verify it works as intended.

[^renaming]:
    Declare a new variable, assign the function to it and then call just the 'new' function.

### More Advanced

Create a function, which takes a variable amount of integer numbers and returns the sum of all given numbers.

(Re)write your `main()` function so that it calls your new function with all arguments you call your script with.[^sysargv]
Since these arguments are interpreted as strings you will need to cast all arguments first.[^cast] A comprehension might come in handy for this!

[^sysargv]:
    The arguments your script is called with are stored in `sys.argv` (remember to import _sys_!).
    The first entry in this list is __always__ the name of the script, so you should remove this entry somehow before moving on in the script.

[^cast]:
    You can cast a string to _int_ using `int()`

{% highlight sh %}
$ python3 my_script.py 5 12 7 18
42
{% endhighlight %}

Now you should expect that you have some users who like to troll you and give something else than numbers as input.
When you try to cast a string that contains no numbers to int, Python will raise a `ValueError`.
Catch[^catch] that, print your own error message and end your script.

[^catch]:
    Catch a exception by surrounding the possible exception source with __try/except__:

        try:
            bad_command()
        except ExceptionName:
            # Handling


### Lambda

Let's go for writing a _Lambda_ function. We'll do it step by step.

First, try to rewrite your script so that the 'calculator' function contains only one line of code (the line with the `return` statement) and all the work is done inside the `return` statement, like so:

{% highlight python %}
def func():
    return "..."
{% endhighlight %}

Now replace the whole inner function with a lambda expression.[^lambda]

[^lambda]:
    `lambda param_a, param_b: expression`
