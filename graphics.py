import turtle as t

def square(size, color1, color2, pos):
	t.penup()
	t.goto(pos)
	t.pendown()
	t.color(color1, color2)
	t.begin_fill()
	for i in range(4):
		t.forward(size)
		t.right(90)
	t.end_fill()
t.ht()

t.tracer(0,0)
square(100, "black", "blue", (0,0))
square(100, "black", "blue", (0,100))
square(100, "black", "blue", (0,200))
square(100, "black", "blue", (100,100))
square(100, "black", "blue", (200,200))
t.update()
t.done()