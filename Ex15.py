"""import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)
keratta.speed(3)

def draw_spiral_square(start_size, step, count):
    size = start_size
    for i in range(count):
        for k in range(4):
            keratta.forward(size)
            keratta.left(90)
        size += step
    keratta.penup()
    keratta.goto(-100, -100)
    keratta.pendown()


keratta.penup()
keratta.goto(-50, -50)
keratta.pendown()

draw_spiral_square(20, 20, 5)

wn.mainloop()
"""
