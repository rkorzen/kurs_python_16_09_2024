# Definicja szablonu formatowania
template = "a: {:^6}, b: {:<6}, p: {:12.3f}"

# Definiowanie krotek z danymi osób
osoba1 = ("Rafał", "Korzniewski", 16, 234.2)
osoba2 = ("Adam", "Sodowy", 16, 23.2)
osoba3 = ("A", "B", 16, 23.2)

# Wybranie jednej osoby do formatowania
osoba = osoba3

# Formatowanie i wyświetlanie danych wybranej osoby
print(template.format(osoba[0], osoba[1], osoba[2], osoba[3]))

# Formatowanie i wyświetlanie danych osoby Rafała
print(template.format(*osoba1))

# Wyświetlenie co drugiego elementu z krotki osoba1 (Rafał, 16)
print(osoba1[::2])

# Znalezienie indeksu elementu "Rafał" w krotce osoba1
print(osoba1.index("Rafał"))

# Próba modyfikacji krotki jest zakomentowana, ponieważ krotki są niemutowalne.
# osoba1[0] = "Xxx"  # Ten kod wyrzuci błąd, bo krotki są niemutowalne

# Operacja rozpakowywania krotki (a, b = pierwsze dwie wartości, *c = reszta wartości)
# a, b, *c = 1, 2, 3, 4
# print(a, b, c)  # Zmienna c to lista [3, 4]

# Łączenie krotek
print((1, 2, 3) + (4, 5, 6))  # Wynik: (1, 2, 3, 4, 5, 6)

# Poniższy kod został zakomentowany, aby uniknąć błędu indeksu, ponieważ krotka osoba1 ma mniej niż 10 elementów
# print(osoba1[10])  # Błąd: IndexError, bo krotka ma tylko 4 elementy
