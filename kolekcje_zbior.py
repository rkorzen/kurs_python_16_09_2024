a = {1, 2, 3}
b = set([2, 3, 4])  # b = {2, 3, 4}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


c = {1, 3}

print(c.issuperset(a))
print(a.issuperset(c))

lista = [2, 2, 2, 2, 3]

print(set(lista))

c.add((1, 2))

print(c)

