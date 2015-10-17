class TestClass():
    # jeder Instanz wird bei Erstellung bereits dieses Attribut zugewiesen
    num = 12

def main():
    a = TestClass()
    b = TestClass()
    # beide Variablen haben fuer 'num' von der Erstellung an den gleichen Wert

    # das Aendern der Variable ueberschreibt das Klassenattribut mit einem Instanzattribut
    a.num = -3
    print(b.num)  # -> liefert immer noch 12
