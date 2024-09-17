"""
korzystajac z rekurencji napisz kod, ktory splaszczy liste

[1, 2, 3, [4, 5], [5, [6, 7]]] -> [1, 2, 3, 4, 5, 5, 6, 7]

"""

# print(type(10))
# print(type(10) == list)
# print(isinstance(10, list))

def splaszcz(lista):
    result = []
    for el in lista:
        if isinstance(el, list):
            for el2 in splaszcz(el):
                result.append(el2)
        else:
            result.append(el)
    return result

assert splaszcz([1, 2, 3, [4, 5], [5, [6, 7]]]) ==  [1, 2, 3, 4, 5, 5, 6, 7]