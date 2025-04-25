import turtle
import random
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)
colors = ("red", "orange", "yellow", "green", "blue", "purple")

for i in range(random.randint(50,100)):
    keratta.pensize(random.randint(1,10))
    keratta.color(random.choice(colors))
    keratta.forward(random.randint(1,10))
    keratta.left(random.randint(1,270))