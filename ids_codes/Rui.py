from uuid6 import uuid7
import logging

class Rui:
	"""Referent Unique Identifier"""
	
	def __init__(self, a_or_r):
		self.uuid = uuid7()
		if (a_or_r == 'A' or a_or_r == 'R'):
			self.a_or_r = a_or_r
		else:
			raise Exception("a_or_r must be set to A (assigned) or R (reserved)")

	def is_assigned(self):
		return (self.a_or_r == 'A')

	def is_reserved(self): 
		return (self.a_or_r == 'R')

	def update_status_assigned(self):
		if (self.a_or_r == 'A'):
			logging.warning("status of Rui instance is already assigned. No change.")
		else:
			self.a_or_r = 'A'
