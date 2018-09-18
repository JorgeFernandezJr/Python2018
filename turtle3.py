# turtle3.py

# ex5.py cwc
# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(100)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/1+ 1)
    t.forward(x)
    t.left(59)
