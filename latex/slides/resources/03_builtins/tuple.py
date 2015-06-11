# Tupel mit 3 Elementen
t = (1, 3, "ein string")
# oder auch ohne klammern
isinstance(t, tuple) # ==> True

t[0] == 1  # ==> True
t[1] == 3  # ==> True
t[2] == "ein string"  # ==> True
t[4] == "ein string"  # ==> IndexError: tuple index out of range
t[2] = "ein anderer string"  # ==> TypeError: 'tuple' object does not support item assignment

t = 1, 3, "ein string"
# macht es (manchmal) besser lesbar, z.b. bei
return 1, 2, 5
