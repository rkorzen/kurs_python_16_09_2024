class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<Vector({self.x},{self.y})>"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return NotImplemented
    
    def __rmul__(self, other):
        return self.__mul__(other)

    """
    __mul__
    __truediv__
    __modiv__


    """

v1 = Vector(1, 1)
v2 = Vector(1, 1)
print(v1 * 3)
print(3 * v1)
print(v1 + v2)

# class X:
#     def __init__(self):
#         self.x = 19
#         self.y = 20
#         self.a = 20

# print(v1 + X())

# # print([v])