import tkinter as ttk

def jakas_funkcja():
    text = pole.get()
    op = operacja.get()
    if op == "a":
        p_t = text.lower()
    else:
        p_t = text.upper()

    wynik.configure(text=p_t)

root = ttk.Tk()
root.title("Proste GUI")

label = ttk.Label(root, text="Jakas labelka")
label.pack()

pole = ttk.Entry(root)
pole.pack()

button = ttk.Button(root, text="wykonaj", command=jakas_funkcja)
button.pack()

wynik = ttk.Label(root, text="-")
wynik.pack()

operacja = ttk.StringVar()
operacja.set("a")

frame = ttk.Frame(root)
frame.pack()


radio_a = ttk.Radiobutton(frame, text="lower", variable=operacja, value="a")
radio_a.pack(side="left")

radio_b = ttk.Radiobutton(frame, text="upper", variable=operacja, value="b")
radio_b.pack(side="left")

root.mainloop()