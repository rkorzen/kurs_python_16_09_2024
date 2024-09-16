# Przykład z warunkami if/else i operacjami na napisach
napis = "Ala ma kota a kot ma Alę"
napis = "aa"

# Sprawdzenie długości napisu
if len(napis) < 15:
    print(napis)
else:
    print(napis[:15])  # Wyświetlenie pierwszych 15 znaków
    print(napis[15:])  # Wyświetlenie pozostałych znaków po 15

print("Poza ifem")  # Zostanie wyświetlone po warunku if/else
print("xxx")

# Sprawdzenie warunku logicznego - len(napis) < 15
print(len(napis) < 15)  # Zwraca True, ponieważ "aa" ma mniej niż 15 znaków

# Przykład działania operatorów logicznych (komentarz, aby uniknąć błędu)
x = 1
# x > 0 or x / 0 == 1  # Operator 'or' powoduje, że dzielenie przez 0 nie zostanie wykonane, bo pierwszy warunek jest True

# Drugi blok if/else z operacją podziału (wyjątek dla błędu dzielenia przez 0)
if len(napis) < 15:
    print(napis)
else:
    1/0  # Ten kod wyrzuci błąd, jeśli zostanie wykonany (gdy napis ma więcej niż 15 znaków)
    print(napis[:15])
    print(napis[15:])
print("Pozwa ifem")
print("xxx")

# Sprawdzenie wartości zmiennej x
x = -1

# Warunek dla x
if x < 0:
    print("mniejszy")  # Zostanie wyświetlone, bo x = -1
elif x == 0:
    1/0  # Ten kod nie zostanie wykonany, bo x nie jest równy 0
else:
    print("x wiekszy")

# Przykład sprawdzania pustej listy
lista = [1, 2]

if len(lista) == 0:
    print("pusta lista")

# Alternatywny sposób sprawdzania pustej listy
if not lista:  # Jeżeli lista jest pusta, zwróci True
    print("pusta lista")

# Wyświetlanie wartości logicznych
# False: 0, 0.0, [], (), {}, ""
# True: różne od zera bądź niepuste wartości
print(bool(2), bool(0), bool(""))  # True, False, False

# Sprawdzenie, czy element jest w liście
print(1 in lista)  # True, bo 1 jest w liście [1, 2]

# Operator "in" może być stosowany dla zbiorów, krotek, list i napisów
# W słownikach operator "in" sprawdza, czy klucz istnieje
print(1 in {1: "a"})  # True, bo 1 jest kluczem w słowniku {1: "a"}
print(1 in {"a": 1})  # False, bo 1 nie jest kluczem w słowniku {"a": 1}
