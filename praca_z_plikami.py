
print("zażółć gęślą jaźń".encode())
print("zażółć gęślą jaźń".encode("CP1250"))

napis_utf = b'za\xc5\xbc\xc3\xb3\xc5\x82\xc4\x87 g\xc4\x99\xc5\x9bl\xc4\x85 ja\xc5\xba\xc5\x84'
napis_cp1250 = b'za\xbf\xf3\xb3\xe6 g\xea\x9cl\xb9 ja\x9f\xf1'

print(napis_utf.decode("utf8"))
print(napis_cp1250.decode("CP1250"))

try:
    f = open("data/dane.txt")
    print(f.read())
except Exception as e:
    print(e)
    1/0
finally:    
    f.close()


with open("cwiczenie_01.py") as f:
    print(dir(f))
    for line in f:
        print(line, end="")


with open("data/dane2.txt", "wb") as f:
    f.write("1 2 3 4 5 6\n".encode())
    f.write("ą ć ź ł 6\n".encode())
