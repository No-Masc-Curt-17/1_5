#   a116_ladybug.py
import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)
iteration = 0

#number of legs
leg = 6
#length of each leg
leg_length = 50
#amount of degrees between legs
degrees = 360 / leg
ladybug.speed(3)

ladybug.pensize(5)
for i in range(3):
  ladybug.goto(0,-35)
  ladybug.setheading(degrees*iteration)
  ladybug.forward(60)
  iteration = iteration + 1

for i in range(3):
  ladybug.goto(0,-35)
  ladybug.setheading(*degrees*iteration)
  ladybug.setheading(0)
  ladybug.forward(60)
  iteration = iteration + 1
 

ladybug.lt(65)
# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  xpos+=10
  ypos+=20
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots+=1

  # position next dots
  xpos = ypos + 25
  xpos = xpos + 15
  num_dot = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()