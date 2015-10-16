---
title: Even more objects! - deeper into classes
status: reviewed
authors: [felixw, felix]
#number: 5
lesson: 2
---

### Step 1

Write a small database for your personal contacts.

Each contact should be represented by a single object[^class] that can hold information about __name__, __date of birth__, __phone number__ and __mail address__.[^init]

Store your contacts in an appropriate data structure. [^which]

[^class]:
    You could write a class `Contact()` to instantiate objects from it.

[^init]:
    Hand over this information to the `__init__` function and store them in instance variables.

[^which]:
    You might want to use a `dict` or a `list`.

### Step 2

Wouldn't it be great if you could simply print your contacts by just calling `print()` with the identifier of the contact object?

Add a `__str__` method[^self] in your class to make it possible.

[^self]:
    Don't forget the `self` argument...


### Step 3

Imagine one of your contacts get a new mailadress.

Add functions to your class that make you able to change the mail address or phone number of a contact *(for practising purposes one function is enough)*.[^simple]

[^simple]:
    Keep it simple! Call the function from an object with e.g. `identifier.changeMail("xy@z.com")` and replace the address stored in the instance.

### Step 4

Now splice your mail/phone number changer function with some I/O.  

Use **string formatting** to ask the user for the new information while displaying the old.[^formatting]

[^formatting]:
    You need the `str.format()` function here. You can nest it inside of an `input()` function.
