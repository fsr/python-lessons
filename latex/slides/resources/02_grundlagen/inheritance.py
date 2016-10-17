class Human():
    def __init__(self, fistname, lastname, dob):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob


class Child(Human):
    # Ein Child ist einfach nur ein Human mit den
    # zusaetzlichen Attributen father und mother
    def __init__(self, fistname, lastname, dob, father, mother):
        super.__init__(fistname, lastname, dob)
        self.father = father
        self.mother = mother
