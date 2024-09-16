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

## Kolekcje

### Napisy

typ niemutowalny - nie da sie zmienic istniejacego napisu

napis = "ala ma kota"

- kolekcja moze miec porzadek (ale nie musi)
- w pythonie indeksujemy od 0

```
 0123456789
"ala ma kot"

literce m odpowiada index 4

napis[4]
napis[9]
napis[-1]
```
### slicing

kolekcja[start*, stop, krok]


## Krotka - tuple

()

krotka = ("A", "l", "a", " ", "k", "o")

krotka = ("napis 1", "napis 2", 10, 20)

osoba = ("Rafał", "Korzniewski", 16, 234.2)

template = "a: {:^6}, b: {:<6}, p: {:12.3f}"

## lista - list
kolekcja mutowalna - mozna zmienia ja - np podmieniac elementy

[]


## zbior - set

mutowalna kolekcja unikalnych obiektow (ktore musza byc hashowalne)

{1, 2, 3}
{2, 3, 4}
set([1, 2, 3])

set() # - pusty zbior a nie {}

## słownik - dict


{} -  pusty slownik
{1: "a", 2: "b"}


## wyrażenia warunkowe

```
if <warunek>:
    <blok instrukcji>

<blok c instrucji>

#################

if <warunek>:
    <blok instrukcji>
else:
    <block b instrukcji>

<blok c instrucji>


######################


if <warunek>:
    <blok instrukcji>
elif <inny warunek>:
    <block b instrukcji>

<blok c instrucji>


#######


if <warunek>:
    <blok instrukcji>
elif <inny warunek>:
    <block b instrukcji>
elif <inny warunek>:
    <block b1 instrukcji>
...
else:
    <block instrukcji ...>
<blok c instrucji>

```

### structural matchin pattern

match:
    case <warunki>:
        ...
    case _:
        ...


### wciecia 

- co do zasady 4 spacje

inny jezyk:
```
if (len(napis) < 15) {
    print(napis); 
    } 
else {
    print(napis[:15]);
    print(napis[15:]);
}
```

```
if len(napis) < 15:
    print(napis)
else:
    print(napis[:15])
    print(napis[15:])
```

## Pętle

### while

```
while <warunek>:
    <blok instrukcji>


while <warunek>:
    <blok instrukcji>
else:
    <blok instrukcji jesli nie bylo przerwania petli>

```

### for

```
for el in kolekcja:
    <blok instrukcji>

```


### zadanie

napisz program, ktory bedzie przyjmowal od uzytkownika liczby (konczy przyjmowanie po wprowadzeniu znaku q).
wypisz takie informacje:

liczb bylo: 22
z czego unikalnych bylo: 2
srednia wynosi: 2.3

len()