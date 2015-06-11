s1 = {1, 2, "string", object, ("ein", "tuple")}

2 in s1  # ==> True
"ein" in s1  # ==> False
("ein", "tuple") in s1  # ==> True
set(("ein", "tuple"))  # ==> {"ein", "tuple"}

s2 = {"anderes", "set"}
s1 > s2  # ==> False
s1.isdisjoint(s2)  # ==> True

s1.add("anderes")
s1 | s2  # ==> {1, 2, "string", object, ("ein", "tuple"), "set"}
s1 & s2  # ==> {"anderes"}
s2 - s1  # ==> {"set"}

s2 = frozenset(s2)
s1.add(s2)
s2.add(5)  # ==> AttributeError: 'frozenset' object has no attribute 'add'
