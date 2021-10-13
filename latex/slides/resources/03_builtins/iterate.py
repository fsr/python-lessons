for i in [1,2,3]:
    if i > 9:
        break
        # verlässt die Schleife
else:
    pass
    # wenn kein break vorkommt

for i in (1,2,3):
    # code
    pass

for i in {1:'value1', 2:'value2'}:
    # iteration ueber die keys
    pass


for i in {1:'value1', 2:'value2'}.items():
    # i ist tuple von (key, value)
    pass

for value1, value2 in [
        (1, 'werner'),
        (3, 'geh mal in den keller'),
        (42, 'ich glaub die russen komm\'')
    ]:
    # iteration mit tuple unpacking
    # code

# oder auch

for value1, value2 in zip([1,3,42], ['werner', 'geh mal in den keller', 'ich glaub die russen komm\'', 'dieser string wird in der iteration nicht auftauchen', 'dieser auch nicht'])

for key, value in {1:'value1', 2:'value2'}.items():
    # iteration ueber keys und values mit tuple unpacking
    pass
