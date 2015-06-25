def get_date(date):
    return ", today it's {}.".format(date)


# unser decorator
def tell_the_world(func):
    def complete_sentence(date):
        return "Hello World{}".format(func(date))
    return complete_sentence

# normaler Aufruf:
print tell_the_world(get_date)("25th June 2015")

# als decorator
get_date = tell_the_world(get_date)

print get_date("25th June 2015")
# => Hello World, today it's 25th June 2015.



# Nutzung des @ Syntaxes

def tell_the_world(func):
    def complete_sentence(date):
        return "Hello World, {}".format(func(date))
    return complete_sentence


@tell_the_world
def get_date(date):
    return "today it's {}.".format(date)

print get_date("25th June 2015")
# => Hello World, today it's 25th June 2015.


# Decorator mit Argumenten
def tell_the_date_to(name):
    def name_decorator(func):
        def complete_sentence(date):
            return "Hello {name}, {date}".format(name=name, date=func(date))
        return complete_sentence
    return name_decorator


@tell_the_date_to("John Doe")
def get_date(date):
    return "today it's {}.".format(date)

print get_date("25th June 2015")
# => Hello John Doe, today it's 25th June 2015.
