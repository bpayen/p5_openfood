#! /usr/bin/env python3
# coding: utf-8
""" Programme de test des appels d'API Openfoodfacts 

This program call API Openfoodfact to get Categories, 
then parse it and filter it to get only 5 cat.
From this Cat the program ask products informations 
about 100 products from the 5 cat.

Then the soft write this informations in the database.

"""
import requests

categorie_ids = []
""" Products categories """

response_cat = requests.get('https://fr-fr.openfoodfacts.org/categories.json')

i=0

for j in response_cat.json()['tags'] :
	""" get the 5 first categories from the API OFF
	    and store it in variable to query later for products 
	    from this cat

	    """
	if i == 5:
	    break
	categorie_ids.append(j['id'])
	i += 1

print(categorie_ids)

for cat in categorie_ids :
    print(cat)
""" query the OFF API to get the 100 first products 
	from each 5 first categories
"""


""" Stores the categories products in the data base """

