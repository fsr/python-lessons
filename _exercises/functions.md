---
title: Functions as values
status: drafty
authors: justus
---

## Regular

Create a function that takes two numbers as arguments and multiplies them, returning the result.

## Assignment

Rename the function.[^renaming] Verify it works as intended.

[^renaming]:
    Declare a new variable, assign the function to it and then delete the old identifier

## Curried

Create another funciton, which also takes two numbers as input but returns a function, that takes no arguments, which when called returns the product of the two numbers.

{% highlight python %}
>>> result = my_func(2, 3)
>>> result()
6
{% endhighlight %}

If you got that working, modify the inner function such that it takes a string, and when called returns the string capitalized and concatenated with the product of the two numbers from the outer function.

{% highlight python %}
>>> result = my_func(2, 3)
>>> result('some string ')
some string 6
{% endhighlight %}

## Lambda

Now first try to rewrite it such that in the inner function immediately returns, that is the line with the `return` statement directly follows the line with the `def` function definition. (One single statement inside the function)

Like so:

{% highlight python %}
def func():
    return "..."
{% endhighlight %}

Now replace it with a lambda expression.[^lambda]

[^lambda]:
    `lambda param_a, param_b: expression`
