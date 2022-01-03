# API Practice
Let's clean up the `pokemon_mess.csv` with code this time. We're going to use a Pokemon API.

## Accessing the API
1. Look at [this documentation for the Pokemon API](https://pokeapi.co/docs/v2#pokemon). What is the baseurl and endpoint?
2. What is the url for getting information for `steelix`? What happens if you try `Steelix`?

## Setup
1. Write a `Pokemon` class that encapsulates all the information you need to clean the csv. The `__str__` method should return the corresponding clean line of the csv.

## Cleanup
Write a Python file that outputs a `pokemon.csv`, which is a clean version of `pokemon_mess.csv`.

Some steps that might help are:
 - reading in the `pokemon_mess.csv`
 - using the name from that data to query the API
 - using the API data to construct `Pokemon` objects
 - using the `__str__` method to print the correct csv

If your program works as intended, the following terminal command should produce the clean csv:  
`python3 clean_pokemon.py > pokemon.csv`