---
title: Even more objects!
status: drafty
author: felixw
number: 5
---

### Let's go deeper into objects

Write a small database for your personal contacts. Each contact should be represented by a single object that can hold information about *name*, *date of birth*, *phone number* and *mail address*. Store your contacts in an appropriate data structure. [^which]

[^which]:
    You might want to use a `dict` or a `list`.

Wouldn't it be great if you could simply print your contacts by just calling `print()` with the identifier of the contact object? Add a `__str__` method in your class to make this possible.
