var = 12

def foo():
    global var
    # global sagt dem Interpreter, dass er hier auf die oberhalb definierte Variable zurueckgreifen soll
    var = 9

def main():
    print(var)  # -> gibt 12 zurueck
    foo()
    print(var)  # -> gibt jetzt 9 aus

if __name__ == '__main__':
    main()
