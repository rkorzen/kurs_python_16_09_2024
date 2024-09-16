napis = "Ala ma kota"

print(napis[0])
print(napis[10])
print(napis[-1])
print(napis[-11])

# wybieranie - slicing
print(napis[3:7])

print(napis[1:10:3])

print(napis[0:10:3])
print(napis[:10:3])


print(napis[3:11:3])
print(napis[3::3])

print(napis[0:11:3])
print(napis[::3])

print(napis[::-1])


# sprawdzanie indexu

print(napis.index('t'))

napis[9] = "T"