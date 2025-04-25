import turtle
wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

# Without list, one by one
for c in ["yellow", "red", "purple", "blue"]:
    keratta.color(c)
    keratta.forward(50)
    keratta.left(90)

keratta.penup()
keratta.forward(100)     # This moves keratta, but no line is drawn
keratta.pendown()

# Assign a list to a variable
clrs = ["yellow", "red", "purple", "blue"]
for c in clrs:
    keratta.color(c)
    keratta.forward(50)
    keratta.left(90)

wn.mainloop()
