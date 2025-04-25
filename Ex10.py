import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)
keratta.shape("arrow") 

size = 20 
for i in range(40):
    keratta.left(90)
    keratta.forward(size)
    size += 5