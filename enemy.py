import random
SKELETON_MIN_HP = 10
SKELETON_MAX_HP = 15

class enemy(object):



class skelly_boi(enemy):
	def __init__(self,attack):
		self.attack = attack
		self.health = random.randint(SKELETON_MIN_HP, SKELETON_MAX_HP)



