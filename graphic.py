# graphic.py

import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.bgcolor("#000000")
g = turtle.pen()
t.speed(0)
t.color("gold")
t.penup()
t.setposition(0, -95)
t.pendown()
t.width(5 + 1)

for i in range (3): 
	t.forward(250)
	t.right(240)
	
for x in range (2):
	t.forward(250)
	t.right(240)
	t.forward(250)
	
for j in range(2):
	t.right(240)
	t.forward(250)
	
for a in range(1):
	t.right(240)
	t.forward(500)
	
for l in range(3):
	t.right(240)
	t.forward(250)

turtle.done()
