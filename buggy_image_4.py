#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
#size of body
spider.circle(20)
#number of legs
leg = 8
#length of each leg
leg_length = 70
#amount of degrees between legs
degrees = 360 / leg
spider.pensize(5)
iteration = 0
#making the legs

x=-10
for i in range(2):
  spider.penup()
  spider.goto(x,50)
  spider.pendown()
  spider.begin_fill()
  spider.fillcolor("red")
  spider.circle(5)
  spider.end_fill()
  x-=10

for i in range(4):
  spider.goto(0,20)
  spider.setheading(degrees*0.5*iteration)
  spider.forward(leg_length)
  iteration = iteration + 1

for i in range(4):
  spider.penup()
  spider.goto(0,20)
  spider.pendown()
  spider.setheading(-degrees*0.5*iteration)
  spider.forward(leg_length)
  iteration = iteration + 1
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()