import requests

response = requests.get("https://api.nbp.pl/api/exchangerates/tables/A/?format=json")

print(response.status_code)
data = response.json()
kursy = data[0]["rates"]

for kurs in kursy:
    print(f"{kurs['code']}: {kurs['mid']}")

print(type(data))