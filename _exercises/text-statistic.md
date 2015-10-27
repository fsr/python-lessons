---
title: Text Statistics
status: reviewed
number: 8
authors: [justus, felix]
lesson: 3
---

### Step 1
Write some [lorem ipsum text](http://www.loremipsum.de) into a file.

Read the file[^filereading] and make a statistic of how often every word appears in the file[^dict] and print your results to the command line.

### Step 2
Now parameterize the function.[^parameterize]

Make the main function peek into `sys.argv`[^sys] and use all arguments to the script as input file names[^first], combining the results[^tuple].

[^parameterize]:
    Let the function take parameters as an input.

[^sys]:
    You have to use `import sys` to have access to `sys.argv`.

[^first]:
    The first argument of `sys.argv` is always the script itself.

[^dict]:
    You can/should use a `dict` containing every word as a key and as the value a counter then scan the text incrementing the respective counters[^counter]

[^filereading]:
    When opening files you can easily just iterate over the lines in the file by iterating over the filehandler object itself.

[^tuple]:
    You can easily return multiple things by using `return value1, value2, value3` and so on, which returns a tuple `(value1, value2, value3)`
