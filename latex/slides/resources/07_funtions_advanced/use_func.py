def function(params):
    return 4

my_var = function
my_var(2)  # ==> 4


def callif(boolean, callback):
    if boolean:
        callback()

callif(True, lambda: print("hello world"))


class MyClass(object):
    def function(self, param):
        return 4

my_var = MyClass.function
my_var(MyClass(), 2)  # ==> 4
