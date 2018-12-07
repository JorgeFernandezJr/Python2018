# plot-dictionary.py
import turtle

def main():
    #table is a dictionary
    table = {-100:40,-90:50,-80:50,-70:80,-60:50,-50:50,
                -40:30,-30:0,-20:80,-10:50,0:0,
                    10:30,20:10,30:80,40:50,50:50,
                    60:20,70:0,80:90,90:50,100:50
            }
    print(" KEYS ")
    print(table.keys())
    print(" VALUES ")
    print(table.values)
    #turle.graphics
    twin = turtle.Screen()
    twin.clear()
    t = turtle.Turtle()
    #tWin = turtle.Screen()
    for h,k in table.items(): #get the items in the dictionary
        print (h, k) # trace code
        #x,y = table[n]
        t.penup()
        t.goto(h,k)
        t.pendown()
        t.circle(5)
    twin.exitonclick()

main()

"""
This code uses a dictionary with keys ranging form
-100 to 10 incrementing by 10.
Each key has a value of 0 as an integer.
To retrieve the values in the dictionary "table" a for loop is used.
The x coordinate on a python turtle screen corresponds to h while
the y values coorsponds to k.
***************************************
for h,k in table.items(): #get the items in the dictionary
    print (h, k) # trace code
h and k are then ploted using
    t.penup()
    t.goto(h,k)
    t.pendown()
    t.circle(5)
*** YOUR TASK ***
Change all values (not keys) form 0 to another integer.
Try to make something grovey.
"""
