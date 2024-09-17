"""
Podaj rodzaj operacji [+/*-]: +
Podaj arg a: 10
podaj arg b: 11

Wynik operacji + dla arg (10, 11) to 21
"""

def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def get_data():
    op = input("Podaj rodzaj operacji [+/*-]: ")
    a = int(input("Podaj arg a: "))
    b = int(input("Podaj arg b: "))
    return op, a, b

def main():
    op, a, b = get_data()
    result = operations[op](a, b)

    print(f"Wynik operacji {op} dla arg ({a}, {b}) to {result}")




if __name__ == "__main__":
    # print(dir())
    # print(__name__)
    main()