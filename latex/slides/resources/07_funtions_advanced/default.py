def greet(name, greeting='Hello'):
    return '{} {}'.format(greeting, name)

greet('Herbert')  # ==> 'Hallo Herbert'
greet('Herbert', 'Gruess Gott')  # ==> 'Gruess Gott Herbert'


def func(param1, param2=[]):
    print(param2)
    param2.append(param1)

func(1)  # ==> []
func(2)  # ==> [1]
func('j')  # ==> [1,2]


def func(param1, param2=None):
    param2 = [] if param2 is None else param2
    pass


def land(house, tree, pond):
    return 'You own land with a {} a {} and a {}'.format(house, tree, pond)

land('green house', 'maple', 'fish pond')
# oder mit Aufruf durch namen:
land(house='green house', pond='fish pond', tree='maple')
# or vermischt
land('green house', pond='fish pond', tree='maple')
# folgendes funktioniert NICHT!
land('maple', house='green house', tree='maple'
