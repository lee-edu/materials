import requests
import sys
import random as r
import csv


def getTypes(p):
  '''
    Extract types from PokeAPI json result
    '''
  types = p['types']

  if len(types) < 2:
    types.append({'type': {'name': "none"}})

  return ",".join([t['type']['name'] for t in types])


def scramble_case(s):
  '''
  Scramble the case of each char in a given string s
  '''

  def scramble_char(c):
    if r.random() < 0.5:
      return c.lower()
    else:
      return c.upper()

  return "".join([scramble_char(c) for c in s])


def scramble_num(x):
  '''
  Scamble a number via math
  '''
  x = int(x)
  if r.random() < 0.5:
    x = int(x * r.random() * 1.5)
  else:
    x -= 100
  return x


def get_pokemon(id_or_name):
  BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
  res = requests.get(f"{BASE_URL}/{id_or_name}")
  if res.status_code == 200:
    pokemon = res.json()
    return [
        pokemon['id'], pokemon['name'], pokemon['height'], pokemon['weight'],
        getTypes(pokemon)
    ]
  else:
    print(f"ERROR: Could not retrieve {id_or_name}")
    exit()


def print_n_random_pokemon(id_or_names):
  for dex_num in id_or_names:
    pokemon = get_pokemon(dex_num)
    print(",".join([str(i) for i in pokemon]))


def generate_messy_csv():
  print("id,name,height,weight,type1,type2")
  n = int(sys.argv[1])
  dex_nums = {r.randint(1, 800) for _ in range(n)}
  print_n_random_pokemon(dex_nums)


def clean_csv():
  print("id,name,height,weight,type1,type2")
  # Retrieve list of names from messy csv
  pokemon = None
  with open("pokemon_mess.csv", "r") as f:
    pokemon = list(csv.DictReader(f))
  names = [p['name'].lower() for p in pokemon]
  print_n_random_pokemon(names)


if __name__ == "__main__":
  #generate_messy_csv()
  clean_csv()
