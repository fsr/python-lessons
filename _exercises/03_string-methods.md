---
title: String Methods
number: 3
status: reviewed
authors: justus
lesson: 1
---

*Remember: String formatting can be very useful when creating strings for printing to the console*

### Step 1

Using the documentation on [this page](https://docs.python.org/3/library/stdtypes.html#string-methods) write a script, that takes user input (see exercise 2).
And checks whether it is (either)[^case]:

1. uppercase
2. numeric
3. contains the substring `":-)"`[^substring] or
4. none of the above

report which of these it was. If multiple branches are true, you need only report one.

[^substring]:
	The using `in` checks for subelements and substrings as well.


[^case]:
	python does not have a case statement


### Step 2

Expand the 'uppercase' branch, to not only report that it was uppercase, but also print a lowercase version. [^docpage]

[^docpage]:
	[Python String Documentation Page](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Step 3

Expand the 'numeric' branch to request a second number from the user and then reporting the sum of the two numbers. [^typecasting]

[^typecasting]:
	Typecasting is done by calling the constructor of the target type on the source value*

### Step 4

Expand the 'none of the above' branch to split the string at every letter 'a' [^string_splitting] and join these strings together into a new string, inserting semicolons between them. [^string_join]

`'aglloatyat' -> ['', 'gllo', 'ty', 't'] -> ';gllo;ty;t'`

[^string_splitting]:
	Strings can be split with the `split(separator)` method. This method also accepts a second parameter (int) how often it should split the string at maximum.

[^string_join]:
	Strings are joined with the `separator_string.join(['list', 'of', 'strings'])` method.
