import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

keratta.penup()
keratta.backward(200)
keratta.pendown()

#An equilateral triangle
for i in range(3):
    keratta.forward(30)
    keratta.left(120)

keratta.penup()
keratta.forward(60)
keratta.pendown()
keratta.color("honeydew")

#A square
for i in range(4):
    keratta.forward(40)
    keratta.left(90)

keratta.penup()
keratta.forward(90)
keratta.pendown()
keratta.color("LavenderBlush")

#A hexagon
for i in range(6):
    keratta.forward(60)
    keratta.left(60)

keratta.penup()
keratta.forward(180)
keratta.pendown()
keratta.color("PeachPuff")

#An octagon
for i in range(8):
    keratta.forward(80)
    keratta.left(45)