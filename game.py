from weapon import *
from enemy import *
from player import *
def user_input():
	while True:
		print ("(S)trike => (P)ierce => (C)rush => (S)rike")
		response = raw_input()
		if response.lower() not in ["s","p","c"]:
			print("you stupid piece of garbage, thats not a valid input, try again")
		else:
			return response.lower()
def enemy_input():
	return random.choice(["s","p","c"])
def who_wins(x, y):
	if x == y:
		return None
	elif x == "s":
		return "user" if y == "p" else "enemy"
	elif x == "p":
		return "user" if y == "c" else "enemy"
	elif x == "c":
		return "user" if y == "s" else "enemy"



def battleloop(player,enemy):
	print("A " + (enemy.name) + " appears. It has " + str(enemy.health) + " health. ")
	while player.health > 0 and enemy.health > 0:
		 x = user_input()
		 y = enemy_input()
		 winner = who_wins (x, y)

		 if "user" == winner:
		 	enemy.health -= player.weapon.damage
		 	print("You hit the " + (enemy.name) + " dealing " + str(player.weapon.damage) + " damage. it has " + str(enemy.health) + " hp left. ")
		 elif "enemy" == winner:
		 	player.health -= enemy.weapon.damage
		 	print("The " + enemy.name + " hits you dealing " + str(enemy.weapon.damage) + " damage. you have " + str(player.health) + " hp left. ")
		 else:
		 	print("You both miss and deal 0 damage")
	if player.health == 0:
		print ("you died")
	else:
		print ("You win")
		player.health = player.maxHP
p = player()
s = skelly_boi(fists(), 1)

battleloop(p, s)



