import random



weapon_types=['sword', 'dagger', 'battle hammer']
damage_offset = {
					'sword':2,
					'dagger':-1,
					'battle hammer':10
				}
stamina = {
			'sword':2,
			'dagger':1,
			'battle hammer':10
		}
dtype = {
			'sword':'slash',
			'dagger':'stab',
			'battle hammer':'crush'
		}
# class Weapon(Item):
class Weapon:
	def __init__(self, level, wtype=None):
		if wtype==None:
			self.wtype = random.choice(weapon_types)
		else:
			self.wtype=wtype
		self.damage=level*2 + damage_offset[self.wtype] + random.normalvariate(0,2)
		self.damage=round(self.damage)
		if self.damage<1:
			self.damage=1
		self.stamina=stamina[self.wtype]
		self.dtype=dtype[self.wtype]


sword=Weapon(2)
print(sword.wtype)
print(sword.damage)
print(sword.stamina)
print(sword.dtype)