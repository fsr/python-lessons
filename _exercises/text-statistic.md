---
title: Text Statistics
status: finished
number: 8
authors: justus
---


Write some [lorem ipsum text](http://www.loremipsum.de) into a file.

Read the file[^filereading] and make a statistic of how often every word appears in the file[^dict] and print that to the command line.

Print the results to the command line.

Parameterize the function and make the main function peek into `sys.argv` and use all arguments to the script as input file names, combining the results[^tuple].


[^dict]:
    You can/should use a `dict` containing every word as a key and as the value a counter then scan the text incrementing the respective counters[^counter]

[^filereading]:
    When opening files you can easily just iterate over the lines in the file by iterating over the filehandler object itself.

[^tuple]:
    You can easily return multiple things by using `return value1, value2, value3` and so on, which returns a tuple `(value1, value2, value3)`
