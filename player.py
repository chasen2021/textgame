from weapon import *
from skill import *


class player(object):
 	def __init__ (self):
 		self.level = 1
 		self.maxHP = 10
 		self.health = self.maxHP
 		self.weapon = fists()
 		self.skill_tokens = []

 	def move_token(self):
 		return

	def levelup_token(self):
 		return

 	def level_up(self, level):
 		self.level = level
 		if level % 10 == 0:
 			self.skill_tokens.append(token())

 		else:
 			if not self.move_token():
 				self.levelup_token()
