---
title: Because builtin is not enough - Inheritance
status: drafty
number: 7
author: justus
---

### Inheriting form dict

Create a class inheriting from `dict`.

In python 2 you'll have to inherit from `collections.UserDict`, in python 3  you can simply inherit from `dict` directly.

Make sure it functions as expected.

### Lowercase keys

Overload the internal method such that the dict only accepts lowercase keys of type `str`[^only_str], and otherwise throws (raises) an exception[^raise].

[^only_str]:
    Overload `__getitem__` and `__setitem__` and check for type `str`, like so: `if not isinstance(value, str): raise ...`

[^raise]:
    `raise KeyError(message)`

### Defaults

Overload the internals such that if an index (of type `str`) is requested, that is not present in the dict, it returns a default value which can optionally be set in the initializer[^default], otherwise it is `None`.

[^default]:
    Example:

        def __init__(self, default, iterable):
            self.default = default
            super().__init__(iterable)


### Non changeable (frozendict)

Create a new class frozendict, which accepts an iterable of tuples in the initializer and fills the dict with the values within.

Overload as many methods you can find[^altering] that can change the contents of the `dict` such that if someone attempts to use them to change the dict, an error is thrown.

[^altering]:
    The ones I can think of are `__setitem__`, `update`, `pop` and `setdefault`
