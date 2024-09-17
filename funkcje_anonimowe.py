

lista = [(4, 50), (3, 100), (1, 20), (5, 11), (21, 22), (-11, 70)]

# def second(x): return x[1]

# second = lambda x: x[1]


# help(lista.sort)
print(lista.sort(reverse=False, key=lambda x: x[1]))
print(lista)

xxx = lambda x, y: (y+1, x+9)

xxx(1, 2)