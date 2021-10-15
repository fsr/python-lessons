# Basics

---

Comprehensions sind eine bequeme Art und Weise, um
_Funktoren_ (Datenstrukturen, die andere Datenstrukturen beinhalten) mit
kleinen Expressions zu erstellen und zu füllen und sind in allen
modernen Sprachen vorhanden.


# List Comprehensions

---


Grundlegender Syntax:

```python
[EXPRESSION for LAUFVARIABLE in ITERABLE (if FILTER)]
```


### EXPRESSION

ein beliebiger Ausdruck (man stelle sich ein implizites
`return` vor), etwa ein Wert, eine Variable, eine Gleichung, etc ...  

`EXPRESSION` wird am Ende in der Liste abgelegt.

---

### LAUFVARIABLE

Eine beliebige Variable, die in *EXPRESSION* und *FILTER* zur
Verfügung steht

---

### ITERABLE

Ist häufig etwas wie `range()` oder eine andere Liste.

---

### FILTER

Eine optionale boolean expression, womit Einträge gefiltert werden
(falls Expression `false`) Nützlich, wenn z.B. nur gerade Zahlen übernommen werden
sollen, usw...

---

### Beispiel

```python
varList = [var * 8 for var in range(10)]
# => [0, 8, 16, 24, 32, 40, 48, 56, 64, 72]


# mit Filter (hier: für i ist gerade)
evenVarList = [var * 8 for var in range(10) if var % 2 == 0]
# => [0, 16, 32, 48, 64]
```


# Dict Comprehension

---

Grundlegender Syntax:

```python
{KEY: VALUE for LAUFVARIABLE in ITERABLE (if FILTER)}
```

---

Fast der gleiche Syntax, nur diesmal mit 2 Expressions: __KEY__ und
__VALUE__. Ansonsten gelten die gleichen Regeln.

---

## Beispiel

```python
liste = ["Fritz", "Alex", "Nadine", "Peter", "Anna"]

names = {key: len(key) for key in liste}
# => {'Peter': 5, 'Fritz': 5, 'Alex': 4, 'Anna': 4, 'Nadine': 6}
```


# Generators

## Generator

Ein Objekt, über das iteriert werden kann. Wenn ein Element daraus
verwendet wurde, ist es nicht mehr in dem Generatorobjekt
enthalten.

---

Grundlegender Syntax:

```python
(EXPRESSION for LAUFVARIABLE in ITERABLE (if FILTER))
```

Da sich `list` und `dict` auch aus Iterables bauen lassen, gilt prinzipiell:

```python
list(EXPR for VAR in ITERABLE) == [EXPR for VAR in ITERABLE]
```
und
```python
dict((KEY, VAL) for VAR in ITERABLE) == {KEY: VAL for VAR in ITERABLE}
```

**Aber:** Generatoren sind lazy, sie erzeugen die Elemente erst wenn sie iteriert werden.

---

## Beispiel

```python
# liefert gerade Zahlen von 0 bis 10 (10 nicht enthalten)
generator = (i for i in range(10) if i % 2 == 0)

# gibt 0, 2, 4, 6 und 8 aus
for number in generator:
    print(number)

# gibt nichts aus, generator ist erschöpft
for number in generator:
    print(number)

# wenn alle Elemente sofort erzeugt werden würde mindestens 4GB Speicher benötigt
for number in (i for i in range(2**32)):
    print(number)
```


# Nesting

## Nesting

`for` Schleifen in Comprehensions können verschachtelt werden.
Dabei werden sie von Links nach Rechts ausgeführt, was man bei Variablen beachten muss.

**Wichtig:** Starke Verschachtelung verringert die Lesbarkeit!

---

## Beispiel

```python
# erzeugt eine Liste welche jede Zahl n
# von 0 bis 4 (4 nicht enthalten) n mal enthält
list1 = [i for i in range(4) for _ in range(i)]

# gleicher Code ohne Comprehension
list2 = []
for i in range(4):
    for _ in range(i):
        l.append(i)

list1 == list2 == [1,2,2,3,3,3]

# löst einen NameError aus, weil
# a erst durch die zweiten Schleife entsteht
[i for i in range(a) for a in range(i)]

# zählt für jede Zahl n von 0 bis 4 (4 nicht enthalten)
# von 0 bis n-1, weil EXPRESSION erst nach der letzten
# Schleife evaluiert wird
list3 = [a for i in range(4) for a in range(i)]

list3 == [0,0,1,0,1,2]
```
