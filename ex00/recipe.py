

class Recipe:
	
	def __init__(self,name,
		cooking_lvl,cooking_time,
		ingredients,recipe_type,
		description=""):
		
		if not isinstance(name, str):
			raise AttributeError("name of Recipe must be a <str> !")
		elif not isinstance(cooking_lvl,int):
			raise AttributeError("cooking_lvl of resipe must be an <int> !")
		elif cooking_lvl<1 or cooking_lvl>5:
			raise IndexError("cooking_lvl of recipe must be between 1 and 5 inclusive !")
		elif not isinstance(cooking_time, int):
			raise AttributeError("cooking_time must be an <int> !")
		elif cooking_time<0:
			raise ValueError("cooking_time cannot be negative !")
		elif not isinstance(ingredients,list):
			raise AttributeError("ingredients must be a list !")
		elif not all(isinstance(ingredient, str) for ingredient in ingredients):
			raise AttributeError("all ingredients must be a <str> !")
		elif not isinstance(recipe_type,str):
			raise AttributeError("recipe type must be a <str> !")
		elif not recipe_type in {"starter","lunch","dessert"}:
			raise ValueError("recipe_type must be 'starter', 'lunch' or 'dessert' !")
		elif not isinstance(description, str):
			raise AttributeError("description must be a <str> !")
		else:
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.recipe_type = recipe_type
			self.desscription = description

	def __str__(self):
		recipe_txt = f"recipe : {self.name}"
		return recipe_txt


