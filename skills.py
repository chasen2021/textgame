skill_tree = {	"awareness":["danger sense", "scent of loot", "spider sense"],
				"brute strength":["hammer affinity", "pumping iron", "unstoppable force"],
				"precision":["critical blows", "sword affinity", "clean cuts"]
				}
skill_categories = ["awareness", "brute strength", "precision"]

class token:
	def __init__ (self):
		self.skill = None
		self.level = 1

