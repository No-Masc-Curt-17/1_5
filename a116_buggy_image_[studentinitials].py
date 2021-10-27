#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
leg = 6
leg_length = 70
degrees = 380 / leg
spider.pensize(5)
iteration = 0
while (iteration < leg):
  spider.goto(0,0)
  spider.setheading(degrees*iteration)
  spider.forward(leg_length)
  iteration = iteration + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()