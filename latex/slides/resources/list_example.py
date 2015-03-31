list_1 = [1, 2, 3]  # lists can be created using square brakets

type(list_1) == list  # ==> True

list_2 = [  # lists can contain different types
    1,  # an integer
    'a string',  # a string
    int  # a type
]

list_3 = list(list_2)  # lists can be created from other iterables using the list() constructor

list_1[1] == 2  # indexing with square brackets
list_1[0] = 4  # settings using quare brackets

list_1.append('new string')  # append to the end
list_1 == [4, 1, 3, 'new string']  # ==> True
# pop from the end 
# removes and returns the element
list_1.pop()  # ==> 'new string'

list_1 == [4, 1, 3]  # ==> True

# new in python 3.4
list_1.clear()
list_1 == []  # ==> True
