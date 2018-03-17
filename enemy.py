import random
from weapon import *
SKELETON_MIN_HP = 10
SKELETON_MAX_HP = 15
RATTY_BOI_MIN_HP = 1 
RATTY_BOI_MAX_HP = 5

class enemy(object):
	def die(self):
		return


class skelly_boi(enemy):
	def __init__(self, level):
		self.weapon = golden_sword()
		self.health = random.randint(SKELETON_MIN_HP * level, SKELETON_MAX_HP * level)
		self.name = "skelly boi"
class ratty_boi(enemy):
	def __init__(self, level):
		self.weapon = golden_sword()
		self.health = random.randint(RATTY_BOI_MIN_HP * level, RATTY_BOI_MAX_HP * level)
		self.name = "ratty boi"

def spawn(level):
	possible_spawns = [
						skelly_boi,
						ratty_boi
						]
	chances =  [45, 55]
	roll = random.randint(1,100)
	for i in range(len(chances)):
		roll -= chances[i]
		if roll <= 0:
			return possible_spawns[i](level)

