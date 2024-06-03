"""
Author: Matt Pettis <matthew.pettis@minneapolis.edu>
Date: 2023-11-27
Description:
    read lab16.csv
"""

import os, sys
from pprint import pprint
from pathlib import Path
import csv
import json
import requests

#inputcsv_fpth = Path.cwd() / "lab16.csv"
inputcsv_fpth = r'C:\Users\id9707qp\PycharmProjects\ITEC_1150_Fa2023\Week-16\lab16.csv'
inputjsonsimple_fpth = r'C:\Users\id9707qp\PycharmProjects\ITEC_1150_Fa2023\Week-16\json-simple.json'
inputjsonpokedex_fpth = r'C:\Users\id9707qp\PycharmProjects\ITEC_1150_Fa2023\Week-16\json-pokedex.json'



# raw read in
# Hard to work with...
with open(inputcsv_fpth) as f:
    for line in f:
        print(line.rstrip())



# Read in file, clunky
with open(inputcsv_fpth) as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
        # if row:
        #     print(row)



# Read the rows in, but make a dict out of it
with open(inputcsv_fpth) as f:
    dictcsv = csv.DictReader(f)
    for row in dictcsv:
        print(row)



# Dicts can make manipulation easier
with open(inputcsv_fpth) as f:
    dictcsv = csv.DictReader(f)
    area_total = 0
    for row in dictcsv:
        row['Area'] = int(row['Area'])
        area_total += row['Area']
    print(f"Continent area total: {area_total:,}")




# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# json

# Read in from string to an object
with open(inputjsonsimple_fpth) as f:
    d = json.load(f)

pprint(d)
print(d['name'])



# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
# Complex: get json from web, read and process
# https://pokeapi.co/docs/v2

# Particular URL
url = 'https://pokeapi.co/api/v2/pokedex/12'

# Pull from API
resp = requests.get(url)

# Turn JSON text to Python dict
pokedex = json.loads(resp.text)
pprint(pokedex)

# Print json to file
# https://stackoverflow.com/questions/9170288/pretty-print-json-data-to-a-file-using-python
with open(inputjsonpokedex_fpth, "w") as f:
    json.dump(pokedex, f, indent=4, sort_keys=True)


# Go through some entries, pick off parts.
for e in pokedex['pokemon_entries']:
    print(e['pokemon_species']['name'])

