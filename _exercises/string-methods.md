---
title: String Methods
number: 3
---

*Remember: String formatting can be very useful for when creating strings for printing to the console*

### Step 1

Using the documentation on [this page](https://docs.python.org/3/library/stdtypes.html#string-methods) write a script, that takes user input (see exercise 2).
And checks whether it is (either):

- a) uppercase
- b) numeric
- c) contains the substring `":-)"`
- d) none of the above

report which of these it was.

Notes and hints[^branches] [^case] [^typechecking]

[^branches]: 
	If multiple branches are true, you need only report one

[^case]: 
	python does not have a case statement

[^typechecking]:
	types can be checked with either `your_type == type(variable)` or `isinstance`

### Step 2

Expand the 'uppercase' branch, to not only report that it was uppercase, but also print a lowercase version.

### Step 3

Expand the 'numeric' branch to request a second number from the user and then reporting the sum of the two numbers.

*Hint: Typecasting is done by calling the constructor of the target type on the source value*

### Step 4

Expand the 'none of the above' branch to split the string at every letter 'a' and join these strings together into a new string, inserting semicolons between them.

`'aglloatyat' -> ['', 'gllo', 'ty', 't'] -> ';gllo;ty;t'`
