import random

chain = {
		'stab':1,
		'slash':3,
		'crush':8
		}
leather = {
		'stab':3,
		'slash':1,
		'crush':8
		}

plate = {
		'stab':2,
		'slash':4,
		'crush':1
		}
armor = {
		'chain':chain,
		'leather':leather,
		'plate':plate 
		}
stamina = {
			'chain': {
					'sword':3,
					'dagger':2,
					'battle hammer':-4
				
					},
			'leather': {
					'sword':0,
					'dagger':-2,
					'battle hammer':0
					},	
			'plate': {
					'sword':-3,
					'dagger':2,
					'battle hammer':4
					}

			}

class Armor:
	def __init__(self, level, atype=None):
		if atype==None:
			self.atype = random.choice(armor.keys())
		else:
			self.atype=atype
		self.rtype = armor[self.atype]
		self.resistance=level + random.normalvariate(0,0.5*level)
		self.resistance=round(self.resistance)
		self.stamina=stamina[self.atype]
		
a=Armor(5)
print(a.atype)
print(a.rtype)
print(a.resistance)
print(a.stamina)