from weapon import *
from enemy import *
from player import *
from AI import *
def user_input():
	while True:
		print ("(S)trike => (P)ierce => (C)rush => (S)rike")
		response = input()
		if response.lower() not in ["s","p","c"]:
			print("you stupid piece of garbage, thats not a valid input, try again")
		else:
			return response.lower()
def enemy_input(AI):
	return AI.attack()
def who_wins(x, y):
	if x == y:
		return None
	elif x == "s":
		return "user" if y == "p" else "enemy"
	elif x == "p":
		return "user" if y == "c" else "enemy"
	elif x == "c":
		return "user" if y == "s" else "enemy"



def battleloop(player,enemy, AI):
	print("A " + (enemy.name) + " appears. It has " + str(enemy.health) + " health. ")
	while player.health > 0 and enemy.health > 0:
		 x = user_input()
		 y = enemy_input(AI)
		 winner = who_wins (x, y)
		 AI.update(x)
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
		exit(0)
	else:
		print ("You win")
		player.health = player.maxHP
p = player()
s = skelly_boi(1)
a = history_model_ai()
battleloop(p, s, a)
print(a.state[("s","s","s","s")])



def explorer_loop(player, AI):
	current_room = room("north",False, player)
	while True:
		current_room.explore()
		if current_room.enemy:
			battleloop(player, current_room.enemy, AI)
		direction = dir_prompt(current_room) #TODO dir_prompt
		current_room = room(direction, current_room.is_hidden(direction), player)



