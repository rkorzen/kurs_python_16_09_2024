# class Samochod:

#     def __init__(self, nazwa):
#         self.nazwa = nazwa
#         self.predkosc = 0

#     def przyspiesz(self):
#         self.predkosc += 10
#         self.info()

#     def zwolnij(self):
#         self.predkosc -= 10
#         self.info()
        
#     def info(self):
#         print(f"Samochod porusza sie z predkoscia {self.predkosc}")

# s1 = Samochod("A")
# s2 = Samochod("B")

# s1.przyspiesz()
# s1.zwolnij()


"""

s = ElectricCar()
s.drive(70) == 70
s.drive(70) == 30
s.drive(10) == 0

s.charge()
s.drive(10) == 10
s.drive(100) == 90

"""

class ElectricCar:
    def __init__(self):
        self.energy = 100

    def drive(self, distance):
        if self.energy > distance:
            self.energy -= distance
            return distance
        to_travel = self.energy
        self.energy = 0
        return to_travel

    def charge(self):
        self.energy = 100

c = ElectricCar()
assert c.drive(70) == 70
assert c.drive(70) == 30
assert c.drive(10) == 0
assert c.charge() is None
assert c.drive(70) == 70
assert c.drive(70) == 30
assert c.drive(10) == 0


print(id(c.charge()))
print(id(None))