import random
class weapon(object):
	def __init__(self):
		self.damage = None
		self.speed = None
class sword(weapon):
	def __init__(self):
		self.speed = 5

class cardboard_sword(sword):
	def __init__(self):
		super( cardboard_sword,self).__init__()
		self.damage = 1
		self.name = "cardboard sword"		

class paper_sword (sword):
	def __init__(self):
		super(paper_sword,self).__init__()
		self.damage = 2
		self.name = "paper sword"

class stone_sword(sword):
	def __init__(self):
		super(stone_sword ,self).__init__()
		self.damage = 3
		self.name = "stone sword"

class golden_sword(sword):
	def __init__(self):
		super( golden_sword,self).__init__()
		self.damage = 4
		self.name = "golden sword"

class best_sword(sword):
	def __init__(self):
		super( best_sword,self).__init__()
		self.damage = 10
		self.name = "best sword"

class best_with_magic_sword(sword):
	def __init__(self):
		super( best_with_magic_sword,self).__init__()
		self.damage = 100000
		self.name = "best sword with magic"

class axe(weapon):
	def __init__(self):
		self.speed = 6



class a_different_axe_the_one_you_have_1(axe):
	def __init__(self):
		super(a_different_axe_the_one_you_have_1,self).__init__()
		self.speed = 6
		self.damage = 5
		self.name = "axe"
class a_different_axe_the_one_you_have_2(axe):
	def __init__(self):
		super(a_different_axe_the_one_you_have_2,self).__init__()
		self.speed = 7
		self.damage = 6
		self.name = "axe with pony"
class a_different_axe_the_one_you_have_3(axe):
	def __init__(self):
		super(a_different_axe_the_one_you_have_3,self).__init__()
		self.speed = 8
		self.damage = 7
		self.name = "axe with lion"
		
		

class fists(weapon):
	def __init__(self):
		self.speed = 3
		self.damage = 1
		self.name = "fisticuffs"



def drop():
	possible_drops = [
						cardboard_sword,
						paper_sword,
						stone_sword,
						golden_sword,
						best_sword,
						best_with_magic_sword,
						a_different_axe_the_one_you_have_1,
						a_different_axe_the_one_you_have_2,
						a_different_axe_the_one_you_have_3
						]
	chances =  [26,24, 10, 7, 3, 1, 20, 6, 3]
	roll = random.randint(1,100)
	for i in range(len(chances)):
		roll -= chances[i]
		if roll <= 0:
			return possible_drops[i]()

