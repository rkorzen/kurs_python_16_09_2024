osoba = {
"imie": "Rafał",
"nazwisko": "Korzeniewski",
"godziny": 32,
"stawka": 233
}
print(osoba)
print(osoba["godziny"])
# print(osoba["wiek"])
print(osoba.get("wiek", 40))

("Rafał", "Korzeniewski", 16, 234.2)


print(osoba.items())

print(dict([('imie', 'Rafał'), ('nazwisko', 'Korzeniewski'), ('godziny', 32), ('stawka', 233)]))

print(osoba.keys())
print(osoba.values())

osoba["imie"] = "Xxx"
print(osoba)

osoba[(1, 2)] = "123"

print(hash((1, 2,3)))