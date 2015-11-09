# Funktionen Variablen zuweisen
def return_hello():
    return "Hello"

say_hello = return_hello

print say_hello()
# => Hello


# Funktionen in Funktionen definieren
def greet(name):
    def return_hello():
        return "Hello "
    greeting = return_hello() + name
    return greeting

print greet("World")
# => Hello World


# Rueckgabe von Funktionen
def greet():
    def say_hello():
        return "Hello"
    return say_hello

print greet()
# Hello


# Uebergabe von Funktionen
def say_date(date):
    return "Today it's {date}".format(date=date)

def which_date(function):
    date = "25th June 2015"
    return function(date)

print which_date(say_date)
# => Today it's 25th June 2015
