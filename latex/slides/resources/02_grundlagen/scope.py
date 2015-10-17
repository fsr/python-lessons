var = 12

def foo():
    # erwarteter Effekt: var wird auf 9 gesetzt
    var = 9

def main():
    print(var)  # -> gibt 12 zurueck
    foo()
    print(var)  # -> Erwartung: gibt 9 aus.
                # Realitaet: gibt 12 aus.

if __name__ == '__main__':
    main()
