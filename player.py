from weapon import *
from skills import *


class player(object):
	def __init__ (self):
		self.level = 1
		self.maxHP = 10
		self.health = self.maxHP
		self.weapon = fists()
		self.skill_tokens = [token(), token(), token()]

	def move_token(self):
		while True:
			print("You have leveled up, would you like to move a token? (Y)es or (N)o")
			response = input().lower()
			if response not in ["y","n"]:
				print("you stupid piece of garbage, thats not a valid input, try again")
			else:
				if response == "y":
					# TODO: Replace skill_tree.keys occurrences with skill_categories
					for i in range(min(3+self.level/10, len(skill_tree.keys()))):
						row = list(skill_tree.keys())[i]
						print(str(i+1)+") " + row + ':')
						letter = ['a','b','c']
						for j in range(3):
							print("\t" + letter[j]+ ') ' + skill_tree[row][j])

					for token in self.skill_tokens:
						print('Token Level ' + str(token.level)+ ' ' + token.skill)
					while True:
						print("Choose your Token. Enter 1 - " + str(len(self.skill_tokens)))
						response = input()
						if response.lower() not in [str(i) for i in range(1,len(self.skill_tokens) + 1)]:
							print("you stupid piece of garbage, thats not a valid input, try again")
						else:
							while True:
								print("To choose a skill write the number of the category and the letter of the skill. Ex. 1b = scent of loot. ")
								response2 = input()
								if response2.lower() not in [str(i) + l for i in range(1,min(3+self.level/10, len(skill_tree.keys()))+1) for l in letter]:
									print("you stupid piece of garbage, thats not a valid input, try again")
								else:
									row = int(response2[0])-1
									column = letter.index(response2[1])
									self.skill_tokens[response-1].skill = skill_tree[list(skill_tree.keys())[row]][column]
									return True
					return True
				else:
					return False


	def levelup_token(self):
		return

	def level_up(self, level):
		self.level = level
		if level % 10 == 0:
			self.skill_tokens.append(token())

		else:
			if not self.move_token():
				self.levelup_token()
