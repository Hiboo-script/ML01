class test:
	def __init__(self,arg1,arg2='other'):
		self.a = arg1
		self.b = arg2

salut = test('e',2)
beu = test('beuuuu')
print(f'{salut.a},{salut.b}')
print(f'{beu.a},{beu.b}')
