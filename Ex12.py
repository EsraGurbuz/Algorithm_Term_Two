import turtle
import random
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

colors = ("red", "orange", "yellow", "green", "blue", "purple")
size = 10
angle = 80

for i in range(80):
    keratta.forward(size)
    keratta.left(angle)
    keratta.color(random.choice(colors))
    size = size + 2
    angle = angle - 1

wn.mainloop()