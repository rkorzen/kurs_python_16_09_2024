# Definiowanie zbiorów
a = {1, 2, 3}
b = set([2, 3, 4])  # Można także zapisać b = {2, 3, 4}

# Operacje na zbiorach

# Suma zbiorów (elementy, które są w a lub b)
print(a | b)  # {1, 2, 3, 4}

# Przecięcie zbiorów (elementy, które są wspólne dla a i b)
print(a & b)  # {2, 3}

# Różnica zbiorów (elementy, które są w a, ale nie w b)
print(a - b)  # {1}

# Różnica symetryczna (elementy, które są w a lub b, ale nie w obu)
print(a ^ b)  # {1, 4}

# Sprawdzenie, czy c jest nadzbiorem a (c zawiera wszystkie elementy a)
c = {1, 3}
print(c.issuperset(a))  # False, bo brakuje elementu 2

# Sprawdzenie, czy a jest nadzbiorem c
print(a.issuperset(c))  # True, bo a zawiera wszystkie elementy c

# Konwersja listy na zbiór (usunięcie duplikatów)
lista = [2, 2, 2, 2, 3]
print(set(lista))  # {2, 3}

# Dodawanie krotki do zbioru (można dodać tylko elementy hashowalne, np. krotki)
c.add((1, 2))
print(c)  # {1, 3, (1, 2)}
