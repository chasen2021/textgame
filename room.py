import random
import weapon
import enemy
import player

class room:
	roomtypes = ["loot", "empty", "enemy"]

	doortypes = ["unlocked", "locked", "hidden", None]
	def __init__(self, direction, hidden, player):
		self.northdoor = "unlocked"
		self.southdoor= "locked" if direction == "north" else random.choice(room.doortypes)
		self.eastdoor= "locked" if direction == "west" else random.choice(room.doortypes)
		self.westdoor= "locked" if direction == "east" else random.choice(room.doortypes)
		if hidden:
			self.rtype = "loot"
		else:
			roll = random.randint(1, 100)
			if roll <= 40:
				self.rtype = "enemy"
			elif roll <= 80:
				self.rtype = "empty"
			else:
				self.rtype = "loot"
		if self.rtype == "loot":
			self.weapon = weapon.drop()

		if self.rtype == "enemy":
			self.enemy = enemy.spawn(player.level)

		# if rtype == "empty":
	def explore(self):
		if self.rtype == "loot":
			print("you find a mysterious" + self.weapon.name +". do you want it?")
			response = input()
			if response == "yes":
				player.weapon = self.weapon
			else:
				print('ok then, I guess.')
		if self.rtype == "enemy":
			print("your screwed. he gone kill you")
			return self.enemy
		

