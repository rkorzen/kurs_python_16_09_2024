"""
Otworz plik
wypisz wiersze w ten sposob by byly ponumerowane

"""

import sys

try:
    nazwa_pliku = sys.argv[1] 
except IndexError:
    print("Nie podano nazwy pliku")
    exit(1)


# plik =  "README.md"
try:
    with open(nazwa_pliku) as f:
        for i, line in enumerate(f, start=1):
            print(f"{i:4} {line}", end="")
except FileNotFoundError:
    print("Nie znaleziono pliku o tej nazwie")
    exit(1)

