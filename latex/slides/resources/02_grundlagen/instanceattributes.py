def Human():
    def __init__(firstname, lastname):
        # die beiden Parameterwerte werden in Instanzattributen gespeichert.
        self.firstname = firstname
        self.lastame = lastname

def main():
    # instanziiert zwei Objekte vom Typ 'Human'
    matthias = Human("Matthias", "Stuhlbein")
    john = Human("John", "Doe")
