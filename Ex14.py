import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)


def draw_square(size):
    for i in range(4):
        keratta.forward(size)
        keratta.left(90)

for i in range(5):
    draw_square(20)
    keratta.penup()
    keratta.forward(40)
    keratta.pendown()

wn.mainloop()