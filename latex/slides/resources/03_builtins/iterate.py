for i in [1,2,3]:
    if i > 9:
        break
        # verlässt die Schleife
else:
    # wenn kein break vorkommt
    print("keine Zahl größer als 9")

# Iterator über die Zahlen von 0 bis 3 (3 nicht enthalten)
iterator = iter(range(0, 3))

# gibt 0, 1 und 2 aus
for i in iterator:
    print(i)

# kein Output, Iterator ist erschöpft
for i in iterator:
    print(i)

# gibt 1, 'value1' und 2, 'value2' aus
for i in {1:'value1', 2:'value2'}.items():
    # i ist ein Tuple von (key, value)
    print(i[0], i[1])

# iteration mit tuple unpacking
# gleiche Ausgabe wie letztes Beispiel
for key, value in {1:'value1', 2:'value2'}.items():
    print(key, value)

# zip verbindet zwei Iterables und stoppt wenn einer die Elemente ausgehen
# -4 wird deswegen nicht ausgegeben
for value1, value2 in zip((1,2,3), (-1,-2,-3,-4)):
    print(value1, value2)

# True != False
any((False, True, False)) != all((False, True, False))
