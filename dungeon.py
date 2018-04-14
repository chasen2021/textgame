import random
class dungeon:
	max_depth = 5

	def __init__(self):
		grid=[["entrance"]]
		starts=[(0,-1,False),(-1,0,False),(0,1,False),(1,0,False)]
		i=random.randint(0,3)
		starts[i]=(starts[i][0],starts[i][1], True)
		for x,y,exit in starts:
			d=0
			while d<dungeon.max_depth:
				offsets=[(0,-1),(-1,0), (0,1), (1,0)]
				x,y += random.choice(offsets)

		if x<0:
			for row in grid:
				row.insert(0,None)
			x=0
		if y < 0:
			grid.insert(0,[None]*len(grid[0]))
			y=0
		if x >= len(grid[0]):
			for row in grid:
				row.append(None)
		if y >= len(grid):
			grid.append([None]*len(grid[0]))

