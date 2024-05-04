from datetime import date

class Book:
	
	def __init__(self, name):
		if not isinstance(name, str):
			raise AttributeError("book name must be a <str> !")
		
		else:
			self.name = name
			self.creation_date = date.today()
			self.last_update = self.creation_date
			self.recipes_list = dict(starter = set(), lunch = set(), dessert = set())
