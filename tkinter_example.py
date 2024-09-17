import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def oblicz():
    try:
        liczba1 = float(entry_liczba1.get())
        liczba2 = float(entry_liczba2.get())
        operacja = var_operacja.get()

        if operacja == '+':
            wynik = liczba1 + liczba2
        elif operacja == '-':
            wynik = liczba1 - liczba2
        elif operacja == '*':
            wynik = liczba1 * liczba2
        elif operacja == '/':
            if liczba2 != 0:
                wynik = liczba1 / liczba2
            else:
                messagebox.showerror("Błąd", "Nie można dzielić przez zero!")
                return
        else:
            messagebox.showerror("Błąd", "Nie wybrano operacji!")
            return

        label_wynik.config(text=f"Wynik: {wynik}")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadź poprawne liczby!")


# Tworzenie głównego okna
root = ttk.Tk()


root.title("Prosty Kalkulator")

# Etykiety i pola do wprowadzania liczb
label_liczba1 = tk.Label(root, text="Liczba 1:")
label_liczba1.grid(row=0, column=0, padx=5, pady=5)

entry_liczba1 = tk.Entry(root)
entry_liczba1.grid(row=0, column=1, padx=5, pady=5)

label_liczba2 = tk.Label(root, text="Liczba 2:")
label_liczba2.grid(row=1, column=0, padx=5, pady=5)

entry_liczba2 = tk.Entry(root)
entry_liczba2.grid(row=1, column=1, padx=5, pady=5)

# Opcje operacji
var_operacja = tk.StringVar()
var_operacja.set('+')  # Domyślna operacja

label_operacja = tk.Label(root, text="Operacja:")
label_operacja.grid(row=2, column=0, padx=5, pady=5)

frame_operacje = tk.Frame(root)
frame_operacje.grid(row=2, column=1, padx=5, pady=5)

radio_dodawanie = tk.Radiobutton(frame_operacje, text='+', variable=var_operacja, value='+')
radio_dodawanie.pack(side='left')

radio_odejmowanie = tk.Radiobutton(frame_operacje, text='-', variable=var_operacja, value='-')
radio_odejmowanie.pack(side='left')

radio_mnozenie = tk.Radiobutton(frame_operacje, text='*', variable=var_operacja, value='*')
radio_mnozenie.pack(side='left')

radio_dzielenie = tk.Radiobutton(frame_operacje, text='/', variable=var_operacja, value='/')
radio_dzielenie.pack(side='left')

# Przycisk do obliczania
button_oblicz = tk.Button(root, text="Oblicz", command=oblicz)
button_oblicz.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Etykieta z wynikiem
label_wynik = tk.Label(root, text="Wynik: ")
label_wynik.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Uruchomienie pętli głównej
root.mainloop()
