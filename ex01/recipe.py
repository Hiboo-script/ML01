

class Recipe:
	
	def __init__(self,name,
		cooking_lvl,cooking_time,
		ingredients,recipe_type,
		description=""):
		try:
			if not isinstance(name, str):
				raise ValueError("argumentError : name of Recipe must be a str !")
			else:
				self.name = name
		except ValueError as e:
			print(e)
			quit()
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.recipe_type = recipe_type
		self.desscription = description

a = Recipe(0,0,0,0,0)
