class test:
	def __init__(self,arg1,arg2):
		self.a = arg1
		if arg2:
			self.b = arg2
		else:
			self.b = 0

salut = test('e',2)
beu = test('beuuuu')
print(f'{salut.a},{salut.b}')
print(f'{beu.a},{beu.b}')
