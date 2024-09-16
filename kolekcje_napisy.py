napis = "Ala ma kota"

# Dostęp do poszczególnych znaków w napisie
print(napis[0])    # Pierwszy znak
print(napis[10])   # Ostatni znak
print(napis[-1])   # Ostatni znak (liczone od końca)
print(napis[-11])  # Pierwszy znak (liczone od końca)

# Wybieranie fragmentów (slicing)
print(napis[3:7])      # Znaki od indeksu 3 do 6
print(napis[1:10:3])   # Co trzeci znak od indeksu 1 do 9
print(napis[0:10:3])   # Co trzeci znak od indeksu 0 do 9
print(napis[:10:3])    # To samo co powyżej, gdyż domyślnie początek to indeks 0

print(napis[3:11:3])   # Co trzeci znak od indeksu 3 do końca
print(napis[3::3])     # To samo, co powyżej
print(napis[0:11:3])   # Co trzeci znak od początku do końca
print(napis[::3])      # To samo, co powyżej

# Odwracanie napisu
print(napis[::-1])     # Odwrócenie kolejności znaków

# Sprawdzanie indeksu znaku 't'
print(napis.index('t'))  # Zwraca indeks pierwszego wystąpienia litery 't'

# Próba modyfikacji znaku (niemutowalne),
# napis[9] = "T"