class Samochod:

    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.predkosc = 0

    def przyspiesz(self):
        self.predkosc += 10
        self.info()

    def zwolnij(self):
        self.predkosc -= 10
        self.info()
        
    def info(self):
        print(f"Samochod porusza sie z predkoscia {self.predkosc}")

s1 = Samochod("A")
s2 = Samochod("B")

s1.przyspiesz()
s1.zwolnij()