# Kurs Podstaw Pythona

## Organizacja

Przerwy:

- 10:00-10:15
- 11:45-12:00
- 13:30-13:45

15:15 - koniec zajęć

Oto uzupełniona wersja sekcji o ogólnej charakterystyce Pythona:

---

## Ogólna charakterystyka

- Python ma **silne** i **dynamiczne** typowanie. Oznacza to, że typy zmiennych są określane w czasie wykonywania programu (dynamiczne typowanie), co sprawia, że nie trzeba jawnie deklarować typów zmiennych przy ich tworzeniu. Typ zmiennej jest automatycznie przypisywany na podstawie wartości, która do niej trafiła.
  
- **Silne typowanie** oznacza, że Python nie pozwala na niejawne konwersje między typami. Na przykład, nie można dodać liczby do napisu bez wcześniejszej konwersji liczby na napis lub odwrotnie:

```python
x = "5"
y = 10
print(x + y)  # Błąd: nie można dodać napisu do liczby
```

  Aby wykonać tę operację, należy jawnie skonwertować typ:

```python
print(int(x) + y)  # Konwersja napisu na liczbę
```

- Python jest językiem **interpretowanym**. Kod Pythona jest wykonywany linia po linii przez interpreter, co oznacza, że programy są uruchamiane bez konieczności wcześniejszej kompilacji. Dzięki temu łatwiej jest testować i debugować programy, jednak może to wpływać na ich szybkość w porównaniu do języków kompilowanych.

- Python jest językiem **wysokopoziomowym**, co oznacza, że zapewnia abstrakcję nad operacjami niskopoziomowymi, takimi jak zarządzanie pamięcią. Programiści nie muszą martwić się o szczegóły sprzętowe, co ułatwia pisanie zrozumiałego i czytelnego kodu.

- Python obsługuje **paradygmaty programowania obiektowego**, **funkcyjnego** i **imperatywnego**, co daje programistom elastyczność w wyborze stylu programowania.

- Python ma **bogatą bibliotekę standardową** (ang. *batteries included*), co oznacza, że zawiera szeroki zestaw modułów i funkcji, które można używać od razu, bez konieczności instalowania dodatkowych bibliotek. Dzięki temu można szybko pisać zaawansowane programy bez potrzeby zewnętrznych narzędzi.




### Pomoc w Pythonie:

- **help()** – funkcja, która wyświetla dokumentację dotyczącą funkcji, metod, klas, modułów oraz obiektów. Jest bardzo przydatna, gdy chcemy dowiedzieć się, jak działa dana funkcja lub jakiej składni oczekuje. W przypadku nieznanej funkcji lub modułu, możemy skorzystać z:

```python
help(obiekt)
```

  Przykłady:

```python
help("ala".upper)  # Pomoc dotycząca metody upper dla obiektu string
help(dir)          # Pomoc dotycząca funkcji dir
help(print)        # Pomoc dotycząca funkcji print
help(list)         # Dokumentacja dotycząca typu list
```

  Można także uzyskać pomoc na poziomie modułów lub pakietów:

```python
import math
help(math)  # Informacje o funkcjach dostępnych w module math
```

- **dir()** – zwraca listę dostępnych atrybutów i metod dla danego obiektu. Można używać tej funkcji, aby sprawdzić, jakie operacje można wykonać na konkretnym obiekcie lub jakie są jego dostępne atrybuty. Jest to szczególnie przydatne, gdy pracujemy z obiektami, których nie znamy dokładnie.

  Przykłady:

```python
dir("ala")  # Zwraca metody dostępne dla obiektu typu string
dir(list)   # Zwraca metody dostępne dla list
dir(math)   # Zwraca funkcje dostępne w module math
```

  Używając `dir()`, można łatwo odkryć, jakie atrybuty i metody są dostępne dla dowolnego obiektu w Pythonie, co jest bardzo pomocne podczas programowania i eksplorowania kodu.

- **print(dir(__builtins__))** – wypisuje wszystkie wbudowane funkcje i zmienne dostępne w Pythonie bez konieczności importowania dodatkowych modułów. Wbudowane funkcje to takie, jak `print()`, `len()`, `range()`, `sum()` itp.

  Przykład:

```python
print(dir(__builtins__))  # Zwraca listę wszystkich wbudowanych funkcji i obiektów
```

  To narzędzie pozwala łatwo zidentyfikować wszystkie funkcje, które są dostępne natychmiast w Pythonie, bez potrzeby ich importowania z zewnętrznych modułów.

- **help(module)** – dla modułów lub bibliotek zewnętrznych, takich jak numpy czy pandas, funkcja `help()` także działa, pokazując dostępne klasy, funkcje i moduły.

  Przykład:

```python
import numpy
help(numpy)  # Zwraca dokumentację dotyczącą biblioteki numpy
```

  Można również użyć `help()` do zrozumienia konkretnych funkcji lub klas w danym module:

```python
help(numpy.array)  # Pomoc dotycząca funkcji numpy.array
```

- **docstring** – każda funkcja w Pythonie może posiadać dokumentację (docstring), którą można odczytać za pomocą funkcji `help()` lub bezpośrednio odwołując się do atrybutu `__doc__`.

  Przykład:

```python
print(str.upper.__doc__)  # Wydruk docstringa dla metody upper
```


## Podstawowe polecenia wiersza poleceń (cmd)

- **cd** – zmiana katalogu:

  ```bash
  cd nazwa_katalogu  # Przejście do określonego katalogu
  cd ..              # Powrót do katalogu wyżej
  ```

- **dir (w Windows)** lub **ls (w Linux/Mac)** – listowanie zawartości katalogu:

  ```bash
  dir    # Wyświetlenie zawartości katalogu w systemie Windows
  ls     # Wyświetlenie zawartości katalogu w systemie Linux/Mac
  ```

- **mkdir** – tworzenie nowego katalogu:

  ```bash
  mkdir nowy_katalog  # Tworzy nowy katalog o nazwie 'nowy_katalog'
  ```

- **rmdir** – usuwanie pustego katalogu:

  ```bash
  rmdir katalog  # Usuwa pusty katalog
  ```

- **del (w Windows)** lub **rm (w Linux/Mac)** – usuwanie plików:

  ```bash
  del plik.txt  # Usuwa plik w systemie Windows
  rm plik.txt   # Usuwa plik w systemie Linux/Mac
  ```

- **cls (w Windows)** lub **clear (w Linux/Mac)** – czyszczenie ekranu:

  ```bash
  cls     # Czyszczenie ekranu w systemie Windows
  clear   # Czyszczenie ekranu w systemie Linux/Mac
  ```


## Podstawowe typy wbudowane w Pythona

### Liczby całkowite – int

Liczby całkowite w Pythonie są reprezentowane przez typ `int`, który obsługuje zarówno małe, jak i bardzo duże liczby. Python automatycznie dostosowuje rozmiar liczby całkowitej w zależności od jej wartości, co oznacza, że liczby mogą być niemal nieograniczonej wielkości (z wyjątkiem ograniczeń pamięci systemowej).

Przykłady liczb całkowitych:

```python
1
0
-123
1231231234541232243123  # Python obsługuje bardzo duże liczby całkowite
```

#### Tworzenie liczb całkowitych

Liczby całkowite można tworzyć bezpośrednio lub za pomocą funkcji `int()`:

```python
int(5)           # Zwraca liczbę całkowitą 5
int("123")       # Konwersja napisu na liczbę całkowitą
int(4.7)         # Konwersja liczby zmiennoprzecinkowej na liczbę całkowitą (tracimy część po przecinku)
int("0b1010", 2) # Konwersja liczby zapisanej w systemie binarnym (jako napis) na int
```

#### Systemy liczbowe

Python obsługuje różne systemy liczbowe i umożliwia konwersję pomiędzy nimi za pomocą wbudowanych funkcji:

- **0b** – liczby binarne (system dwójkowy)
- **0o** – liczby ósemkowe (system ósemkowy)
- **0x** – liczby szesnastkowe (system szesnastkowy)

Przykłady:

```python
bin(10)    # '0b1010' – zapis liczby 10 w systemie binarnym
hex(255)   # '0xff' – zapis liczby 255 w systemie szesnastkowym
oct(8)     # '0o10' – zapis liczby 8 w systemie ósemkowym
```

Liczby można również bezpośrednio zapisywać w tych systemach, używając odpowiednich prefiksów:

```python
0b1010  # Liczba binarna (10 w systemie dziesiętnym)
0o12    # Liczba ósemkowa (10 w systemie dziesiętnym)
0xff    # Liczba szesnastkowa (255 w systemie dziesiętnym)
```

#### Czytelność liczb

Python pozwala na używanie podkreślników w liczbach, co poprawia ich czytelność, szczególnie w przypadku dużych liczb. Podkreślniki nie wpływają na wartość liczby.

```python
1_000_000       # Odpowiada liczbie 1000000, ale jest bardziej czytelne
123_456_789_012 # Liczba z podkreślnikami dla lepszej czytelności
```

#### Funkcje pomocnicze do pracy z liczbami całkowitymi

Python oferuje kilka wbudowanych funkcji, które ułatwiają pracę z liczbami całkowitymi:

- **abs()** – zwraca wartość absolutną liczby:

  ```python
  abs(-5)  # 5
  ```

- **pow()** – zwraca wynik potęgowania:

  ```python
  pow(2, 3)  # 2^3 = 8
  pow(2, 3, 5)  # (2^3) % 5 = 3
  ```

- **divmod()** – zwraca krotkę zawierającą wynik dzielenia całkowitego i reszty:

  ```python
  divmod(17, 3)  # (5, 2) – dzielenie 17 przez 3: wynik to 5, reszta to 2
  ```

#### Operacje na liczbach całkowitych

Liczby całkowite obsługują standardowe operatory arytmetyczne, takie jak dodawanie, odejmowanie, mnożenie, dzielenie i inne:

- **Dodawanie (+)**:

  ```python
  10 + 5  # 15
  ```

- **Odejmowanie (-)**:

  ```python
  10 - 5  # 5
  ```

- **Mnożenie (*)**:

  ```python
  10 * 5  # 50
  ```

- **Dzielenie (/)**:

  ```python
  10 / 3  # 3.333... – wynik jest liczbą zmiennoprzecinkową
  ```

- **Dzielenie całkowite (//)**:

  ```python
  10 // 3  # 3 – wynik dzielenia całkowitego
  ```

- **Reszta z dzielenia (%)**:

  ```python
  10 % 3  # 1 – reszta z dzielenia 10 przez 3
  ```

- **Potęgowanie (**)**:

  ```python
  2 ** 3  # 8 – 2 do potęgi 3
  ```

Python automatycznie konwertuje wynik operacji, jeżeli jest to konieczne, np. operacje na dużych liczbach nie powodują przepełnienia, co jest dużą zaletą w porównaniu z niektórymi innymi językami programowania.



### Typ logiczny – bool

Typ logiczny `bool` w Pythonie reprezentuje wartości logiczne, które mogą przyjmować jedną z dwóch możliwych wartości:

- **True** – odpowiada prawdzie.
- **False** – odpowiada fałszowi.

Przykłady:

```python
True
False
```

#### Relacja z typem `int`

Typ logiczny `bool` w Pythonie jest w rzeczywistości szczególnym przypadkiem typu całkowitego (`int`). Oznacza to, że wartości logiczne `True` i `False` są związane odpowiednio z liczbami `1` i `0`. Można to zweryfikować, wykonując proste operacje arytmetyczne na wartościach logicznych:

```python
int(True)   # Zwraca 1
int(False)  # Zwraca 0
```

Z drugiej strony, każda liczba całkowita w Pythonie może zostać przekonwertowana na wartość logiczną za pomocą funkcji `bool()`:

- Liczba **0** zawsze zwraca **False**.
- Wszystkie inne liczby (zarówno dodatnie, jak i ujemne) zwracają **True**.

Przykłady:

```python
bool(0)    # False
bool(1)    # True
bool(-1)   # True
bool(100)  # True
```

Relacja między `bool` a `int` umożliwia także wykonywanie operacji arytmetycznych na wartościach logicznych:

```python
True + True   # 2, bo True = 1
True * False  # 0, bo False = 0
False - True  # -1, bo False = 0, a True = 1
```

#### Wartości logiczne w kontekście operacji i warunków

Typ `bool` jest najczęściej używany w kontekście wyrażeń warunkowych i instrukcji sterujących. Operatorzy porównania zwracają wartości logiczne, co umożliwia kontrolowanie przepływu programu:

```python
a = 5
b = 10

result = a < b  # True, bo 5 jest mniejsze niż 10
```

Wartości logiczne są także kluczowe w pętlach i instrukcjach warunkowych:

```python
if True:
    print("To się zawsze wykona")

if False:
    print("To się nigdy nie wykona")
```

#### Operacje logiczne

Python obsługuje standardowe operatory logiczne, które zwracają wartości typu `bool`:

- **and** – zwraca **True**, jeśli oba operandy są prawdziwe.
  
  ```python
  True and True    # True
  True and False   # False
  ```

- **or** – zwraca **True**, jeśli przynajmniej jeden z operandów jest prawdziwy.

  ```python
  True or False    # True
  False or False   # False
  ```

- **not** – zwraca negację wartości logicznej.

  ```python
  not True         # False
  not False        # True
  ```

#### Wartości "prawdziwe" i "fałszywe" innych typów

W Pythonie różne typy danych mogą być interpretowane jako wartości logiczne. Ogólna zasada jest taka, że wartości "puste" (jak `0`, pusty ciąg znaków, lista, krotka, czy `None`) są uznawane za **False**, a wszystkie inne wartości są traktowane jako **True**:

- **False**: `None`, `0`, `0.0`, `''` (pusty ciąg), `[]` (pusta lista), `{}` (pusty słownik), `set()`.
- **True**: Wszystkie inne wartości.

Przykłady:

```python
bool("")     # False, pusty string
bool([1, 2]) # True, lista nie jest pusta
bool(0)      # False, liczba 0
bool(3.14)   # True, liczba zmiennoprzecinkowa
```

### Liczby zmiennoprzecinkowe – float

https://docs.python.org/3/tutorial/floatingpoint.html

https://pywaw.org/105/


Liczby zmiennoprzecinkowe w Pythonie są reprezentowane przez typ `float`. Służą do przechowywania liczb rzeczywistych z częścią ułamkową, czyli takich, które nie są liczbami całkowitymi. Typ `float` jest implementowany zgodnie ze standardem IEEE 754 dla liczb zmiennoprzecinkowych podwójnej precyzji (64 bity).

#### Tworzenie liczb zmiennoprzecinkowych

Liczby zmiennoprzecinkowe można tworzyć na kilka sposobów:

- **Bezpośrednie przypisanie liczby z częścią dziesiętną**:

  ```python
  0.1
  3.14
  -2.5
  ```

- **Użycie funkcji `float()` do konwersji z innych typów**:

  ```python
  float(1)          # Konwersja liczby całkowitej na zmiennoprzecinkową: 1.0
  float("1.1")      # Konwersja napisu na liczbę zmiennoprzecinkową: 1.1
  float("nan")      # Specjalna wartość 'Not a Number'
  float("inf")      # Nieskończoność
  ```

- **Użycie notacji naukowej (wykładniczej)**:

  ```python
  1e10     # 1 * 10^10 = 10000000000.0
  2.5e-4   # 2.5 * 10^-4 = 0.00025
  ```

#### Ograniczenia precyzji liczb zmiennoprzecinkowych

Ważne jest zrozumienie, że liczby zmiennoprzecinkowe nie mogą reprezentować wszystkich liczb rzeczywistych z nieskończoną dokładnością. Ze względu na sposób przechowywania w postaci binarnej, wiele liczb dziesiętnych jest reprezentowanych tylko w przybliżeniu, co może prowadzić do nieoczekiwanych rezultatów w obliczeniach:

```python
0.1 + 0.2  # Oczekiwane: 0.3, rzeczywiste: 0.30000000000000004
```

Jest to spowodowane tym, że liczby takie jak 0.1 czy 0.2 nie mają dokładnej reprezentacji w systemie binarnym z użyciem skończonej liczby bitów.

#### Specjalne wartości

Python obsługuje specjalne wartości typu `float`, które są użyteczne w różnych kontekstach:

- **Nieskończoność**:

  ```python
  float('inf')     # Reprezentuje nieskończoność
  float('-inf')    # Reprezentuje minus nieskończoność
  ```

  Nieskończoność zachowuje się zgodnie z oczekiwaniami w operacjach arytmetycznych:

  ```python
  float('inf') + 1000       # inf
  float('-inf') * 2         # -inf
  float('inf') - float('inf')  # nan (nieokreślone)
  ```

- **Not-a-Number (NaN)**:

  ```python
  float('nan')  # Reprezentuje wartość nieokreśloną lub nieistniejącą
  ```

  Wartość `nan` ma unikalne właściwości:

  - `nan` **nie jest równe żadnej wartości, nawet sobie samemu**:

    ```python
    float('nan') == float('nan')  # False
    math.isnan(float('nan'))      # True
    ```

#### Operacje na liczbach zmiennoprzecinkowych

Liczby zmiennoprzecinkowe obsługują standardowe operatory arytmetyczne:

- **Dodawanie (+)**:

  ```python
  0.1 + 0.2  # 0.30000000000000004
  ```

- **Odejmowanie (-)**:

  ```python
  5.5 - 2.2  # 3.3
  ```

- **Mnożenie (*)**:

  ```python
  2.0 * 3.5  # 7.0
  ```

- **Dzielenie (/)**:

  ```python
  7.0 / 2.0  # 3.5
  ```

- **Potęgowanie (**)**:

  ```python
  2.0 ** 3  # 8.0
  ```

#### Funkcje matematyczne

Python oferuje moduł `math`, który zawiera wiele funkcji matematycznych działających na liczbach zmiennoprzecinkowych:

```python
import math

math.sqrt(16)           # 4.0
math.sin(math.pi / 2)   # 1.0
math.log(1024, 2)       # 10.0
```

#### Notacja naukowa

Liczby zmiennoprzecinkowe mogą być reprezentowane w notacji naukowej (wykładniczej), co jest szczególnie przydatne dla bardzo dużych lub bardzo małych liczb:

```python
1e10     # 1 * 10^10 = 10000000000.0
3.5e-4   # 3.5 * 10^-4 = 0.00035
```

#### Problemy z precyzją

Ze względu na ograniczenia w reprezentacji binarnej, niektóre operacje arytmetyczne mogą dawać niespodziewane wyniki:

```python
0.1 + 0.2 == 0.3   # False
```

Aby porównywać liczby zmiennoprzecinkowe z uwzględnieniem tolerancji, można użyć funkcji `math.isclose()`:

```python
import math

math.isclose(0.1 + 0.2, 0.3)  # True
```

#### Moduł `decimal` dla większej precyzji

Jeśli potrzebna jest większa precyzja obliczeń zmiennoprzecinkowych, można skorzystać z modułu `decimal`, który pozwala na pracę z liczbami dziesiętnymi o arbitralnej precyzji:

```python
from decimal import Decimal, getcontext

getcontext().prec = 28  # Ustawienie precyzji na 28 miejsc po przecinku

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b

print(c)  # 0.3
```

Moduł `decimal` jest szczególnie przydatny w finansach i innych dziedzinach, gdzie precyzja jest kluczowa.

#### Moduł `fractions` dla liczb wymiernych

Alternatywnie, dla dokładnego przedstawienia liczb wymiernych można użyć modułu `fractions`, który pozwala na operacje na ułamkach:

```python
from fractions import Fraction

a = Fraction(1, 3)
b = Fraction(2, 3)
c = a + b

print(c)       # 1
print(float(c))  # 1.0
```

#### Konwersja typów

Konwersja pomiędzy typami liczbowymi jest prosta i odbywa się za pomocą funkcji wbudowanych:

- **Konwersja na `float`**:

  ```python
  float(10)         # 10.0
  float('3.14')     # 3.14
  ```

- **Konwersja z `float` na `int`** (traci część ułamkową):

  ```python
  int(3.99)       # 3
  int(-3.99)      # -3
  ```

#### Reprezentacja liczby zmiennoprzecinkowej jako ciągu znaków

Gdy liczba zmiennoprzecinkowa jest konwertowana na ciąg znaków, może to prowadzić do długich rozwinięć dziesiętnych:

```python
str(0.1)   # '0.1'
repr(0.1)  # '0.1'
```

Jednak przy obliczeniach wyniki mogą być zaskakujące:

```python
print(0.1 + 0.2)     # 0.30000000000000004
print(str(0.1 + 0.2))  # '0.30000000000000004'
```

#### Zaokrąglanie liczb zmiennoprzecinkowych

Do zaokrąglania liczb zmiennoprzecinkowych można użyć funkcji `round()`:

```python
round(3.14159, 2)  # 3.14
round(2.675, 2)    # 2.67 (uwaga na ograniczenia precyzji binarnej)
```

#### Porównywanie liczb zmiennoprzecinkowych

Z powodu problemów z precyzją, bezpośrednie porównywanie liczb zmiennoprzecinkowych może być niebezpieczne. Zamiast tego, należy sprawdzać, czy różnica między liczbami jest mniejsza od określonej tolerancji:

```python
abs(a - b) < 1e-9
```

Lub używać funkcji `math.isclose()` z odpowiednimi parametrami:

```python
import math

math.isclose(a, b, rel_tol=1e-9)
```

#### Podsumowanie

- **Typ `float`** służy do reprezentowania liczb rzeczywistych z częścią ułamkową.
- **Ograniczenia precyzji** wynikają z reprezentacji binarnej liczb zmiennoprzecinkowych.
- **Specjalne wartości** takie jak `inf`, `-inf` i `nan` są obsługiwane.
- **Moduł `decimal`** pozwala na dokładniejsze obliczenia zmiennoprzecinkowe.
- **Moduł `fractions`** umożliwia operacje na liczbach wymiernych bez utraty precyzji.
- **Porównywanie liczb zmiennoprzecinkowych** powinno uwzględniać tolerancję błędu.

#### Przykładowe zastosowanie

```python
from decimal import Decimal, getcontext

# Ustawienie precyzji
getcontext().prec = 10

# Obliczenia z użyciem Decimal
a = Decimal('1.23456789')
b = Decimal('0.00000001')
c = a + b

print(c)  # 1.23456790
```

Używając odpowiednich typów i modułów, można w Pythonie dokładnie i efektywnie pracować z liczbami zmiennoprzecinkowymi.

### Liczby zespolone – `complex`

Liczby zespolone w Pythonie są reprezentowane przez typ `complex`. Liczba zespolona składa się z części rzeczywistej i części urojonej, które są liczbami zmiennoprzecinkowymi (`float`). W matematyce liczba zespolona jest zapisywana w postaci \( a + bi \), gdzie:

- \( a \) – część rzeczywista,
- \( b \) – część urojona,
- \( i \) – jednostka urojona (\( i^2 = -1 \)).

W Pythonie część urojona jest oznaczana przez sufiks `j` lub `J`.

#### Tworzenie liczb zespolonych

**Bezpośrednie przypisanie**:

```python
z = 1 + 2j         # Liczba zespolona z częścią rzeczywistą 1 i urojoną 2
z = -3.5 + 4j      # Liczba zespolona z częścią rzeczywistą -3.5 i urojoną 4
z = 0 + 1j         # Jednostka urojona
z = 5j             # Liczba czysto urojona z częścią rzeczywistą 0
```

**Użycie funkcji `complex()`**:

```python
z = complex(1, 2)        # Tworzy liczbę 1 + 2j
z = complex(-3.5, 4)     # Tworzy liczbę -3.5 + 4j
z = complex(5)           # Tworzy liczbę 5 + 0j
z = complex("3+4j")      # Tworzy liczbę 3 + 4j z napisu
```

#### Dostęp do części rzeczywistej i urojonej

Można uzyskać dostęp do części rzeczywistej i urojonej liczby zespolonej za pomocą atrybutów `real` i `imag`:

```python
z = 1 + 2j
print(z.real)  # Wyjście: 1.0
print(z.imag)  # Wyjście: 2.0
```

#### Operacje arytmetyczne na liczbach zespolonych

Liczby zespolone obsługują standardowe operatory arytmetyczne:

- **Dodawanie (+)**:

  ```python
  z1 = 1 + 2j
  z2 = 3 + 4j
  wynik = z1 + z2  # Wynik: (4+6j)
  ```

- **Odejmowanie (-)**:

  ```python
  wynik = z1 - z2  # Wynik: (-2-2j)
  ```

- **Mnożenie (*)**:

  ```python
  wynik = z1 * z2  # Wynik: (-5+10j)
  ```

- **Dzielenie (/)**:

  ```python
  wynik = z1 / z2  # Wynik: (0.44+0.08j)
  ```

- **Potęgowanie (**)**:

  ```python
  wynik = z1 ** 2  # Wynik: (-3+4j)
  ```

#### Moduł i argument liczby zespolonej

- **Moduł** (wartość bezwzględna) liczby zespolonej:

  ```python
  z = 3 + 4j
  modul = abs(z)  # Wynik: 5.0
  ```

- **Argument** (faza) liczby zespolonej:

  ```python
  import cmath

  z = 1 + 1j
  argument = cmath.phase(z)  # Wynik: 0.7853981633974483 (radiany)
  ```

#### Konwersja z postaci trygonometrycznej na algebraiczną i odwrotnie

- **Z postaci algebraicznej do trygonometrycznej**:

  ```python
  r = abs(z)                  # Moduł
  theta = cmath.phase(z)      # Argument w radianach
  ```

- **Z postaci trygonometrycznej do algebraicznej**:

  ```python
  z = cmath.rect(r, theta)    # Odtworzenie liczby zespolonej
  ```

Przykład:

```python
import cmath

r = 2
theta = cmath.pi / 4  # 45 stopni w radianach

z = cmath.rect(r, theta)
print(z)  # Wynik: (1.4142135623730951+1.414213562373095j)
```

#### Funkcje matematyczne dla liczb zespolonych

Moduł `cmath` zawiera funkcje matematyczne działające na liczbach zespolonych:

- **Pierwiastek kwadratowy**:

  ```python
  import cmath

  z = -1
  wynik = cmath.sqrt(z)  # Wynik: 1j
  ```

- **Funkcje wykładnicze i logarytmiczne**:

  ```python
  wynik_exp = cmath.exp(z)    # e^(z)
  wynik_log = cmath.log(z)    # Logarytm naturalny
  ```

- **Funkcje trygonometryczne**:

  ```python
  wynik_sin = cmath.sin(z)
  wynik_cos = cmath.cos(z)
  wynik_tan = cmath.tan(z)
  ```

- **Funkcje hiperboliczne**:

  ```python
  wynik_sinh = cmath.sinh(z)
  wynik_cosh = cmath.cosh(z)
  wynik_tanh = cmath.tanh(z)
  ```

#### Porównywanie liczb zespolonych

- **Równość**:

  ```python
  z1 = 1 + 2j
  z2 = 1 + 2j
  print(z1 == z2)  # True
  ```

- **Brak możliwości użycia operatorów porównania**:

  Operatorów `<`, `>`, `<=`, `>=` nie można stosować do liczb zespolonych; próba ich użycia spowoduje błąd `TypeError`.

#### Konwersja i rzutowanie

- **Nie można bezpośrednio konwertować liczby zespolonej na `int` lub `float`**:

  ```python
  z = 1 + 2j
  # int(z)    # TypeError
  # float(z)  # TypeError
  ```

- **Konwersja części rzeczywistej lub urojonej**:

  ```python
  z = 1 + 2j
  real_part = int(z.real)     # 1
  imag_part = float(z.imag)   # 2.0
  ```

#### Zastosowania praktyczne

- **Rozwiązywanie równań kwadratowych z deltą ujemną**:

  ```python
  import cmath

  a = 1
  b = 2
  c = 5

  delta = b**2 - 4*a*c  # Delta: -16
  sqrt_delta = cmath.sqrt(delta)

  x1 = (-b + sqrt_delta) / (2*a)
  x2 = (-b - sqrt_delta) / (2*a)

  print(f"x1 = {x1}")  # x1 = (-1+2j)
  print(f"x2 = {x2}")  # x2 = (-1-2j)
  ```

- **Analiza sygnałów i obwodów elektrycznych**:

  Liczby zespolone są używane do reprezentacji impedancji w obwodach prądu zmiennego.

#### Ważne uwagi

- **Części rzeczywista i urojona są typu `float`**:

  ```python
  z = 1 + 2j
  type(z.real)  # <class 'float'>
  type(z.imag)  # <class 'float'>
  ```

- **Reprezentacja tekstowa**:

  ```python
  z = 1 + 2j
  print(z)        # (1+2j)
  print(str(z))   # (1+2j)
  print(repr(z))  # (1+2j)
  ```

#### Podsumowanie

- **Typ `complex`** służy do reprezentacji liczb zespolonych w Pythonie.
- **Operacje arytmetyczne** działają podobnie jak dla innych typów liczbowych.
- **Moduł `cmath`** dostarcza funkcji matematycznych dla liczb zespolonych.
- **Części rzeczywista i urojona** są dostępne poprzez atrybuty `real` i `imag`.
- **Konwersja na inne typy** wymaga dostępu do poszczególnych części liczby zespolonej.
- **Porównywanie** jest ograniczone do sprawdzania równości; nie można używać operatorów `>`, `<`, `>=`, `<=`.


## Operatory arytmetyczne

Operatory arytmetyczne w Pythonie służą do wykonywania podstawowych operacji matematycznych na liczbach (zarówno całkowitych, jak i zmiennoprzecinkowych).

### Dodawanie (`+`)

- **Opis**: Sumuje dwie liczby.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a + b  # wynik = 8
  ```

### Odejmowanie (`-`)

- **Opis**: Odejmuje jedną liczbę od drugiej.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a - b  # wynik = 2
  ```

### Mnożenie (`*`)

- **Opis**: Mnoży dwie liczby.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a * b  # wynik = 15
  ```

### Dzielenie (`/`)

- **Opis**: Dzieli jedną liczbę przez drugą. Zawsze zwraca wynik zmiennoprzecinkowy.
- **Przykład**:

  ```python
  a = 5
  b = 2
  wynik = a / b  # wynik = 2.5
  ```

### Dzielenie całkowite (`//`)

- **Opis**: Dzieli jedną liczbę przez drugą, zwracając część całkowitą wyniku (zaokrągloną w dół do najbliższej liczby całkowitej).
- **Przykład**:

  ```python
  a = 5
  b = 2
  wynik = a // b  # wynik = 2
  ```

  Uwaga: Dla liczb ujemnych zaokrąglenie jest w kierunku minus nieskończoności.

  ```python
  a = -5
  b = 2
  wynik = a // b  # wynik = -3
  ```

### Reszta z dzielenia (modulo) (`%`)

- **Opis**: Zwraca resztę z dzielenia dwóch liczb.
- **Przykład**:

  ```python
  a = 5
  b = 2
  wynik = a % b  # wynik = 1
  ```

  Użyteczne w sprawdzaniu podzielności liczb:

  ```python
  if liczba % 2 == 0:
      print("Liczba jest parzysta")
  else:
      print("Liczba jest nieparzysta")
  ```

### Potęgowanie (`**`)

- **Opis**: Podnosi liczbę do potęgi.
- **Przykład**:

  ```python
  a = 2
  b = 3
  wynik = a ** b  # wynik = 8
  ```

- **Alternatywa**: Funkcja `pow()`

  ```python
  wynik = pow(2, 3)  # wynik = 8
  ```

  Funkcja `pow()` ma również trzeci opcjonalny argument, który zwraca wynik modulo:

  ```python
  wynik = pow(2, 3, 5)  # wynik = 3, ponieważ 2**3 % 5 = 8 % 5 = 3
  ```

### Operator unarny `-`

- **Opis**: Zmienia znak liczby.
- **Przykład**:

  ```python
  a = 5
  b = -a  # b = -5
  ```

---

## Operatory porównania

Operatory porównania służą do porównywania wartości dwóch operandów i zwracają wartość logiczną `True` lub `False`.

### Równość (`==`)

- **Opis**: Sprawdza, czy wartości dwóch operandów są równe.
- **Przykład**:

  ```python
  a = 5
  b = 5
  wynik = a == b  # wynik = True
  ```

### Różność (`!=`)

- **Opis**: Sprawdza, czy wartości dwóch operandów są różne.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a != b  # wynik = True
  ```

### Większe niż (`>`)

- **Opis**: Sprawdza, czy lewy operand jest większy od prawego.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a > b  # wynik = True
  ```

### Mniejsze niż (`<`)

- **Opis**: Sprawdza, czy lewy operand jest mniejszy od prawego.
- **Przykład**:

  ```python
  a = 5
  b = 3
  wynik = a < b  # wynik = False
  ```

### Większe lub równe (`>=`)

- **Opis**: Sprawdza, czy lewy operand jest większy lub równy prawemu.
- **Przykład**:

  ```python
  a = 5
  b = 5
  wynik = a >= b  # wynik = True
  ```

### Mniejsze lub równe (`<=`)

- **Opis**: Sprawdza, czy lewy operand jest mniejszy lub równy prawemu.
- **Przykład**:

  ```python
  a = 3
  b = 5
  wynik = a <= b  # wynik = True
  ```

### Operator tożsamości (`is`)

- **Opis**: Sprawdza, czy dwa obiekty są tym samym obiektem w pamięci (mają ten sam identyfikator).
- **Przykład**:

  ```python
  a = [1, 2, 3]
  b = a
  c = [1, 2, 3]
  print(a is b)  # True, ponieważ b odnosi się do tego samego obiektu co a
  print(a is c)  # False, ponieważ c jest innym obiektem z taką samą zawartością
  ```

- **Uwaga**: Operator `is` nie powinien być używany do porównywania wartości. Do tego służy operator `==`.

### Operator braku tożsamości (`is not`)

- **Opis**: Sprawdza, czy dwa obiekty nie są tym samym obiektem.
- **Przykład**:

  ```python
  print(a is not c)  # True
  ```

---

## Operatory przypisania

Operatory przypisania są używane do przypisywania wartości do zmiennych. Oprócz podstawowego operatora `=`, Python oferuje rozszerzone operatory przypisania, które łączą operację arytmetyczną z przypisaniem.

### Podstawowe przypisanie (`=`)

- **Opis**: Przypisuje wartość do zmiennej.
- **Przykład**:

  ```python
  x = 10
  ```

### Dodawanie i przypisanie (`+=`)

- **Opis**: Dodaje wartość prawego operandu do zmiennej i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x += 3  # x = x + 3, więc x = 8
  ```

### Odejmowanie i przypisanie (`-=`)

- **Opis**: Odejmuje wartość prawego operandu od zmiennej i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x -= 2  # x = x - 2, więc x = 3
  ```

### Mnożenie i przypisanie (`*=`)

- **Opis**: Mnoży zmienną przez wartość prawego operandu i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x *= 2  # x = x * 2, więc x = 10
  ```

### Dzielenie i przypisanie (`/=`)

- **Opis**: Dzieli zmienną przez wartość prawego operandu i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x /= 2  # x = x / 2, więc x = 2.5
  ```

### Dzielenie całkowite i przypisanie (`//=`)

- **Opis**: Dzieli zmienną przez wartość prawego operandu, wykonując dzielenie całkowite, i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x //= 2  # x = x // 2, więc x = 2
  ```

### Reszta z dzielenia i przypisanie (`%=`)

- **Opis**: Oblicza resztę z dzielenia zmiennej przez wartość prawego operandu i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 5
  x %= 2  # x = x % 2, więc x = 1
  ```

### Potęgowanie i przypisanie (`**=`)

- **Opis**: Podnosi zmienną do potęgi określonej przez wartość prawego operandu i przypisuje wynik do tej zmiennej.
- **Przykład**:

  ```python
  x = 2
  x **= 3  # x = x ** 3, więc x = 8
  ```

### Bitowe operatory przypisania

- **`&=`**: Bitowe AND i przypisanie
- **`|=`**: Bitowe OR i przypisanie
- **`^=`**: Bitowe XOR i przypisanie
- **`<<=`**: Przesunięcie bitowe w lewo i przypisanie
- **`>>=`**: Przesunięcie bitowe w prawo i przypisanie

---

## Operatory logiczne

Operatory logiczne są używane do operacji na wartościach logicznych (`bool`), zwracają wartość `True` lub `False`.

### Operator `and`

- **Opis**: Zwraca `True` tylko wtedy, gdy oba operandy są prawdziwe.
- **Tabela prawdy**:

  | A       | B       | A and B |
  |---------|---------|---------|
  | False   | False   | False   |
  | False   | True    | False   |
  | True    | False   | False   |
  | True    | True    | True    |

- **Przykład**:

  ```python
  a = True
  b = False
  wynik = a and b  # wynik = False
  ```

### Operator `or`

- **Opis**: Zwraca `True` jeśli przynajmniej jeden z operandów jest prawdziwy.
- **Tabela prawdy**:

  | A       | B       | A or B |
  |---------|---------|--------|
  | False   | False   | False  |
  | False   | True    | True   |
  | True    | False   | True   |
  | True    | True    | True   |

- **Przykład**:

  ```python
  a = True
  b = False
  wynik = a or b  # wynik = True
  ```

### Operator `not`

- **Opis**: Zwraca negację wartości logicznej.
- **Tabela prawdy**:

  | A       | not A |
  |---------|-------|
  | False   | True  |
  | True    | False |

- **Przykład**:

  ```python
  a = True
  wynik = not a  # wynik = False
  ```

### Zwarta ocena wyrażeń logicznych

https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

Python używa tzw. "zwartych" (ang. short-circuit) operatorów logicznych. Oznacza to, że ewaluacja wyrażenia zatrzymuje się, gdy wynik jest już znany.

- **`and`**: Jeśli pierwszy operand jest `False`, drugi nie jest ewaluowany, ponieważ wynik całego wyrażenia będzie na pewno `False`.
- **`or`**: Jeśli pierwszy operand jest `True`, drugi nie jest ewaluowany, ponieważ wynik całego wyrażenia będzie na pewno `True`.

**Przykład**:

```python
def test():
    print("Funkcja test() została wywołana")
    return True

a = False
wynik = a and test()  # Funkcja test() nie zostanie wywołana
```

---

## Operatory bitowe

Operatory bitowe wykonują operacje na poziomie bitów liczb całkowitych.

### Operator bitowy OR (`|`)

- **Opis**: Bitowe OR między dwoma liczbami.
- **Przykład**:

  ```python
  a = 0b1010  # 10 w systemie dziesiętnym
  b = 0b1100  # 12 w systemie dziesiętnym
  wynik = a | b  # 0b1110, czyli 14
  ```

### Operator bitowy AND (`&`)

- **Opis**: Bitowe AND między dwoma liczbami.
- **Przykład**:

  ```python
  wynik = a & b  # 0b1000, czyli 8
  ```

### Operator bitowy XOR (`^`)

- **Opis**: Bitowe XOR między dwoma liczbami.
- **Przykład**:

  ```python
  wynik = a ^ b  # 0b0110, czyli 6
  ```

### Operator negacji bitowej (`~`)

- **Opis**: Odwraca wszystkie bity liczby (bitowe NOT).
- **Przykład**:

  ```python
  wynik = ~a  # Jeśli a = 0b1010 (10), wynik = -11 (uwaga na reprezentację liczb w pamięci)
  ```

### Przesunięcie bitowe w lewo (`<<`)

- **Opis**: Przesuwa bity liczby w lewo o określoną liczbę miejsc (mnożenie przez 2^n).
- **Przykład**:

  ```python
  a = 0b0010  # 2 w dziesiętnym
  wynik = a << 2  # 0b1000, czyli 8
  ```

### Przesunięcie bitowe w prawo (`>>`)

- **Opis**: Przesuwa bity liczby w prawo o określoną liczbę miejsc (dzielenie całkowite przez 2^n).
- **Przykład**:

  ```python
  a = 0b1000  # 8 w dziesiętnym
  wynik = a >> 2  # 0b0010, czyli 2
  ```

### Operatory przypisania z operatorami bitowymi

- **`&=`**: Bitowe AND i przypisanie
- **`|=`**: Bitowe OR i przypisanie
- **`^=`**: Bitowe XOR i przypisanie
- **`<<=`**: Przesunięcie w lewo i przypisanie
- **`>>=`**: Przesunięcie w prawo i przypisanie

**Przykład**:

```python
a = 0b1010
a &= 0b1100  # a = a & 0b1100
```


### Typ tekstowy – `str`

Typ `str` w Pythonie służy do reprezentacji ciągów znaków (napisów). Napisy są sekwencjami znaków Unicode i są wykorzystywane do przechowywania oraz manipulowania tekstem.

#### Tworzenie napisów

Napisy można tworzyć za pomocą pojedynczych (`'...'`) lub podwójnych (`"..."`) cudzysłowów:

```python
"to jest napis"
'to jest napis'
```

Można również konwertować inne typy na napis za pomocą funkcji `str()`:

```python
str(1)  # Konwersja liczby całkowitej na napis '1'
```

#### Tekst wielolinijkowy

Aby utworzyć tekst zawierający wiele linii, używa się potrójnych cudzysłowów:

- Potrójne podwójne cudzysłowy (`"""..."""`):

  ```python
  """
  Ala
  ma
  kota
  """
  ```

- Potrójne pojedyncze cudzysłowy (`'''...'''`):

  ```python
  '''
  To jest
  wielolinijkowy
  napis
  '''
  ```

#### Znaki specjalne

W napisach można używać znaków specjalnych (sekwencji ucieczki) poprzedzonych ukośnikiem `\`:

- `\n` – nowa linia (znak LF)
- `\t` – tabulacja pozioma
- `\r` – powrót karetki (znak CR)
- `\\` – ukośnik odwrotny `\`
- `\'` – apostrof `'`
- `\"` – cudzysłów `"`
- `\a` – sygnał dźwiękowy (bell)

Przykład:

```python
"Linia pierwsza\nLinia druga"
```

#### Niemutowalność napisów

Napisy w Pythonie są **niemutowalne**, co oznacza, że po utworzeniu nie można zmienić ich zawartości. Operacje na napisach zawsze tworzą nowy obiekt.

#### Operacje na napisach

- **Konkatenacja** (łączenie napisów):

  ```python
  "Hello, " + "world!"  # 'Hello, world!'
  ```

- **Powielanie**:

  ```python
  "ha" * 3  # 'hahaha'
  ```

- **Dostęp do znaków i fragmentów (slicing)**:

  ```python
  napis = "Python"
  napis[0]     # 'P' – pierwszy znak
  napis[-1]    # 'n' – ostatni znak
  napis[2:5]   # 'tho' – znaki od indeksu 2 do 4
  napis[:3]    # 'Pyt' – znaki od początku do indeksu 2
  napis[3:]    # 'hon' – znaki od indeksu 3 do końca
  ```

- **Długość napisu**:

  ```python
  len(napis)  # 6 – długość napisu 'Python'
  ```

#### Metody napisów

Napisy w Pythonie mają wiele wbudowanych metod ułatwiających pracę z tekstem:

- `upper()` – zamiana wszystkich liter na wielkie:

  ```python
  "python".upper()  # 'PYTHON'
  ```

- `lower()` – zamiana wszystkich liter na małe:

  ```python
  "Python".lower()  # 'python'
  ```

- `capitalize()` – zamiana pierwszej litery na wielką:

  ```python
  "python".capitalize()  # 'Python'
  ```

- `strip()` – usuwanie białych znaków z początku i końca:

  ```python
  "  Hello World  ".strip()  # 'Hello World'
  ```

- `replace(old, new)` – zamiana podciągu na inny:

  ```python
  "Hello World".replace("World", "Python")  # 'Hello Python'
  ```

- `split(separator)` – podział napisu na listę według separatora:

  ```python
  "A,B,C".split(",")  # ['A', 'B', 'C']
  ```

- `join(iterable)` – łączenie elementów iterowalnych w napis:

  ```python
  ",".join(['A', 'B', 'C'])  # 'A,B,C'
  ```

#### Ćwiczenie

1. **Utwórz zmienne `imie` i `nazwisko`, przypisz swoje dane.**
2. **Wypisz te dane zamienione na duże litery, ale dane w zmiennych mają być małymi literami.**
3. **Wypisz imię i nazwisko połączone w jedną zmienną.**

Przykładowe rozwiązanie:

```python
# Punkt 1
imie = "rafal"
nazwisko = "korzeniewski"

# Punkt 2
print(imie.upper(), nazwisko.upper())  # 'RAFAL KORZENIEWSKI'

# Punkt 3
pelne_imie = imie + " " + nazwisko
print(pelne_imie)  # 'rafal korzeniewski'
```

#### Formatowanie napisów

Istnieje kilka sposobów na formatowanie napisów w Pythonie:

- **Konkatenacja za pomocą operatora `+`**:

  ```python
  imie = "Rafał"
  nazwisko = "Korzeniewski"
  dane = "Imię: " + imie + ", Nazwisko: " + nazwisko
  print(dane)
  ```

- **Metoda `format()`**:

  ```python
  dane = "Imię: {}, Nazwisko: {}".format(imie, nazwisko)
  print(dane)
  ```

- **F-stringi (od Pythona 3.6)**:

  ```python
  dane = f"Imię: {imie}, Nazwisko: {nazwisko}"
  print(dane)
  ```

- **Formatowanie z użyciem operatora `%`** (starszy sposób):

  ```python
  dane = "Imię: %s, Nazwisko: %s" % (imie, nazwisko)
  print(dane)
  ```

#### Przykład formatowania z dodatkowymi parametrami

Można kontrolować sposób wyświetlania wartości, np. liczb zmiennoprzecinkowych:

```python
pi = 3.1415926535
print(f"Pi z dokładnością do dwóch miejsc: {pi:.2f}")  # 'Pi z dokładnością do dwóch miejsc: 3.14'
```

#### Używanie surowych napisów (raw strings)

Surowe napisy ignorują sekwencje ucieczki, co jest przydatne np. w wyrażeniach regularnych lub ścieżkach plików:

```python
sciezka = r"C:\nowy_folder\plik.txt"
print(sciezka)  # 'C:\nowy_folder\plik.txt'
```

#### Unicode i znaki międzynarodowe

Napisy w Pythonie 3 obsługują Unicode, co pozwala na używanie znaków spoza standardowego zestawu ASCII:

```python
napis = "Zażółć gęślą jaźń"
print(napis)
```

#### Sprawdzanie zawartości napisu

- **Czy napis zaczyna się lub kończy określonym podciągiem**:

  ```python
  napis.startswith("Py")  # True, jeśli napis zaczyna się od 'Py'
  napis.endswith("on")    # True, jeśli napis kończy się na 'on'
  ```

- **Wyszukiwanie podciągu**:

  ```python
  napis.find("th")        # Zwraca indeks pierwszego wystąpienia lub -1
  napis.count("o")        # Liczba wystąpień znaku 'o'
  ```

#### Podsumowanie

- Typ `str` jest podstawowym typem danych do pracy z tekstem w Pythonie.
- Napisy są niemutowalne – operacje na nich tworzą nowe obiekty.
- Dostępne są liczne metody do manipulacji i analizy tekstu.
- Formatowanie napisów umożliwia tworzenie czytelnych i złożonych komunikatów.


# Kolekcje

## Napisy – `str`

- **Typ niemutowalny** – po utworzeniu nie można zmienić zawartości napisu.
- Napisy są sekwencjami znaków Unicode, do których można uzyskać dostęp za pomocą indeksów.

```python
napis = "Ala ma kota"
napis[4]     # 'm' – dostęp do piątego znaku (indeks 4)
napis[-1]    # 'a' – ostatni znak
```

### Slicing

- **Wybieranie fragmentów napisu** za pomocą operatora wycinania (slicing):

```python
kolekcja[start:stop:step]
```

- Przykłady:

```python
napis = "Ala ma kota"
napis[0:3]    # 'Ala' – znaki od indeksu 0 do 2
napis[4:6]    # 'ma' – znaki od indeksu 4 do 5
napis[7:]     # 'kota' – znaki od indeksu 7 do końca
napis[:3]     # 'Ala' – znaki od początku do indeksu 2
napis[::2]    # 'Aammkt' – co drugi znak
```

## Krotka – `tuple`

- **Typ niemutowalny** – nie można zmienić elementów po utworzeniu.
- Krotki są sekwencjami mogącymi przechowywać elementy różnych typów.

```python
krotka = ("A", "l", "a")
osoba = ("Rafał", "Korzeniewski", 16, 234.2)
```

- Dostęp do elementów:

```python
imie = osoba[0]      # 'Rafał'
wiek = osoba[2]      # 16
```

- **Zastosowanie**: często używane do zwracania wielu wartości z funkcji.

## Lista – `list`

- **Typ mutowalny** – można zmieniać, dodawać i usuwać elementy.
- Listy mogą przechowywać elementy różnych typów.

```python
lista = [1, 2, 3]
lista[1] = 42        # Zmiana elementu na indeksie 1
lista.append(4)      # Dodanie elementu na końcu
lista.remove(2)      # Usunięcie pierwszego wystąpienia wartości 2
lista.sort()         # Sortowanie listy
```

## Zbiór – `set`

- **Nieuporządkowana kolekcja unikalnych elementów**.
- Elementy muszą być hashowalne (np. liczby, napisy, krotki).

```python
zbior = {1, 2, 3}
zbior2 = set([3, 4, 5])
```

- Operacje na zbiorach:

```python
zbior.union(zbior2)           # {1, 2, 3, 4, 5} – suma zbiorów
zbior.intersection(zbior2)    # {3} – część wspólna
zbior.difference(zbior2)      # {1, 2} – różnica zbiorów
```

- Modyfikacje zbioru:

```python
zbior.add(6)      # Dodanie elementu
zbior.discard(2)  # Usunięcie elementu (bez błędu, jeśli nie istnieje)
```

## Słownik – `dict`

- **Mutowalna kolekcja par klucz-wartość**.
- Klucze muszą być niezmienne i hashowalne.

```python
slownik = {1: "a", 2: "b"}
slownik['klucz'] = 'wartość'    # Dodanie nowej pary
wartosc = slownik[1]            # Dostęp do wartości 'a'
```

- Metody słownika:

```python
slownik.keys()      # Zwraca widok kluczy
slownik.values()    # Zwraca widok wartości
slownik.items()     # Zwraca widok par klucz-wartość
slownik.get('klucz', 'domyślna')  # Pobiera wartość lub zwraca domyślną
```

# Instrukcje warunkowe

Instrukcje warunkowe umożliwiają wykonanie bloku kodu w zależności od spełnienia określonego warunku.

```python
if warunek:
    # Blok instrukcji, gdy warunek jest prawdziwy
elif inny_warunek:
    # Blok instrukcji, gdy inny warunek jest prawdziwy
else:
    # Blok instrukcji, gdy żaden z powyższych warunków nie jest prawdziwy
```

- **Przykład**:

```python
x = 10
if x > 0:
    print("Liczba dodatnia")
elif x == 0:
    print("Zero")
else:
    print("Liczba ujemna")
```

## Structural Pattern Matching

Wprowadzony w Pythonie 3.10, umożliwia dopasowywanie wzorców.

```python
match zmienna:
    case wartość1:
        # Blok instrukcji dla wartość1
    case wartość2:
        # Blok instrukcji dla wartość2
    case _:
        # Domyślny blok, gdy żaden wzorzec nie pasuje
```

- **Przykład**:

```python
komenda = 'start'
match komenda:
    case 'start':
        uruchom()
    case 'stop':
        zatrzymaj()
    case _:
        print("Nieznana komenda")
```

# Wcięcia

- **Python używa wcięć do określania bloków kodu**.
- Standardowo stosuje się **4 spacje**.
- **Nie mieszać spacji i tabulatorów** – może to prowadzić do błędów.

# Pętle

## Pętla `while`

Wykonuje blok kodu, dopóki warunek jest prawdziwy.

```python
while warunek:
    # Blok instrukcji
else:
    # Blok instrukcji, gdy pętla zakończy się bez użycia `break`
```

- **Przykład**:

```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Pętla zakończona normalnie")
```

## Pętla `for`

Służy do iteracji po elementach kolekcji.

```python
for element in kolekcja:
    # Blok instrukcji
```

- **Przykład**:

```python
for i in range(5):
    print(i)
```

- **Pętla `for` z klauzulą `else`**:

```python
for element in kolekcja:
    if szukany_warunek:
        break
else:
    # Wykona się, jeśli pętla nie została przerwana instrukcją `break`
    print("Nie znaleziono elementu spełniającego warunek")
```

# Zadanie

Napisz program, który przyjmuje liczby od użytkownika (kończy przyjmowanie po wpisaniu `"q"`). Program ma wypisać:

- **Liczb było**: łączna liczba wprowadzonych liczb
- **Unikalnych liczb było**: liczba unikalnych wartości
- **Średnia wynosi**: średnia arytmetyczna wprowadzonych liczb

### Rozwiązanie:

```python
liczby = []

while True:
    liczba = input("Podaj liczbę (lub 'q' aby zakończyć): ")
    if liczba == 'q':
        break
    try:
        liczby.append(int(liczba))
    except ValueError:
        print("Proszę podać poprawną liczbę lub 'q' aby zakończyć.")

if liczby:
    unikalne_liczby = set(liczby)
    srednia = sum(liczby) / len(liczby)

    print(f"Liczb było: {len(liczby)}")
    print(f"Unikalnych liczb było: {len(unikalne_liczby)}")
    print(f"Średnia wynosi: {srednia:.2f}")
else:
    print("Nie wprowadzono żadnych liczb.")
```

- **Wyjaśnienie**:
  - Użyto obsługi wyjątków (`try`/`except`), aby zabezpieczyć program przed błędnym wprowadzeniem danych.
  - Sprawdzane jest, czy lista `liczby` nie jest pusta przed obliczeniem średniej, aby uniknąć dzielenia przez zero.
  - Wynik średniej jest formatowany do dwóch miejsc po przecinku.



# Funkcje w Pythonie

## definicje

```python

def nazwa_funkcji():  # sygnatura funkcji
    <cialo funkcji> 


def nazwa_funkcji():
     return None


def nazwa_funkcji():
     return 10


def nazwa_funkcji():
     return 10, 20, 30


def nazwa_funkcji():
    data = now()  # symbolicznie obecna data
    if data.rok > 2020:
      return 200
    return 10


def suma(a, b):
     return a + b

nazwa_funkcji # obiekt funkcji
nazwa_funlcji()  # wywolanie funcji

print
print()


suma()  # zakonczy sie bledem
suma(1)

suma(1, 2)

suma(1, 2, 3)