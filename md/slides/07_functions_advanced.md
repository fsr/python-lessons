---
title: Funktionen (fortgeschritten)
---

# Nutzung von Funktionen


## Funktionen als Werte

---

Funktionen können wie alle
anderen Werte zugewiesen werden

```python
def function(params):
    return 4

my_var = function
my_var(2)  # ==> 4
```

---

Oder als Parameter mitgegeben werden

```python
def callif(boolean, callback):
    if boolean:
        callback()

callif(True, lambda: print("hello world"))
```

---

## Methoden sind Funktionen

```python
class MyClass(object):
    def function(self, param):
        return 4

my_var = MyClass.function
my_var(MyClass(), 2)  # ==> 4
```


## Default Parameter

---


-   Funktionen können vordefinierte Werte für Parameter haben.

-   Parameter ohne `default`-Werten werden positionale Argumente genannt

-   Parameter mit `default`-Werten werden name

---

```python
def greet(name, greeting='Hello'):
    return '{} {}'.format(greeting, name)

greet('Herbert')
# ==> 'Hallo Herbert'

greet('Herbert', 'Gruess Gott')
# ==> 'Gruess Gott Herbert'
```

---

## ACHTUNG!

---

__Niemals `mutable Values` (änderbare Werte) als `default`-Parameter verwenden!__

---

__mutable Values:__

`list`, `dict`, `set` und eigene Klassen (bzw. deren Attribute)

__immutable Values:__

`string`, `function`, `int`, `type` und `None`

---

__Warum?__

```python
def func(param1, param2=[]):
    print(param2)
    param2.append(param1)
```

---

Man denkt, die Funktion hat jedes mal eine leere
List, jedoch passiert folgendes:

```python
func(1)  # ==> []
func(2)  # ==> [1]
func('j')  # ==> [1,2]
```

Die Liste wird einmalig zum Start angelegt und fortgeführt.

---

So sollte man es machen:

```python
def func(param1, param2=None):
    param2 = [] if param2 is None else param2
    pass
```

Den `default`-Parameter als `None` setzten und dann, falls er `None` ist
als z.B. leere Liste setzen.

---

## Aufruf mit Namen

---

Funktionsparameter können
direkt mit ihrem Namen aufgerufen werden, dann spielt die
Aufrufreihenfolge keine Rolle mehr.

---

```python
def land(house, tree, pond):
    return 'You own land with a {} \
a {} and a {}'.format(house, tree, pond)

land('green house', 'maple', 'fish pond')

# oder mit Aufruf durch Namen:
land(house='green house', pond='fish pond', tree='maple')

# or vermischt
land('green house', pond='fish pond', tree='maple')

# folgendes funktioniert NICHT!
land('maple', house='green house', tree='maple'
```

---

__Es gelten folgende Regeln:__
-   Alle Parameter können an ihrer Position angesprochen werden
-   Es können auch alle mit ihrem Namen angesprochen werden
-   Wenn eins mit dem Namen angesprochen wurde, müssen die folgenden
    ebenfalls mit Namen angesprochen werden


# Aggregatoren

---

**Aggregatoren** (auch Sammler genannt), sind
sehr nützlich, wenn man, zusätzlich zu bereits definierten Parametern,
in einer Funktion eine unbestimmte Anzahl an Funktionsargumenten
entgegen nehmen will.

## Positionale Aggregatoren

---

-   jede Funktion kann einen Aggregator haben
-   dieser muss der *letzte* positionale Parameter sein
-   Positionale Aggregatoren werden durch einen `*` gekennzeichnet
-   nach einem Aggregator können nur noch benamte Parameter definiert
    werden, diese müssen auch mit Namen aufgerufen werden\

---

Der Inhalt des Aggregators wird in einem *Tupel* gespeichert:

```python
def f(*args):
    print(type(args))  # ==> tuple
```

---

### Beispiel

```python
def function(param1, *aggr, param2=0):
    pass

function(1, 2, 3, 4)    # korrekt, aggr = (2,3,4)
function(1, 2, 4, 5, 6, 78, 9, 90, 0)
# auch korrekt, aggr = (2,4,5,6,78,9,90,0)
function()    # inkorrekt, param1 braucht mindestens ein Argument
function(1, param2=7)    # korrekt, aggr = ()
function(param2=8)    # inkorrekt, param1 braucht einen Wert
function(param2=0, param1=6)    # korrekt
```

---

-   Eine Funktion kann auch nur einen Aggregator als Parameter
    entgegennehmen (keine anderen Parameter)
-   Ohne Argumente ergibt sich `len(args)` zu 0
-   Werden keine anderen Parameter erwartet, nennt man den Aggregator
    meist `args` (kurz für *Arguments*)\

---

In **Python 3** kann man Aggregatoren auch ohne Namen definieren:
```python
def function(param1, param2, *, param3=6):
    pass
```
Auf diesen Aggregator kann nicht zugegriffen werden. Er erzwingt lediglich,
dass alle folgenden Parameter mit Namen aufgerufen werden.

## Benannte Aggregatoren

---

Analog zu Parametern gibt es auch benannte Aggregatoren. Diese werden mit `**` vor dem
Parameternamen definiert. Diese Aggregatoren akzeptieren lediglich
benannte Parameter und sind vom Typ `dict`.

---

### Beispiel

```python
def function(param1, **aggr):
    pass


function(1)    # korrekt, aggr = {}
function(1, some=9)    # korrekt, agar = {'some': 9}
function(some=6)    # inkorrekt, param1 braucht einen Wert
function(some=0, param1=8, param2=4)
# korrekt, agar = {'some': 0, 'param2': 4}
```

Wenn eine Funktion keine anderen Parameter erwartet, nennt man den
Aggregator meist `**kwargs` (kurz für *Keyword Arguments*)


## Benannte und Positionale Aggregatoren

---

Beide Aggregatoren können gleichzeitig in einer Funktion verwendet werden.  
Die Regel dabei ist: Von jeder Sorte nur *ein* Aggregator.

---

### Beispiel

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

### Generelle Funktionsstruktur

Wenn beide Aggregatoren zum Einsatz kommen sollen, ergibt sich folgende Funktionsstruktur:


```python
def name(
        [params, ...]
        [, *[aggregator]]
        [, kwparams=kwvalue, ...]
        [**kwaggreg]
        ):
    pass
```
 *Eckige Klammern stehen für optionale Parameter/Namen.*
