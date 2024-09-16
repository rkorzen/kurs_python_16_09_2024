punkt = (5, 50)

x = punkt[0]
y = punkt[1]

# x, y = punkt

if x < 0 or y < 0 or x > 100 or y > 100:
    print("Poza planszą")
elif x > 90 and y > 90:
    print("GPR")
elif x > 90 and y < 10:
    print("DPR")
elif x < 10 and y < 10:
    print("DLR")
elif x < 10 and y > 90:
    print("GLR")
elif x > 90: 
    print("PK")
elif y < 10:
    print("DK")
elif x < 10:
    print("LK")
elif y > 90:
    print("GK")
else:
    print("C")