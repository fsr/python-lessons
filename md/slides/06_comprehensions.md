---
title: Comprehensions
---

# Basics

---

Comprehensions sind eine bequeme Art und Weise, um
_Funktoren_ (Datenstrukturen, die andere Datenstrukturen beinhalten) mit
kleinen Expressions zu erstellen und zu füllen und sind in allen
modernen Sprachen vorhanden.


# List Comprehensions


Grundlegender Syntax:

```python
[EXPRESSION for LAUFVARIABLE in ITERABLE (if FILTER)]
```

---

### EXPRESSION

ein beliebiger Ausdruck (man stelle sich ein implizites
`return` vor). Wie ein Wert, eine Variable, eine Gleichung, etc ...  

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


## Beispiel

```python
varList = [var * 8 for var in range(10)]
# => [0, 8, 16, 24, 32, 40, 48, 56, 64, 72]


# mit Filter (hier: für i ist gerade)
evenVarList = [var * 8 for var in range(10) if var % 2 == 0]
# => [0, 16, 32, 48, 64]
```


# Dict Comprehension


Grundlegender Syntax:

```python 
{KEY: VALUE for LAUFVARIABLE in ITERABLE (if FILTER)}
```

---

Fast der gleiche Syntax, nur diesmal mit 2 Expressions: __KEY__ und
__VALUE__. Ansonsten gelten die gleichen Regeln.


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

Die grundlegende Syntax ist gleich der einer *List Comprehension*. Da
sich und auch aus Iterables bauen lassen gilt prinzipiell:

```python
list(EXPR for VAR in ITERABLE) == [EXPR for VAR in ITERABLE]
```
und
```python
dict((KEY, VAL) for VAR in ITERABLE) == {KEY: VAL for VAR in ITERABLE}
```

---

**Aber:** Generators verhalten sich anders als Lists oder Dicts!
