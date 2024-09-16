
### 1. **Podstawowe zasady:**
- Python jest dynamicznie typowany (nie trzeba deklarować typów zmiennych).
- Bloki kodu są wyznaczane przez wcięcia (zazwyczaj 4 spacje).
- funkcje `help` i `dir` to Twoi sprzymierzeńcy

```python

dir("napis")
help(str.lower)

```

### 2. **Zmienne i podstawowe typy:**
```python
x = 10       # int
y = 3.14     # float
z = "Hello"  # str
b = True     # bool

print(x, y, z, b)  # Wyświetlanie wartości zmiennych
```

### 3. **Operatory:**
- Aritmetyczne: `+`, `-`, `*`, `/`, `//` (dzielenie całkowite), `%` (modulo), `**` (potęgowanie).
- Logiczne: `and`, `or`, `not`.
- Porównania: `==`, `!=`, `>`, `<`, `>=`, `<=`.

### 4. **Listy** (mutowalne):
```python
lista = [1, 2, 3]
lista.append(4)     # Dodanie elementu
lista.remove(2)     # Usunięcie elementu
print(lista[0])     # Dostęp do pierwszego elementu
print(lista[-1])    # Dostęp do ostatniego elementu
print(lista[1:3])   # Slicing (elementy od 1 do 2)
```

### 5. **Krotki** (niemutowalne):
```python
krotka = (1, 2, 3)
print(krotka[0])    # Dostęp do elementu
# krotka[0] = 10    # Błąd: krotki są niemutowalne
```

### 6. **Słowniki** (klucz-wartość):
```python
slownik = {"imie": "Rafał", "wiek": 30}
print(slownik["imie"])  # Dostęp do wartości po kluczu
slownik["miasto"] = "Warszawa"  # Dodanie nowej pary
print(slownik.keys())  # Zwraca klucze
print(slownik.values())  # Zwraca wartości
```

### 7. **Zbiory** (unikalne elementy):
```python
zbior = {1, 2, 3, 2}
zbior.add(4)       # Dodanie elementu
zbior.remove(1)    # Usunięcie elementu
print(zbior)
```

### 8. **Wyrażenia warunkowe:**
```python
x = 5
if x > 10:
    print("Większe niż 10")
elif x == 5:
    print("Równe 5")
else:
    print("Mniejsze niż 10")
```

### 9. **Pętle:**
- **`for`**: iteracja po elementach:
```python
for i in range(5):  # Liczby od 0 do 4
    print(i)
```
- **`while`**: iteracja, dopóki warunek jest spełniony:
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 10. **Funkcje:**
```python
def suma(a, b):
    return a + b

print(suma(3, 4))  # Wywołanie funkcji
```

### 11. **List comprehension** (skrótowy zapis tworzenia list):
```python
kwadraty = [x**2 for x in range(5)]
print(kwadraty)  # [0, 1, 4, 9, 16]
```

### 12. **Obsługa wyjątków:**
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Błąd: dzielenie przez zero")
```

### 13. **Wbudowane funkcje:**
- `len(lista)` – długość listy,
- `sum(lista)` – suma elementów,
- `max(lista)` – maksymalna wartość,
- `min(lista)` – minimalna wartość.

