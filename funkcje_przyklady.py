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

def roznica(a, b):
    return a - b

suma(1)
print(suma(1, 2))
print(suma("a", "b"))

x = suma
x(1, 2)

operacje = [suma, roznica]

for op in operacje:
    print(op(1, 2))


def add(a, b, *args, pretty_print=False, **kwargs):

    print(args)
    print(kwargs)

add(1 , 2, 3, 4)

add(1, 2, 3, 4, pretty_print=True, to_float=True)