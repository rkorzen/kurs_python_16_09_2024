"""
napisz kod, ktory bedzie dzialal nastepujaco:

$ python baza.py
Odczyt czy zapis [o, z]: o
a: 10, b: 20
a: 11, b: 11

$ python baza.py
Odczyt czy zapis [o, z]: z
podaj a: 11
podaj b: 13

$ python baza.py
Odczyt czy zapis [o, z]: o
a: 10, b: 20
a: 11, b: 11
a: 11, b: 13

"""
import json

try:
    with open("data/ddd.json") as f:
        dane = json.load(f)
except FileNotFoundError:
    dane = []


tryb = input('Odczyt czy zapis [o, z]')

if tryb == "o":
    for d in dane:
        print(f"a: {d['a']}, b: {d['b']}")
if tryb == "z":
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))
    d = {"a": a, "b": b}
    dane.append(d)

    with open("data/ddd.json", "w") as f:
        json.dump(dane, f)