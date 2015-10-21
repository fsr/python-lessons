---
title: Objects and classes
number: 4
status: reviewed
authors: justus
lesson: 2
---

__Fire up the interpreter!__

*Hint: The names in this example are just (very poor) suggestions. You can use your own, more creative, names, if you can think of any.*

The steps 7 and 8 are a little bit more advanced. Inheritance will be introduced in a future lesson, so you might want to come back and do this two tasks later.

### Step 1

Create an empty[^empty] class[^class] (name irrelevant, but let's call it "A").

[^class]:
    Classes are created using the keyword `class`.

[^empty]:
    Empty things are created with the `pass` keyword as the last statement inside the block.

Create an instance[^instance], let's call it "a".

[^instance]:
    Instances are created by simply calling the class name like a function which yields an instance that can be captured in a variable, aka `a = A()`.

Attach some attributes.[^attach_attr]

[^attach_attr]:
    Attributes can be attached using dot notation `.` and the usual equal sign `=` for setting variables on the instance (e.g. `a.first_attr = True`)

A string `'id#456'` called `id_string`.

A number `456` called `id_value`.

Access these attributes and make sure they have the correct value.[^access_attr]

[^access_attr]:
    You can access attributes of classes using the same dot notation like attaching them (e.g. `a.first_attr`)

### Step 2

Create another instance of class "A" called "b".

Try to access the attributes `id_value` and `id_string`. What happens? [^err]

[^err]:
  The interpreter will throw an error, since these two attributes are only defined for the instance 'a'. This problem results from instance attributes being defined outside the *Initializer*.

### Step 3

Create another **non-empty** class called "B" with a method[^methods] called "my_method" that simply returns the number 42.

[^methods]:
    Methods are declared like regular functions using `def name(params):`. However they have to be inside the class (indented) and the first parameter will be the class instance, usually called "self".

        class SomeClass:
            def method(self, other_params):
                # self is an object instance
                stuff
                return something

Try it with an instance of the class.

Try it using the alternative call method.[^alt_call]

[^alt_call]:
    `Class.method(instance, other_params)`

### Step 4

Create a new class "C" and implement the initializer[^initializer] such that it accepts some arguments and sets them as attributes.[^attr_init]

Create some instances, check the attributes work as intended.

[^attr_init]:
    Attributes in the initializer are set like any other `self.attr = value`.

[^initializer]:
    The initializer is a special method called `__init__`. This method also needs to have a first parameter called `self`.

### Step 5

Add a class attribute to "C". Verify the instances you just created all have that same attribute.

Modify it from one of the instances. Now check the value from another instance. Does it change there? [^no]

[^no]:
  No. I doesn't change there.

### Step 6

Create a class "D". Implement the initalizer to accept an integer and store it in an attribute `value`. Also implement a method called `plus` which returns the stored integer plus three.

Try the method on some instances.[^anon_class]

[^anon_class]:
    You can use the instance directly, without saving it. `Class(params).method()`

Try the alternative call.[^alt_call]

### *Step 7*

Create a class inheriting from "D", called "DChild"[^super] that accepts another integer and stores it. Overload the `plus` method to return the sum of the two integers.

[^super]:
    You'll need to call the parent class constructor using `super().__init__(params)`.


### *Step 8*

Play around with inheritance.[^super2]

[^super2]:
    Also play around with `super` it's useful.
