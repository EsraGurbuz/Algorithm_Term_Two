import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

tosbik = turtle.Turtle()
tosbik.color("MistyRose")
tosbik.pensize(2)

for i in range(3):
    keratta.forward(80)
    keratta.left(120)

for j in range(4):
    tosbik.forward(50)
    tosbik.left(90)

wn.mainloop()