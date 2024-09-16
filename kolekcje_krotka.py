template = "a: {:^6}, b: {:<6}, p: {:12.3f}"
#         0        1              2   3 
osoba1 = ("Rafał", "Korzniewski", 16, 234.2)
osoba2 = ("Adam", "Sodowy", 16, 23.2)
osoba3 = ("A", "B", 16, 23.2)

osoba = osoba3

print(template.format(osoba[0], osoba[1], osoba[2], osoba[3]))

print(template.format(*osoba1))

print(osoba1[::2])


print(osoba1.index("Rafał"))

# osoba1[0] = "Xxx"
# a, b, *c = 1, 2, 3, 4

# print(a, b, c)

print((1, 2, 3) + (4, 5, 6))

# print(osoba1[10])