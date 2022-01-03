import requests, sys, csv

pokemon = None
with open("pokemon_mess.csv", "r") as f:
  pokemon = list(csv.DictReader(f))

base_url = "https://pokeapi.co/api/v2/pokemon/"
print("id,name,height,weight,type1,type2")

for p in pokemon:
  res = requests.get(f"{base_url}/{p['name']}")
  if res.status_code == 200:
    info = res.json()
    print(f"{info['id']},{info['name'],}}")
