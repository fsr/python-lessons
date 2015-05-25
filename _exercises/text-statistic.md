---
title: Text Statistics
---

Download [this](//) file.

Read the file[^file_reading] and make a statistic of how often every word appears in the file and print that to the command line.

[^file_reading]:
    Use a context manager `with` and the function `open(filename, mode="r")` like so 
    {% highlight python %}
    with open('path/to/file', mode='r') as file:
        contents = file.read()
    # now it implicitly calls file.close()
    contents.do_something()
    {% endhighlight %}


### Tips

You can/should use a dictionary containing every word and then scan the text incrementing individual counters[^counter]

[^counter]:
    There's a dedicated data structure for that in the python standard library, in the `collections` module called `Counter`.
