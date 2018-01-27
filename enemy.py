import random
SKELETON_MIN_HP = 10
SKELETON_MAX_HP = 15

class enemy(object):
	def die(self):
		return


class skelly_boi(enemy):
	def __init__(self,weapon, level):
		self.weapon = weapon
		self.health = random.randint(SKELETON_MIN_HP * level, SKELETON_MAX_HP * level)
		self.name = "skelly boi"

