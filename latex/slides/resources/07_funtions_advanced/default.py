def greet(name, greeting='Hello'):
    return '{} {}'.format(greeting, name)

greet('Herbert')  # ==> 'Hallo Herbert'
greet('Herbert', 'Gruess Gott')  # ==> 'Gruess Gott Herbert
