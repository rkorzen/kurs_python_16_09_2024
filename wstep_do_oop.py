

class Square:
    def __init__(self, side=1):
        if side < 0:
            raise ValueError("Bok nie może miec ujemnej dlugosci")
        self.side = side
        # self.area = side * side


    @property  # pozbywamy sie nawiasow
    def side(self):
        return self._side
    
    @side.setter
    def side(self, value):
        if value < 0:
            raise ValueError("Bok nie może miec ujemnej dlugosci")
        self._side = value


    @property  # pozbywamy sie nawiasow
    def area(self):
        return self.side ** 2
    
    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Bok nie może miec ujemnej dlugosci")
        self.side = value ** 0.5


s1 = Square()


s1.area = 100
print(s1.area)
s1.side = -100