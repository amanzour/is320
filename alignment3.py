from random import random
import turtle as tri
import random as rand

# Got any grapes? - Billy K

#-----game configuration----

# sh = shape, c = color, fc = fillcolor

sh = "triangle"
c = "pink"
fc = "pink"
tri.shapesize(1)
tri.shape(sh)
tri.fillcolor(fc)
tri.setheading(90)
 
def onclick(): 
 ()
if (tri.onclick):
 x2 = rand.randint (-250,250) 
 y2 = rand.randint (-300, 300)
 def change_posit():
  (x2,y2)
 
def tri_clicked(a,b):
 change_posit
 tri.penup()
 tri.goto(x2,y2)
 tri.pendown()

tri.onclick(tri_clicked)

def draw_triangle(pen_type="turtle",
                  init_x=-100, init_y=0, size=300):
  # draw triangle 
  pen = tri.Turtle()
  pen.shape(pen_type)
  pen.penup()
  pen.goto(init_x,init_y)
  pen.pendown()

  for i in range(3):
    pen.forward(size)
    pen.left(120)

  pen.hideturtle()

draw_triangle("triangle",-50,50,400)

wn = tri.Screen()
wn.mainloop()
#-----does this work-----
