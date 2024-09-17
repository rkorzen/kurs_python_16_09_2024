# help(print)

# print()
# print(1, 2, "23", sep="-", end="---")
# print(1, 2, "23", sep="-",)
# x = 10
# print("-", f"{x:15}", "-")

# print(list(range(10)))
# print(range(10))


# for i in range(10, 100, 10):
#     for j in range(10, 100, 10):
#         print(i * j)


"""
    1  2  3  4  5

1   1  2  3  4  5
2   2  4  6  8  10
3   3  6  9  12 15 
...

"""

print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()
print()

for i in range(1, 11):
    print(f"{i:3}", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()