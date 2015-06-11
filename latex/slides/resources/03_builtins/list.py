l = [1, 9, "string", object]

isinstance(l[0], int)  # ==> True
l[1] == 9  # ==> True
len(l)  # ==> 4

9 in l  # ==> True

l.pop()  # ==> object
len(l)  # ==> 3
l.append([])  # ==> None

l  # ==> [1, 9, "string", []]
len(l)  # ==> 4
