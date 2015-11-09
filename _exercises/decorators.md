---
title: It is beautiful - Decorator
status: finished
# number: 12
authors: felix
lesson: 3
---

### Step 1

__Edit__

Write a script. Import the time module.[^time]
Then write a decorator called `time_teller` this should be our decorator. `time_teller` contains another function that set three Strings into "It is {date}. Since {hour} hours and {minutes} minutes.".

[^time]:
    Use `import time`

Write a second function `get_time` that return a list with string values of the date and the time split into hours and minutes.[^usetime]

Use the decorator on `get_time` and print this function

[^usetime]:
    You can get formatted time using e.g. `time.strftime("%Y/%m/%d")` for the date for hours and minutes use `%H` and `%M`

__Run__

Run your script.

### Step 2

__Edit__

Change your decorator that it is accepting arguments. Change the String as well to "Now it is {date}"

Change `get_time` to accept a sting as input (default should be `"%Y/%m/%d %H:%M"`)[^default] and return the date formatted like this.

[^default]:
    You can define default values if there is no argument given (e.g.: `def my_func(value="Take this String if there is none")`

Add some more prints with custom date formats as you like.[^dateformats]

__Run__

Run your script and test if the values are correct.

[^dateformats]:
    A table of the formats could be found in the [Documentation](https://docs.python.org/3.4/library/time.html#module-time){:target="_blank"}
