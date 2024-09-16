kolekcja = "Ala ma kota"

# while 
i = 0
while True:
    print(kolekcja[i])
    if i == 10:
        break
    i += 1

kolekcja = "Ala ma kota"

# Pętla while - wypisywanie znaków z kolekcji, zatrzymanie na 10 znaku
i = 0
while i < len(kolekcja):  # Zamiast 'while True', możemy bezpośrednio użyć warunku
    print(kolekcja[i])
    if i == 10:  # Zatrzymanie na 10 znaku
        break
    i += 1

# Alternatywna wersja - pętla while do 11 znaku
i = 0
while i < 11:
    print(kolekcja[i])
    i += 1

# Pętla for - iterowanie po każdym znaku w kolekcji
for element in kolekcja:
    print(element)

# Pętla for - iterowanie po indeksach (użycie range zamiast ręcznej listy)
for index in range(11):  # Zakładam, że chcesz wydrukować pierwsze 11 znaków
    print(kolekcja[index])

print("-" * 40)

# Przykład z użyciem break i continue - dla kolekcji "abc"
kolekcja = "abc"

# Pętla for z continue - pominięcie litery 'b'
for s in kolekcja:
    if s == "b":
        continue  # Pomija 'b' i przechodzi do kolejnej iteracji
    print(s)

# Pętla while z continue - pominięcie litery 'b'
i = 0
while i < len(kolekcja):  # Poprawka na dynamiczne liczenie długości kolekcji
    if kolekcja[i] == "b":
        i += 1
        continue  # Pomija 'b' i przechodzi do kolejnej iteracji
    print(kolekcja[i])
    i += 1

print("-" * 40)

# Pobieranie liczb od użytkownika do momentu wpisania 'q'
liczby = []
while True:
    s = input("Podaj liczbę lub wpisz 'q' by zakończyć: ")
    if s == "q":
        break  # Zatrzymanie pętli, jeśli użytkownik wpisze 'q'
    liczby.append(int(s))  # Dodanie liczby do listy po zamianie na int

print("Wprowadzone liczby:", liczby)

### Pętla while z blokiem else (else wykona się tylko, jeśli pętla nie zostanie przerwana przez 'break')
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 15:  # Warunek ten nigdy nie będzie spełniony, więc pętla nie przerwie działania
        break
else:
    print("Done")  # Ten blok się wykona, bo pętla zakończy się naturalnie

