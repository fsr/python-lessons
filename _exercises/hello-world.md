---
title: Hello World
number: 1
status: reviewed
authors: justus
---

### Step 1

__Run__  
Start the interpreter using `python3` and print `'Hello World'` using the `print()` function.

### Step 2

__Edit__  
Write a python script containing the same function.

__Run__  
Run the script `python3 script.py`. What happens?

### Step 3

__Edit__  
Now put the `print()` statement inside a function.

__Run__  
Run the script again. What changed?

Run the script interactively using `python3 -i script.py` and once the interpreter has started call your function.

### Step 4

__Edit__  
In the script, call the function at the top level.

__Run__  
Run the whole thing again.

Open the interpreter `python3` in the same directory where your script resides and import (see below) the script. What happened?

{% highlight python %}
import your_script_name_here  # notice no '.py' at the end
{% endhighlight %}

### Step 5

__Edit__  
Add the main script boilerplate code:

{% highlight python %}
if __name__ == '__main__':
    your_function()
{% endhighlight %}

And call your function inside the `if` block.

__Run__  
Run it again.

Open the interpreter again and import the script again. What changed?
