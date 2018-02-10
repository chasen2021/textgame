from weapon import *
from skills import *


class player(object):

	def exp_to_level(level):
		return 10*(level**2)

	def __init__ (self):
		self.level = 1
		self.maxHP = 10
		self.health = self.maxHP
		self.weapon = fists()
		self.skill_tokens = [token(), token(), token()]
		self.start_tokens()
		self.exp = 0





	def start_tokens(self):
		for i in range(len(self.skill_tokens)):
			self.skill_tokens[i].skill = skill_tree[skill_categories[i]][0]

	def display_skill_tree(self):
		for i in range(min(3+self.level/10, len(skill_categories))):
			row = skill_categories[i]
			print(str(i+1)+") " + row + ':')
			for j in range(3):
				print("\t" + skill_letters[j]+ ') ' + skill_tree[row][j])

	def display_skill_tokens(self):
		for i in range(len( self.skill_tokens)):
			token=self.skill_tokens[i]
			print(str(i+1) + ': Token Level ' + str(token.level)+ ' ' + token.skill)

	def move_token(self):
		while True:
			print("You have leveled up, would you like to move a token? (Y)es or (N)o")
			response = input().lower()
			if response not in ["y","n"]:
				print("you stupid piece of garbage, thats not a valid input, try again")
			else:
				if response == "y":
					self.display_skill_tree()
					self.display_skill_tokens()

					while True:
						print("Choose your Token. Enter 1 - " + str(len(self.skill_tokens)))
						response = input()
						if response.lower() not in [str(i) for i in range(1,len(self.skill_tokens) + 1)]:
							print("you stupid piece of garbage, thats not a valid input, try again")
						else:
							while True:
								print("To choose a skill write the number of the category and the letter of the skill. Ex. 1b = scent of loot. ")
								response2 = input()
								if response2.lower() not in [str(i) + l for i in range(1,min(3+self.level/10, len(skill_categories))+1) for l in skill_letters]:
									print("you stupid piece of garbage, thats not a valid input, try again")
								else:
									row = int(response2[0])-1
									column = skill_letters.index(response2[1])
									self.skill_tokens[int(response)-1].skill = skill_tree[skill_categories[row]][column]
									print("Your skill tokens are now ")
									self.display_skill_tokens()
									return True
					return True
				else:
					return False


	def levelup_token(self):
		self.display_skill_tokens()
		while True:
			print("Choose your Token to level up. Enter 1 - " + str(len(self.skill_tokens)))
			response = input()
			if response.lower() not in [str(i) for i in range(1,len(self.skill_tokens) + 1)]:
				print("you stupid piece of garbage. god ur dumb, thats not a valid input, try again")
			else:
				self.skill_tokens[int(response)-1].level += 1
				break
		self.display_skill_tokens()
	def level_up(self, level):
		self.level = level
		if level % 10 == 0:
			self.skill_tokens.append(token())

		else:
			if not self.move_token():
				self.levelup_token()

