import recipe
import unittest

salade = recipe.Recipe("salad",1,10,["onion","oil","salad"],"starter")
print(str(salade))


class TestStringMethods(unittest.TestCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)
	
	def test_nameRecipe(self):
		with self.assertRaises(ValueError):
			yaourt = recipe.Recipe(78,3,20,["milk","berry"],"dessert","like in market")

if __name__ == '__main__':
    unittest.main()
