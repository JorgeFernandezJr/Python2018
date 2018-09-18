# Turtle.py
# turtle3.py
import turtle

# ex5.py cwc
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
colors = ['red', 'purple', 'blue', 'green', 'orange', 'light blue']
t = turtle.Pen()
turtle.bgcolor('yellow')
t.speed(0)
for x in range(720):
    t.pencolor(colors[x%6])
    t.width(x/200+ 1)
    t.forward(x)
    t.left(59)


ninja = turtle.Turtle()
ninja.speed(0)
ninja.color("#000000")
for i in range(180):
	ninja.forward(100)
	ninja.right(30)
	ninja.forward(20)
	ninja.left(60)
	ninja.forward(50)
	ninja.right(30)
	
	ninja.penup()
	ninja.setposition(0, 0)
	ninja.pendown()
	
	ninja.right(2)

turtle.done()

