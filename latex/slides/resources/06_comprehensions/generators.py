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
