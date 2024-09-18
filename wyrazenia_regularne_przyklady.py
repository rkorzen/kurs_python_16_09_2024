import re

text = "17-120 dsdf  sd 17-120 dsfd f 23-234  434-23223 3123-32 f34rf 45-123"
text_kod = "12-120"

kod_pattern = re.compile(r"\b\d{2}-\d{3}\b")

print(kod_pattern.match(text_kod))
print(kod_pattern.findall(text))


tekst = "Kontant: jan.kowalski@example.pl"
tekst2 = "Kontant: kowalski@example.com.pl"

wzorzec = r"(((\w+\.)+(\w+)|\w+)@(\w+\.)+\w+)"

dopasowanie = re.search(wzorzec, tekst)
print(dopasowanie)

dopasowanie = re.search(wzorzec, tekst2)
print(dopasowanie)
print(dir(dopasowanie))
print(dopasowanie.group())
print(dopasowanie.groups())


# # sub

# tekst  = "To jest stara wersja pliku"
# wzorzec = r"stara"
# zamiennik = "nowa"

# nowy_tekst = re.sub(wzorzec, zamiennik, tekst)


# print("tekst \\n dsdd") # \\n \t \\v 

# print(r"tekst \n dsdd")
