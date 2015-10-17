var = 12

def foo():
    # erwarteter Effekt: var wird auf 9 gesetzt
    var = 9

def main():
    print(var)  # -> gibt 12 zurück
    foo()
    print(var)  # -> Erwartung: gibt 9 aus.
                # Realität: gibt 12 aus.

if __name__ == '__main__':
    main()
