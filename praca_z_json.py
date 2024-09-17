import json

"""
dump
load
dumps
loads
"""

lista = [{"ą": 1, "b": 2}, {"a": 2, "b": 3}]
print(lista)
print(json.dumps(lista))

text = '[{"\u0105": 1, "b": 2}, {"a": 2, "b": 3}]'
print(text[0])
x = json.loads(text)

print(x[0])

with open("data/dane.json", "w") as f:
    json.dump(x, f)

