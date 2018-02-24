import random


class random_model_ai:
	def __init__(self):
		self.sc = 1
		self.pc = 1
		self.cc = 1
		self.normalize()
		self.lr = .05

	def normalize(self):
		sum = self.sc + self.pc +self.cc
		self.sc /= sum
		self.pc /= sum
		self.cc /= sum

	def update(self, attack):
		self.sc = (1-self.lr)*self.sc+self.lr*(attack == "s")
		self.pc = (1-self.lr)*self.pc+self.lr*(attack == "p")
		self.cc = (1-self.lr)*self.cc+self.lr*(attack == "c")
		self.normalize()

	def belief(self):
		roll = random.random()
		if roll < self.sc:
			return "s"
		if roll < self.sc+self.pc:
			return "p"
		return "c"

	def attack(self):
		roll = self.belief()
		if roll == "s":
			return "c"
		if roll =="p":
			return "s"
		else:
			return "p"
attacks = ['s','p','c']
class history_model_ai:
	def __init__(self):
		self.state = {}
		for a1 in attacks:
			for a2 in attacks:
				for a3 in attacks:
					for a4 in attacks:
						self.state[(a1,a2,a3,a4)] = 1
		self.normalize()
		self.lr = 0.05
		self.history = []

	def normalize(self):
		sum = 0
		for a1 in attacks:
			for a2 in attacks:
				for a3 in attacks:
					for a4 in attacks:
						sum += self.state[(a1,a2,a3,a4)]
		for a1 in attacks:
			for a2 in attacks:
				for a3 in attacks:
					for a4 in attacks:
						self.state[(a1,a2,a3,a4)] /= sum
	def update(self,attack):
		self.history.insert(0,attack)
		self.history = self.history[0:4]
		if len(self.history) == 4:
			# todo update beliefs.


