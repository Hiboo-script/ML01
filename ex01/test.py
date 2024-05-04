from recipe import Recipe
import unittest


class TestStringMethods(unittest.TestCase):

	def test_nameRecipe(self):
		with self.assertRaises(AttributeError):
			yaourt = Recipe(78,3,20,["milk","berry"],"dessert","like in market")
	
	def test_typeLvl(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt","3",20,["milk","berry"],"dessert","like in market")
	
	def test_indexLvlUp(self):	
		with self.assertRaises(IndexError):
			yaourt = Recipe("yaourt",6,20,["milk","berry"],"dessert","like in market")
	
	def test_indexLvlDown(self):	
		with self.assertRaises(IndexError):
			yaourt = Recipe("yaourt",0,20,["milk","berry"],"dessert","like in market")
	
	def test_typeTime(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt",3,"20",["milk","berry"],"dessert","like in market")
	
	def test_negativeTime(self):	
		with self.assertRaises(ValueError):
			yaourt = Recipe("yaourt",3,-20,["milk","berry"],"dessert","like in market")
	
	def test_typeIngredients(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt",3,20,"milk","dessert","like in market")
	
	def test_typeIngredient(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt",3,20,["milk","berry",45],"dessert","like in market")
	
	def test_cookingType(self):	
		with self.assertRaises(ValueError):
			yaourt = Recipe("yaourt",3,20,["milk","berry"],"dert","like in market")
	
	def test_typeCookingType(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt",3,20,["milk","berry"],89,"like in market")
	
	def test_typeDescription(self):	
		with self.assertRaises(AttributeError):
			yaourt = Recipe("yaourt",3,20,["milk","berry"],"dessert",78)

	
if __name__ == '__main__':
    unittest.main()
