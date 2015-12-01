---
title: Your own grep - using subprocess
status: drafty
authors: felix
number: 16
lesson: 8
---

### Step 1

Use the script from the previous exercise and modify it.

Assign the return value of the `subprocess.run()` to an variable an print it after clearing the terminal.

What do you get? Does it return the expected Value?

### Step 2

Determine how you could fetch the output which is now printed to `stdout` and store it in a variable.[^getoutput]  
The original `ls` command has one new item every newline so you can store them easily in an list.[^split]

Grep shows you every element which contains the passed string. So you should create a input and parse it as a Regex.

Now print every element that got a match-Object if you use `re.match()` on it.

[^getoutput]:
    You should use `subprocess.getoutput()` instead.

[^split]:
    Use `split('\n')` on the saved output.
