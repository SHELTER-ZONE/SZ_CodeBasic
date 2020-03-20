class abc:
	def __init__(self, targets):
		self.targets = targets
		
target_1 = abc([10, 81, 95, 73])

def position(x):
	for target in x:
		if target % 5 == 0:
			x = target
			y = target + 10
			return x, y

x, y = position(target_1.targets)

print(x+y)
