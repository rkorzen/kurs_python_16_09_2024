# Słownik z danymi osoby
osoba = {
    "imie": "Rafał",
    "nazwisko": "Korzeniewski",
    "godziny": 32,
    "stawka": 233
}

# Wyświetlenie całego słownika
print(osoba)

# Dostęp do wartości klucza "godziny"
print(osoba["godziny"])

# Przykład obsługi sytuacji, gdzie klucz "wiek" nie istnieje w słowniku
# Zamiast zgłaszać błąd, zwróci wartość domyślną (w tym przypadku 40)
print(osoba.get("wiek", 40))

# Wyświetlenie wszystkich par klucz-wartość w słowniku
print(osoba.items())

# Tworzenie słownika z listy krotek
print(dict([('imie', 'Rafał'), ('nazwisko', 'Korzeniewski'), ('godziny', 32), ('stawka', 233)]))

# Wyświetlenie samych kluczy słownika
print(osoba.keys())

# Wyświetlenie samych wartości słownika
print(osoba.values())

# Modyfikacja wartości przypisanej do klucza "imie"
osoba["imie"] = "Xxx"
print(osoba)

# Dodanie nowego klucza-krotki (1, 2) do słownika z wartością "123"
osoba[(1, 2)] = "123"
print(osoba)

# Hashowanie krotki (1, 2, 3) - sprawdzenie wartości hash
print(hash((1, 2, 3)))

# Próba hashowania niektórych typów, jak lista, spowodowałaby błąd,
# ponieważ lista jest typem niemutowalnym, a tylko mutowalne typy mogą być hashowane.
