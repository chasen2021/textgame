import random
class AI:
	def attack(self):
		roll = self.belief()
		if roll == "s":
			return "c"
		if roll =="p":
			return "s"
		else:
			return "p"

class random_model_ai(AI):
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


attacks = ['s','p','c']
class history_model_ai(AI):
	def __init__(self):
		self.state = {}
		for a1 in attacks:
			for a2 in attacks:
				for a3 in attacks:
					for a4 in attacks:
						self.state[(a1,a2,a3,a4)] = {"s":1, "p":1, "c":1}
		for a1 in attacks:
			for a2 in attacks:
				for a3 in attacks:
					for a4 in attacks:
						self.normalize((a1,a2,a3,a4))
		self.lr = 0.1
		self.history = []

	def normalize(self, history):
		d=self.state[history]
		sum = 0
		for attack in ["s","p","c"]:
			sum += d[attack]
		for attack in ["s","p","c"]:
			d[attack] /= float(sum)

	def update(self,attack):
		self.history.insert(0,attack)
		self.history = self.history[0:4]
		if len(self.history) == 4:
			d=self.state[tuple(self.history)]
			d["s"] = (1-self.lr) * d["s"] + self.lr * ("s" == attack)
			d["p"] = (1-self.lr) * d["p"] + self.lr * ("p" == attack)
			d["c"] = (1-self.lr) * d["c"] + self.lr * ("c" == attack)
			self.normalize(tuple(self.history))

	def belief(self):
		if len(self.history) < 4:
			return random.choice(attacks)
		d=self.state[tuple(self.history)]
		roll = random.random()
		if roll < d["s"]:
			return "s"
		if roll < d["s"]+d["p"]:
			return "p"
		return "c"
