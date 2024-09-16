import copy

# Definiujemy szablon do formatowania wyjścia
template = "a: {:^6}, b: {:<6}, p: {:12.3f}"

# Definiujemy osoby
osoba1 = ["Rafał", "Korzeniewski", 16, 234.2]
osoba2 = ["Adam", "Sodowy", 16, 23.2]
osoba3 = ["A", "B", 16, 23.2]

# Wybór osoby do formatowania
osoba = osoba3

# Formatowanie wybranej osoby
print(template.format(osoba[0], osoba[1], osoba[2], osoba[3]))

# Formatowanie innych osób
print(template.format(*osoba1))

# Wyświetlenie elementów co drugi od początku
print(osoba1[::2])

# Znalezienie indeksu imienia "Rafał"
print(osoba1.index("Rafał"))

# Modyfikacja listy osoba1
print(osoba1)
osoba1[0] = "Xxx"
print(osoba1)

# Operacje na listach
print([1, 2, 3] + [4, 5, 6])

# Dodawanie elementu do listy osoba1
osoba1.append(100)
print(osoba1)

# Operacje na liście 'lista'
lista = [1, 2, 3, 4]
lista.append(6)
print(lista)

# Wstawianie elementu na początku listy
lista.insert(0, 7)
print(lista)

# Sprawdzenie dostępnych metod dla listy
print(dir(lista))

# Usuwanie elementu
lista.remove(7)
print(lista)

# Przykład mutowalności list
x = [1, 2, 3]
y = x
x.append(10)
y.append(11)
print(x, y)

# Kopiowanie listy
z = x.copy()
x.remove(1)
print(x, y, z)

# Operacje na zagnieżdżonych listach
a = [1, 2]
b = [3, 4, a]  # [3, 4, [1, 2]]
c = b

a.append(10)
print(a, b, c)

# Kopiowanie płytkie listy
a = [1, 2]
b = [3, 4, a]  # [3, 4, [1, 2]]
c = b.copy()

a.append(10)
print(a, b, c)

# Kopiowanie głębokie listy
a = [1, 2]
b = [3, 4, a]  # [3, 4, [1, 2]]
c = copy.deepcopy(b)

a.append(10)
print(a, b, c)
