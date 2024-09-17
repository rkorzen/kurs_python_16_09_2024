import csv

with open("data/data.csv") as f:
    oceny = []
    reader = csv.DictReader(f)
    for line in reader:
        ocena = int(line['ocena'])
        oceny.append(ocena)

    #     imie, nazwisko, ocena = line
    #     try:
    #         oceny.append(int(ocena))
    #     except ValueError:
    #         continue
    print(sum(oceny)/len(oceny))


header = list("ABCDE")
dane = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]

with open("data/dane2.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(header)
    writer.writerows(dane)