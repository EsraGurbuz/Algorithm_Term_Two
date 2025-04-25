import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)
keratta.shape("arrow") 

size = 70
right = 144

keratta.left(72)
keratta.forward(size)
for i in range(4):
    keratta.right(right)
    keratta.forward(size)

