

class Square:
    def __init__(self, side=1):
        if side < 0:
            raise ValueError("Bok nie może miec ujemnej dlugosci")
        self.side = side
        # self.area = side * side

    @property  # pozbywamy sie nawiasow
    def area(self):
        return self.side ** 2
    
    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Bok nie może miec ujemnej dlugosci")
        self.side = value ** 0.5


s1 = Square()
print(s1.area)
s1.area = -100
# s.side = 1

s2 = Square(10)
# s2.side = -15
# s2.set_side(-15)

# s3 = Square(-10)

print(Square)
print(s1.side)
print(s2.side)
print(s1.area)
print(s2.area)