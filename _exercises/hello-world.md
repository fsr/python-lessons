---
title: Hello World
number: 1
---

### Step 1

#### Run
Start the interpreter using `python3` and try to print `'Hello World'` using the `print()` function.

### Step 2

#### Edit
Write a python script containing the same function.

#### Run
Run the script `python3 script.py`. What happens?

### Step 3

#### Edit
Now put the `print()` statement inside a function.

#### Run
Run the script again. What changed?

Run the script interactively using `python3 -i script.py` and once the interpreter has started call your function.

### Step 4

#### Edit
Call the function at the top level of the script.

#### Run
Run the whole thing again.

Open the interpreter `python3` in the same directory where your script resides and import (see below) the script. What happened?

{% highlight python %}
import your_script_name_here  # notice no '.py' at the end
{% endhighlight %}

### Step 5

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
