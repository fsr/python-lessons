# Exception Handling

---

-   Alle Exceptions erben von `Exception`
-   Catching mit try/except
-   `finally` um Code auszuführen, der *unbedingt* laufen muss, egal ob
    eine Exception vorliegt oder nicht

---

```python
class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return '{} mit nachricht {}'.format(self.__class__,
                                            self.message)
```

---

```python
try:
    # code
    raise KeyError('message')
# mit nur einer exception
# except MyException as error:
except (KeyError, MyException) as error:
    print(error)
    pass
finally:
    # was unbedingt zu tun ist

```

# Boolsche Werte

---

-   *type* ist `bool`
-   Mögliche Werte: `True` oder `False`
-   Operationen sind *und*, *oder*, *nicht* (`and, or, not`)


# list

---

-   enthält variable Anzahl von Objekten
-   eine Liste kann beliebig viele verschiedene Datentypen
    enthalten (z.B. `bool` und `list`)
-   Auch Listen können in Listen gespeichert werden!
-   Listenobjekte haben eine feste Reihenfolge (*first in, last out*)
-   optimiert für einseitige Benutzung wie z.B. Queue (`append` und
    `pop`)

---

```python
l = [1, 9, 'string', object]

isinstance(l[0], int)  # ==> True
l[1] == 9  # ==> True
len(l)  # ==> 4

9 in l  # ==> True

l.pop()  # ==> object
len(l)  # ==> 3
l.append([])  # ==> None

l  # ==> [1, 9, 'string', []]
len(l)  # ==> 4
```

# tuple

---

-   Gruppiert Daten
-   kann nicht mehr verändert werden, sobald es erstellt wurde
-   Funktionen mit mehreren Rückgabewerten geben ein Tupel zurück

---

```python
# Tupel mit 3 Elementen
t = (1, 3, 'ein string')
isinstance(t, tuple) # ==> True

t[0] == 1  # ==> True
t[1] == 3  # ==> True
t[2] == 'ein string'  # ==> True
t[4] == 'ein string'  # ==> IndexError: tuple index out of range
t[2] = 'ein anderer string'  # ==> TypeError: 'tuple' object
                             # does not support item assignment

# oder auch ohne klammern
t = 1, 3, 'ein string'
# macht es (manchmal) besser lesbar, z.b. bei
return 1, 2, 5
```

# dict

---

-   einfache HashMap
-   ungeordnet
-   jeder hashbare Typ kann ein Key sein
-   jedem Key ist dann ein Value zugeordnet

---

```python
d = { 'm': 4, 3: 'val2', object: 'auch typen koennen keys sein' }

d[3]  # ==> "val2"
d['q']  # ==> KeyError: 'q'
d.get('q')  # ==> None
d.get('q', 5)  # ==> 5

d[0] = 7
d  # ==> {3: 'val2', 'm': 4, 'q': 5,
   #      <class 'object'>: 'auch typen koennen schluessel sein'}
```

---

```python
d.setdefault('m')  # ==> 4
d.setdefault('q', 5)  # ==> 5
d  # ==> { 'm': 4, 3: 'val2',
   #      object: 'auch typen koennen keys sein',
   #      0:7, 'q': 5 }
len(d)  # ==> 5
d.keys()  # ==> dict_keys([3, 0, 'm', 'q', <class 'object'>])
d.values()  # ==> dict_values(['val2', 7, 4, 5,
            #                  'auch typen koennen keys sein'])
d.items()  # ==> dict_items([(3, 'val2'), (0, 7), ('m', 4),
           #                 ('q', 5), (<class 'object'>,
           #                           'auch typen koennen ...')])

'm' in d  # ==> True
object in d  # ==> True
tuple in d  # ==> False
```

# set/frozenset

---

-   kann nur hashbare Einträge enthalten
-   `set` selbst ist nicht hashbar
-   `frozensets` sind hashbar, jedoch nicht mehr veränderbar
-   enthält jedes Element nur einmal

---

-   schnellere Überprüfung mit `in` (prüft, ob Element enthalten ist)
-   Mögliche Operationen: `superset()`, `subset()`, `isdisjoint()`,
    `difference()`, `<`, `>`, `disjoint()`, `-`
-   ungeordnet
-   (frozen)sets können frozensets enthalten

---

```python
s1 = {1, 2, 'string', object, ('ein', 'tuple')}

2 in s1  # ==> True
'ein' in s1  # ==> False
('ein', 'tuple') in s1  # ==> True
set(('ein', 'tuple'))  # ==> {'ein', 'tuple'}

s2 = {'anderes', 'set'}
s1 > s2  # ==> False
s1.isdisjoint(s2)  # ==> True

s1.add('anderes')
s1 | s2  # ==> {1, 2, 'string', object, ('ein', 'tuple'), 'set'}
s1 & s2  # ==> {'anderes'}
s2 - s1  # ==> {'set'}
```

---

```python
s2 = frozenset(s2)
s1.add(s2)
s2.add(5)  # ==> AttributeError: 'frozenset' object has no attribute 'add'
```

# Iteraton

---

-   nur foreach
-   für Iterationen über Integer gibt es `range([start], stop, step=1)`
-   um Iteratoren zu kombinieren kann man
    `zip(iterator_1, iterator_2, ..., iterator_n)` verwenden
-   alles mit einer `__iter__` Methode ist iterierbar
-   `iter(iterable)` konstruiert einen *stateful iterator*

---

```python
for i in [1,2,3]:
    if i > 9:
        break
    # code
    else:
        pass
        # wenn kein break vorkommt

for i in (1,2,3):
    # code
    pass

for i in {1:'value1', 2:'value2'}:
    # iteration ueber die keys
    pass
```

---

```python
for i in {1:'value1', 2:'value2'}.items():
    # i ist tuple von (key, value)
    pass

for value1, value2 in [
        (1, 'werner'),
        (3, 'geh mal in den keller'),
        (42, 'ich glaub die russen komm\'')
    ]:
    # iteration mit tuple unpacking
    # code
```

---

```python
# oder auch

for value1, value2 in zip([1,3,42], ['werner',
                                     'geh mal in den keller',
                                     'ich glaub die russen komm\'',
                                     'dieser string wird in \
der iteration nicht auftauchen', 'dieser auch nicht'])

for key, value in {1:'value1', 2:'value2'}.items():
    # iteration ueber keys und values mit tuple unpacking
    pass
```

# unpacking

---

-   einfaches Auflösen von Listen und Tupeln in einzelne Variablen
-   nützlich in `for`-Schleifen

---

```python
# unpacking (geht auch mit listen)
t = 1, 3, 'ein string'   # tuple ohne klammern gebaut

x, y, z = t
x is t[0]  # ==> True
y is t[1]  # ==> True

x, *y = t
x  # ==> 1
y  # ==> [3, 'ein string']

a, b, c = 1, 2, 4

d, e, f, *g = [3, 0, 8, 7, 46, 42]
f  # ==> 8
g  # ==> [7, 46, 42]
```

# Context Manager

---

-   Aufruf mit `with`
-   kann jedes Objekt sein, welches eine `__enter__` und `__exit__`
    Methode hat
-   praktisch beim *File Handling*

---

```python
class MyManager:
    def __enter__(self):
        # tue dinge
        pass

    def __exit__(self):
        # schliesse handler etc ...
        pass

    def do_things(self):
        # ...
        pass

with MyManager() as m:
    m.do_things()
```

#File Handling

---

-   Dateien können mit `open(filename, mode=r)` geöffnet werden
-   *File Handler* sind Iteratoren über die Zeilen einer Datei
-   **Wichtig:** File Handler müssen auch wieder geschlossen werden
-   `r` steht für Lesezugriff, `w` für Schreibzugriff  

**Beachte:** Wird eine Datei mit Schreibzugriff geöffnet, wird
sie geleert! Also wichtige Inhalte vorher auslesen.

---

```python
with open(myfile, mode='r') as f:
    for line in f:
        # code

with open(myfile, mode='w+') as f:

    for line in document:
        f.write(line)
        # oder
        print(line, file=f)

f = open(myfile)
# code
f.close()
```
