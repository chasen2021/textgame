class weapon(object):
	def __init__(self,damage):
		self.damage = damage


class sword(weapon):
	def __init__(self,damage):
		super(sword,self).__init__(damage)
		self.speed = 5

class axe(weapon):
	def __init__(self,damage):
		super(axe,self).__init__(damage)
		self.speed = 6
		self.damage *= 1.2
		self.damage = int(round(damage))

class fists(weapon):
	def __init__(self):
		super(fists,self).__init__(1)
		self.speed = 3
		
