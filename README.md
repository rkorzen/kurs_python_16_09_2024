# Kurs Podstaw Pythona

## Organizacja:

Przerwy:

* 10:00-10:15
* 11:45-12:00
* 13:30-13:45

15:15 - koniec zajęć

## ogolna charakterystyka

- typowanie silne i dynamiczne

### 

help - jak czesgos uzywac

help("ala".upper)
help(dir)
help(print)

dir -  stad dowiemy sie co moge zrobic z danym obiektem

dir("ala")

print(dir(__builtins__))  - stad wiemy o wbudowanych funkcjach

## podstawowe polecenia wiersza polecen (cmd)

* cd - change directory

```
    cd nazwa
    cd ..  - wyjscie wyzej
```

* dir - listuje to co jest w katalogu

## Podstawowe typy wbudowane w Pythona

### typ calkowity - int

1 
1231231234541232243123

int()

0b - system binarny
0o - system ósemkowy
0x - system szesntastkowy

1_0_0000_00

bin, hex, oct - przydatne konwersje

### bool - typ logiczny

True, False

### float - liczby zmiennoprzecinkowe

https://docs.python.org/3/tutorial/floatingpoint.html

https://pywaw.org/105/

float(1)
float("1.1")
0.1

- wazna jest swiadomosc precyzji liczb zmiennoprzecinkowych
- notacja naukowa 1e10
- "inf", "-inf", "nan"

decimal.Decimal  (jako alternatywa - tam gdzie to konieczne)

## complex

1 + 1j

## operatory arytmetyczne:

+
*
-
/  -  standardowe dzielenie
// -  dzielenie calkowite
%  -  dzielenie modulo
**
pow()

## operatory porownania

== 
>
<
>=
<=

is

## operatory przypisania

=

x = 1
x += 1  
to samo co
x = x + 1


+=
-=
*=
...

## operatory logiczne

and
or
not

## str (string)- napis 

"to jest napis"
'to jest napis'

str(1)

"""
Ala
ma
kota
"""

''' '''

"Ala\nma\nkota"

\n - znak nowej linii
\t - znak tabulacji
\r - powrot karetki
\a

### Cwiczenie
Utworz zmienne imie i nazwisko. Przypisz do nich swoje dane.
Wypisz na ekranie te dane zamienione na duze litery - w zmiennych maja byc dane z malymi literami
wypisz zlaczone imie i nazwisko
print(x, y)



## Formatowanie napisow

https://pyformat.info/

```python
"1" + "2"
imie = "Rafal"
nazwisko = "Korzeniewski"

dane = "imie: " + imie + " nazwisko: " + nazwisko
print(dane)

```