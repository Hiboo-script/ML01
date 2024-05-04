

class Recipe:
	
	def __init__(self,name,
		cooking_lvl,cooking_time,
		ingredients,recipe_type,
		description=""):
		try:
			if not isinstance(name, str):
				raise ValueError("argumentError : name of Recipe must be a str !")
			elif not isinstance(cooking_lvl,int):
				raise ValueError("argumentError : cooking_lvl of resipe must be an int !")
			elif cooking_lvl<1 and cooking_lvl>5:
				raise Value_Error("rangeError : cooking_lvl of recipe must be between 1 and 5 inclusive !")
			elif not isinstance(cooking_time, int):
				raise valueError("argumentError : cooking_time must be an int !")
			elif cooking_time<0:
				raise valueError("physicalError : cooking_time cannot be negative !")
			elif ingredient
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
