#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
#size of body
spider.circle(20)
#number of legs
leg = 6
#length of each leg
leg_length = 70
#amount of degrees between legs
degrees = 380 / leg
spider.pensize(5)
iteration = 0
#making the legs
while (iteration < leg):
  spider.goto(0,0)
  spider.setheading(degrees*iteration)
  spider.forward(leg_length)
  iteration = iteration + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()