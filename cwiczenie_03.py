"""
napisz program, ktory bedzie przyjmowal od uzytkownika liczby (konczy przyjmowanie po wprowadzeniu znaku q).
wypisz takie informacje:

liczb bylo: 22
z czego unikalnych bylo: 2
srednia wynosi: 2.3

len()
"""

liczby = []

while True:
    s = input("Podaj liczbe lub wpisz q by zakonczyc: ")
    if s == "q":
        break
    liczby.append(int(s))

suma = 0

for liczba in liczby:
    suma += liczba

print(
f"""
liczb bylo: {len(liczby)}
z czego unikalnych bylo: {len(set(liczby))}
srednia wynosi: {suma/len(liczby)}    
"""
)