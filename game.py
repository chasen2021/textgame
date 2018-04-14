from weapon import *
from enemy import *
import player
from room import *
from AI import *
import random
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
	if player.health <= 0:
		print ("you died")
		exit(0)
	else:
		print ("You win")
		player.health = player.maxHP


def hidden_check(player):
	chance = 50
	token = player.has_skill("scent of loot")
	if token:
		chance += 10 * token.level
	roll = random.randint(1,100)
	if roll <= chance:
		return True
	return False  


def dir_prompt(current_room, player):
	while True:	
		prompt = "you see a door to the North"
		prompt += ", south" if current_room.southdoor in ["locked", "unlocked"] else ""
		prompt += ", east" if current_room.eastdoor in ["locked", "unlocked"] else ""
		prompt += ", west" if current_room.westdoor in ["locked", "unlocked"] else ""
		print (prompt)


		print("choose a direction to go")
		response1 = input().lower()
		if response1 not in ["north", "east","west","south"]:
			print("congrats, you know how not to type north, south, west, or east")
		else: 
			door = getattr(current_room, response1+"door")
			if door == None:
				print('that door is not there')
			if door == "locked":
				print('the door is locked')
			if door == "unlocked":
				return room(response1, False, player)
			if door == "hidden":
				unlocked = hidden_check(player)
				if unlocked:
					next_room = room(response1, True, player)
					return next_room
				else:
					print("you find a door but are unable to unlock it")





def explorer_loop(player, AI):
	current_room = room("north",False, player)
	while True:
		enemy = current_room.explore(player)
		if enemy:
			battleloop(player, enemy, AI)
		current_room = dir_prompt(current_room, player)




p = player.player()
a = history_model_ai()
explorer_loop(p, a)