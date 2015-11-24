---
title: Functions as values
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
    Declare a new variable, assign the function to it and then delete the old identifier

### More Advanced

Create another function, which also takes two numbers as input. Instead of returning the result, it should return a function. This function should then return the product of the two numbers.

{% highlight python %}
>>> result = my_func(2, 3)
>>> result()
6
{% endhighlight %}

If you got that working, modify the inner function such that it takes a string, and when called returns the string capitalized[^docs] and concatenated with the product of the two numbers from the outer function.

[^docs]:
    You might wanna take a look at the [string docs](https://docs.python.org/3/library/string.html) or [string method docs](https://docs.python.org/3/library/stdtypes.html?highlight=capitalize#string-methods)? ;)

{% highlight python %}
>>> result = my_func(2, 3)
>>> result('some string ')
Some string 6
{% endhighlight %}

### Lambda

Let's go for writing a _Lambda_ function. We'll do it step by step.

First, try to rewrite your script so that the inner function contains only one line of code (the line with the `return` statement) and all the work is done inside the `return` statement, like so:

{% highlight python %}
def func():
    return "..."
{% endhighlight %}

Now replace the whole inner function with a lambda expression.[^lambda]

[^lambda]:
    `lambda param_a, param_b: expression`
