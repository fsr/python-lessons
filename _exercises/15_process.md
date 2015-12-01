---
title: Hand off the work - subprocess
status: finished
authors: felix
number: 15
lesson: 8
---

### Step 1

You don't know on which OS this script will run eventually. So you should first determine if you are running on an UNIX System or on Windows.[^platform]  
Save the result in an efficient way in a variable[^bool]

### Step 2

List all existing files in your current directory using the subprocess.[^os]<sup>,</sup>[^subprocess]

__Run your script.__

### Step 3

Since your terminal got a bit messy from the output of the last `subprocess` command it is time to clear the screen after five seconds.[^time]<sup>,</sup>[^clear]


[^platform]:
    To do this you should have a look at the [`platform` module](https://docs.python.org/3.5/library/platform.html) and its [`system()` method](https://docs.python.org/3.5/library/platform.html#platform.system).

[^bool]:
    A `Bool`-Value would be more efficient than the returned String.

[^os]:
    Here you have to decide which command you have to call `ls -lha` for UNIX `dir` for Windows.

[^subprocess]:
    Remember you have do pass a list with every argument in a single string, if there are whitespaces in your command.
    Use `subprocess.run()` here.

[^time]:
    To wait a certain amount of time use `time.wait(in_seconds)` from the `time` module.

[^clear]:
    Here again: UNIX command is `clear`, Windows command is `cls`.
