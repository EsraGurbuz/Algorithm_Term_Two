import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)
keratta.shape("turtle") 
#Every turtle can have its own shape. The ones available “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
keratta.speed(10)
#Speed settings can be set between 1 (slowest) to 10 (fastest).

keratta.penup()                # This is new
size = 20
for i in range(30):
   keratta.stamp()             # Leave an impression on the canvas
   size = size + 3             # Increase the size on every iteration
   keratta.forward(size)       # Move keratta along
   keratta.right(24)           #  ...  and turn her

"""
keratta.shape("arrow")
size = 30
for i in range(30):
   keratta.stamp()             # Leave an impression on the canvas
   size = size + 3             # Increase the size on every iteration
   keratta.forward(size)       # Move keratta along
   keratta.left(24)           #  ...  and turn her
"""

wn.mainloop()