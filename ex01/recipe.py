

class Recipe:
	
	def __init__(self,name,
		cooking_lvl,cooking_time,
		ingredients,recipe_type,
		description=""):
		try:
			if not isinstance(name, str):
				raise ValueError("typeError : name of Recipe must be a <str> !")
			elif not isinstance(cooking_lvl,int):
				raise ValueError("typeError : cooking_lvl of resipe must be an <int> !")
			elif cooking_lvl<1 or cooking_lvl>5:
				raise ValueError("rangeError : cooking_lvl of recipe must be between 1 and 5 inclusive !")
			elif not isinstance(cooking_time, int):
				raise ValueError("typeError : cooking_time must be an <int> !")
			elif cooking_time<0:
				raise ValueError("physicalError : cooking_time cannot be negative !")
			elif not isinstance(ingredients,list):
				raise ValueError("typeError : ingredients must be a list !")
			elif not all(isinstance(ingredient, str) for ingredient in ingredients):
				raise ValueError("typeError : all ingredients must be a <str> !")
			elif not isinstance(recipe_type,str):
				raise ValueError("typeError : recipe type must be a <str> !")
			elif not recipe_type in {"starter","lunch","dessert"}:
				raise ValueError("valueError : recipe_type must be 'starter', 'lunch' or 'dessert' !")
			elif not isinstance(description, str):
				raise ValueError("typeError : description must be a <str> !")
			else:
				self.name = name
				self.cooking_lvl = cooking_lvl
				self.cooking_time = cooking_time
				self.ingredients = ingredients
				self.recipe_type = recipe_type
				self.desscription = description
		except ValueError as e:
			print(e)
			quit()

		def __str__(self):
			recipe_txt = f"recipe : {recipe.name}"
			return recipe_txt
