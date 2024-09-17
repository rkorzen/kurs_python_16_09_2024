# def suma(a, b):
#     return a + b


# suma(1, 2)
# suma(a=10, b=20)
# suma(b=10, a=20)
# suma(1, b=2)

# # suma(a=1, 2)


# def suma(a, b=1):
#     return a + b


# suma(1)
# suma(1, 2)


def suma(a: int = 0, b: int = 1) -> int:
    return a + b


suma(1)
print(suma(1, 2))

print(suma("a", "b"))
