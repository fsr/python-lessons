---
theme: black
title: Advanced function (signatures)
---

## Advanced functions

## Functions as Values

Functions can be assigned like normal values.

```python
def function(params):
    return 4

my_var = function

my_var(2)  # ==> 4
```

---

Or passed as parameters.

```python
def callif(boolean, callback):
    if boolean:
        callback()

callif(True, lambda : print("hello world"))
```

## Methods are functions

```python
class MyClass(object):
    def function(self, param):
        return 4


my_var = MyClass.function

my_var(MyClass(), 2)  # ==> 4
```

## Default Parameters

Functions may define default values for their parameters.
Parameters with no default value are also often called positional parameters.
Parameters with default arguments are often called named arguments (we will see why later).

```python
def greet(name, greeting='Hello'):
    return '{} {}'.format(greeting, name)

greet('Herbert')  # ==> 'Hallo Herbert'
greet('Herbert', 'Gruess Gott')  # ==> 'Gruess Gott Herbert'
```

---

### Don't

Ever, EVER, even though the language allows it, make a mutable value the default value of a function. Mutable Values include `list`, `dict`, `set` and your own classes (more precisely their attributes).

Immutable values would be `string`, `function` (sort of), `int`, `type`and `None`.

```python
def func(param1, param2=[]):
    print(param2)
    param2.append(param1)
```

---

One would expect this function to always print the empty list `[]`. However the default param is not recalculated. So what actually happens is this.

```python
func(1)  # ==> []
func(2)  # ==> [1]
func('j') # ==> [1,2]
```

Bugs like these are truly hard to find.

---

### Do

If you actually want a mutable value as default, you simply make the default `None` and reassign.

```python
def func(param1, param2=None):
    param2 = [] if param2 is None else param2
    pass
```

That is the save way.


## Call by name

Function parameters may be provided by their names.
When calling functions by name the order in which the arguments are provided does not matter.

```python
def land(house, tree, pond):
    return 'You own land with a {} a {} and a {}'.format(house, tree, pond)

land('green house', 'maple', 'fish pond')
# or called by name
land(house='green house', pond='fish pond', tree='maple')
# or mixed
land('green house', pond='fish pond', tree='maple')
# but THIS does not work
land('maple', house='green house', tree='maple')
```

---

The rule is:

- You may call as many parameters position as they wish.
- You may call any parameter by name.
- If a parameter is being called by name, any parameter following it has to be called by name as well.


## Aggregate Parameters

---

### Positional

Every function may have one aggregate parameter. This must be the last positional parameter.
The aggregate parameter is denoted by the operator `*` (pronounced 'star').
Only named arguments may follow an aggregate parameter.
If an aggregate exists, arguments following it may only be called by name (obviously).

---

```python
def function(param1, *aggr, param2=0):
    pass
function(1,2,3,4)  # correct, aggr = (2,3,4)
function(1,2,4,5,6,78,9,90,0)  
# also correct, aggr = (2,4,5,6,78,9,90,0)
function()  # incorrect param1 requires at least one argument
function(1, param2=7)  # correct, aggr = ()
function(param2=8)  # incorrect, param1 needs a value
function(param2=0, param1=6)  # correct
```

The type of an aggregate is **always** `tuple`.

---

```python
def f(*args):
    print(type(args)) # ==> tuple
```

As you can see a function can have only an aggregate as a parameter.
If no argument is passed to the aggregate `len(args) == 0`, if one is passed `len(args) == 1` etc.
If the aggregate is the only parameter it is often named `args` (short for 'arguments').

---

The aggregaor operator `*` may also occur without a name (python3), in which case it'll simply force any subsequent (named) parameters have to be called by name, and cannot be called positionally.

```python
def function(param1, param2, *, param3=6):
    pass
```

---

### Named

Analog to the positional aggregate there's an aggregate for named values also. It is denoted using the `**` operator (pronounced 'star star', aka `**kwargs` is pronounced 'key duouble u args star star').
The named aggregator only aggregates named arguments and is of type `dict`.

```python
def function(param1, **aggr):
    pass

function(1)  # correct, aggr = {}
function(1, some=9)  # correct, aggr = {'some':9}
function(some=6)  # incorrect, param1 requires a value
function(some=0, param1=8, param2=4)  
# correct, aggr = {'some':0, 'param2':4}
```

If a function has no named arguments besides the aggregator, it is often named `kwargs` (keyword args).

---

### Mixing

Both aggregators can be used simultaneously in one function.
The rule is, that each aggregator can only occur once.

```python
def function(
        param1,
        param2,
        *args,
        kwparam1=0,
        kwparam2=None,
        **kwargs
    ):
    pass
```

---

This leads to the following generalized function signature.

```pyhton
def name(
        [params, ...]
        [, *[aggregator]]
        [, kwparams=kwvalue, ...]
        [**kwaggreg]
    ):
    pass
```

*Note that the square brackets mean optional*
