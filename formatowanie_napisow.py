# Konkatenacja łańcuchów znaków
imie = "Rafal"
nazwisko = "Korzeniewski"

dane = "imie: " + imie + " nazwisko: " + nazwisko
print(dane)

# Użycie operatora % do formatowania ciągów znaków
print("imie: %s nazwisko: %s zaplanowane godziny: %d, stawka: %.2f" % (imie, nazwisko, 16.1, 250))

# Zmienna dla godzin i stawki
godziny = 32
stawka = 180.5

# Użycie f-stringów (wprowadzone w Pythonie 3.6) - nowoczesny sposób formatowania
print(f"imie: {imie} nazwisko: {nazwisko} zaplanowane godziny: {godziny}, stawka: {stawka:.2f}")

# Użycie metody format() z nazwanymi parametrami
print(
    "imie: {imie2} nazwisko: {nazwisko} zaplanowane godziny: {godziny}, stawka: {stawka:.2f}".format(
        imie2=imie, nazwisko=nazwisko, godziny=godziny, stawka=stawka
    )
)

# Użycie metody format() bez nazwanych parametrów
print(
    "imie: {} nazwisko: {} zaplanowane godziny: {}, stawka: {:.2f}".format(
        imie, nazwisko, godziny, stawka
    )
)

# Obliczenia dla przykładu z powierzchniami
a1 = 10
b1 = 20
a2 = 300
b2 = 250

# Obliczenia powierzchni
p1 = a1 * b1
p2 = a2 * b2

# Szablon formatowania - wyrównywanie, szerokość pól, precyzja
template = "a: {:^6}, b: {:<6}, p: {:12.3f}"

# Formatowanie i wyświetlanie wyników obliczeń dla a1, b1, p1
print(template.format(a1, b1, p1))

# Formatowanie i wyświetlanie wyników obliczeń dla a2, b2, p2
print(template.format(a2, b2, p2))
