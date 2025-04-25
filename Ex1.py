import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

for i in range(4):
    keratta.forward(50)
    keratta.left(90)

wn.mainloop()