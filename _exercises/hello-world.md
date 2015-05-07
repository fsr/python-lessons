---
title: Hello World
number: 1
---

### Step 1

#### Edit
Write a python script that will print the String `'Hello World!'` to the command line when run using the `print()` function.

#### Run
Run the script `python3 script.py`. What happens?

### Step 2

#### Edit
Now put the `print()` statement inside a function.

#### Run
Run the script again. What changed?

Run the script interactively using `python3 -i script.py` and once the interpreter has started call your function.

### Step 3

#### Edit
Call the function at the top level of the script.

#### Run
Run the whole thing again.

Open the interpreter `python3` in the same directory where your script resides and import (see below) the script. What happened?

{% highlight python %}
import your_script_name_here  # notice no '.py' at the end
{% endhighlight %}

### Step 4

#### Edit
Add the main script boilerplate code:

{% highlight python %}
if __name__ == '__main__':
    your_function()
{% endhighlight %}

And call your function inside the `if` block.

#### Run
Run it again.

Open the interpreter again and import the script again. What changed?
