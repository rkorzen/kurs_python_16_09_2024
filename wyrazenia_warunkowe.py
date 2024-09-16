napis = "Ala ma kota a kot ma Alę"
napis = "aa"


if len(napis) < 15:
    print(napis)
else:
    print(napis[:15])
    print(napis[15:])
print("Pozwa ifem") 
print("xxx")

print(len(napis) < 15)



x = 1

# x > 0 or x / 0 == 1



if len(napis) < 15:
    print(napis)
else:
    1/0
    print(napis[:15])
    print(napis[15:])
print("Pozwa ifem") 
print("xxx")

x = -1

if x < 0:
    print("mniejszy")
elif x == 0:
    1/0
else:
    print("x wiekszy")


lista = [1, 2]

if len(lista) == 0:
    print("pusta lista")

if not lista:
    print("pusta lista")

# False: 0, 0.0. [], (), {}, ""
# True: rozne od zera badz niepuste


print(bool(2), bool(0), bool(""))

print(1 in lista)

# In: zbior, krotka, lista, napis
# w slowniku - szuka natomiast w kluczach

1 in {1: "a"}
1 in {"a": 1}