# konkatenacja
imie = "Rafal"
nazwisko = "Korzeniewski"

dane = "imie: " + imie + " nazwisko: " + nazwisko
print(dane)

# uzycie operatora %

print("imie: %s nazwisko: %s zaplanowane godziny: %d, stawka: %.2f" % (imie, nazwisko, 16.1, 250))

godziny = 32
stawka = 180.5

# uzycie f-string
print(f"imie: {imie} nazwisko: {nazwisko} zaplanowane godziny: {godziny}, stawka: {stawka:.2f}")

# uzycie metody format

print(
    "imie: {imie2} nazwisko: {nazwisko} zaplanowane godziny: {godziny}, stawka: {stawka:.2f}".format(
        imie2=imie, nazwisko=nazwisko, godziny=godziny, stawka=stawka
    )
)


print(
    "imie: {} nazwisko: {} zaplanowane godziny: {}, stawka: {:.2f}".format(
        imie, nazwisko, godziny, stawka
    )
)



a1 = 10
b1 = 20

a2 = 300
b2 = 250

p1 = a1 * b1
p2 = a2 * b2


template = "a: {:^6}, b: {:<6}, p: {:12.3f}"


print(template.format(a1, b1, p1))
print(template.format(a2, b2, p2))