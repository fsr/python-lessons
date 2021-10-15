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
# a erst durch die zweite Schleife entsteht
[i for i in range(a) for a in range(i)]

# zählt für jede Zahl n von 0 bis 4 (4 nicht enthalten)
# von 0 bis n-1, weil EXPRESSION erst nach der letzten
# Schleife evaluiert wird
list3 = [a for i in range(4) for a in range(i)]

list3 == [0,0,1,0,1,2]
