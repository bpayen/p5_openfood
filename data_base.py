#! /usr/bin/env python3
# coding: utf-8
""" creates MySQL database of the application 

This program is in charge of managing the 
database of the application.

"""
import mysql.connector

""" import cosntantes values """



class dataBase:
	""" contains evry action and data about the database """


	def initialise_database(self):
		""" initialise all the database, from dropping the old one
		to creating the new one.

		"""

		pass

    def store_categorie(self, id, name, description ):

		""" Store the categorie information in the DB """
		pass

	
	def store_product(self, id, nutriscore, store="", url_off="", description, fk_categorie):

		""" Store the product information in the DB """
		pass


	def store_surrogate(self, fk_categorie, fk_product):
		""" Store the substitute into the DB """
		pass

	def get_surrogate(self, fk_categorie, fk_product):

		""" returns the substitute from the DB, according to 
		the parameters passed to the methode.

		"""
		pass




