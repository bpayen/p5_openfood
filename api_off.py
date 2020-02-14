#! /usr/bin/env python3
# coding: utf-8
""" Calls the OFF API to get categories and products

"""
import requests
from api_off_constantes import *
""" import constantes values """



class ApiOff:
	""" contains evry action and data to get informations from OFF API """

	def get_categories(self):
		""" Pull the first 5 categories from the OFF API.
		It returns LIST object with the 5 firts ID categories inside.

		"""
		_categories_info = []
		""" Products categories """

		_response_cat = requests.get(CATEGORIES_URL)

		i=0
		""" Loop control """

		security = 0
		""" variable used to protect against infinite loop """

		for categorie in _response_cat.json()['tags'] :
			""" get the 5 first categories from the API OFF
			    and store it in variable to query later for products 
			    from this cat.

			    It must have at least 100 product in the categorie to retain it 
			    in the list.

			    """

			#print(categorie['id'], end=" ") #DEBUG
			#print(categorie['products']) #DEBUG

			if categorie['products'] >= MAX_PRODUCTS :
				_categories_info.append({ 'id' : categorie['id'], 'name' : categorie['name']})
				i += 1

			if i == MAX_CATEGORIES or security >= MAX_LOOP:
				break

			security += 1

		#print(_categories_info) #DEBUG

		return _categories_info

	def get_products(self, id_categories):

		""" returns LIST object containing up to 100 products 
		corresponding to the category given as parameter.

		"""
		_products_info = []

		

		#_response_products = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=' + id_categories + '&json=true&page_size=100')
		_response_products = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=en:dairies&json=true&page_size=100')

		i=0

		""" variable used to protect against infinite loop """

		for product in _response_products.json()['products'] :
			""" get the 5 first categories from the API OFF
			    and store it in variable to query later for products 
			    from this cat.

			    It must have at least 100 product in the categorie to retain it 
			    in the list.

			    """
			try:
			    _products_info.append(
			    	{ 'id' : product['id'], 'product_name' : product['product_name'], 
			    	'generic_name':product['generic_name'], 'brands' : product['brands'], 'url':product['url'],
			    	'purchase_places':product['purchase_places'], 'stores':product['stores']
			    	}
			    	)
			    i += 1

			except KeyError:
				print("KeyError") # DEBUG
				pass


			if i == MAX_PRODUCTS :
				break

		print(_products_info) #DEBUG

		return _products_info
