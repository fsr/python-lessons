# unpacking (geht auch mit listen)
t = 1, 3, "ein string"   # tuple ohne klammern gebaut

x, y, z = t
x is t[0]  # ==> True
y is t[1]  # ==> True

# oder
x, *y = t
y  # ==> 1
y  # ==> [3, "ein string"]

a, b, c = 1, 2, 4

d, e, f, *g = [3, 0, 8, 7, 46, 42]
f  # ==> 8
g  # ==> [7, 46, 42]
