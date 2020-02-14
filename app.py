#! /usr/bin/env python3
# coding: utf-8
""" Module that encapsulate the openfoodfact applicaation

This program coodonate calls to API class to renew 
database informations, store this informations in database and
manages interaction with the user.

"""

#import data_base
from api_off import *

class App:
	def __init__(self):

	    """ creates API class instance """
	    self.api_off = ApiOff()

	    #print(self.api_off.get_categories()) # DEBUG
	    print(self.api_off.get_products('en:dairies')) # DEBUG

	    """ creates Database class instance """

	""" for every first 5 categories scarped on OFF we scrap 
	100 products, and store them in the DataBase.
	"""
	pass



# ==================================================================================================
def main():
    app = App()
    #app.on_execute()

if __name__ == "__main__":
    main()