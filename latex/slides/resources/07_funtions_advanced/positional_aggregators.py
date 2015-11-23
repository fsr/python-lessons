def f(*args):
    print(type(args))  # ==> tuple


def function(param1, *aggr, param2=0):
    pass


function(1, 2, 3, 4)    # korrekt, aggr = (2,3,4)
function(1, 2, 4, 5, 6, 78, 9, 90, 0)
# auch korrekt, aggr = (2,4,5,6,78,9,90,0)
function()    # inkorrekt, param1 braucht mindestens ein Argument
function(1, param2=7)    # korrekt, aggr = ()
function(param2=8)    # inkorrekt, param1 braucht einen Wert
function(param2=0, param1=6)    # korrekt
