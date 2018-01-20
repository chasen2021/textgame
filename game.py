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


def battleloop(player,enemy):
	while player.health > 0 and enemy.health > 0: