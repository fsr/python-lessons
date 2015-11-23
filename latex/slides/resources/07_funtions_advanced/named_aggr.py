def function(param1, **aggr):
    pass


function(1)    # korrekt, aggr = {}
function(1, some=9)    # korrekt, agar = {'some': 9}
function(some=6)    # inkorrekt, param1 braucht einen Wert
function(some=0, param1=8, param2=4)
# korrekt, agar = {'some': 0, ’param2': 4}
