import random
import armor
import weapon
class enemy:
	def __init__(self, armor, weapon, health, stamina):
		level = 5
		self.stamina = 10
		self.health = level + random.randint(4,15)
		self.armor=armor
		self.weapon=weapon
e=enemy(armor.Armor(4),weapon.Weapon(4), 3, 10)
print(e.stamina)
print(e.health)
print(e.armor)
print(e.weapon)



