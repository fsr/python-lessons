---
title: Because builtin is not enough - Inheritance
status: drafty
---

### Inheriting form dict

Create a class inheriting from `dict`.

Make sure it functions as expected.

### Lowercase keys

Overload the internal method such that the dict only accepts lowercase keys of type str, and otherwise throws an exception.

### Defaults

Overload the internals such that if an index is requested, that is not present in the dict, it returns a default value which can optionally be set in the initializer, otherwise it is `None`.
