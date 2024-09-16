kolekcja = "Ala ma kota"

# while 
i = 0
while True:
    print(kolekcja[i])
    if i == 10:
        break
    i += 1


i = 0
while i < 11:
    print(kolekcja[i])
    i += 1


# for

for element in kolekcja:
    print(element)


for index in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(kolekcja[index])

print("-"*40)
# break i continue

kolekcja = "abc"

for s in kolekcja:
    if s == "b":
        continue
    print(s)

i = 0
while i < 3:
    if kolekcja[i] == "b":
        i += 1
        continue
    print(kolekcja[i])
    i += 1

print("-"*40)

liczby = []

while True:
    s = input("Podaj liczbe lub wpisz q by zakonczyc: ")
    if s == "q":
        break
    liczby.append(int(s))

### 
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 15:
        break
else:
    print("Done")

