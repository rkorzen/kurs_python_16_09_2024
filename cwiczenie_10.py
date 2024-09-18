"""
w oparciu o API NBP i tkinter
stworz prosty program z GUI do przeliczania walut

"""
import tkinter as ttk
import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=json"

def get_data(url):
    response = requests.get(url)
    data = response.json()
    kursy = data[0]["rates"]
    return kursy

def get_value_for_currency(kursy, code):
    for currency in kursy:
        if currency["code"] == code:
            return currency["mid"]


def calculate():
    c = currency.get()
    a = int(amount.get())

    kursy = get_data(url)
    v = get_value_for_currency(kursy, c)

    wynik.configure(text=f"{v*a:.2f}")


root = ttk.Tk()

label_currency = ttk.Label(root, text="Podaj kod waluty: ")
label_currency.pack()

currency = ttk.Entry(root)
currency.pack()

label_amount = ttk.Label(root, text="Wpisz ile chcesz tej waluty: ")
label_amount.pack()

amount = ttk.Entry(root)
amount.pack()

button = ttk.Button(root, text="Przelicz", command=calculate)
button.pack()

wynik = ttk.Label(root, text="-")
wynik.pack()

root.mainloop()
