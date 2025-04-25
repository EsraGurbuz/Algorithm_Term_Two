import turtle

polygons = int(input("Enter a polygons value: "))
length = polygons * 10
angle = 360 / polygons

if polygons < 3:
    print("A polygon must have at least 3 sides!")
    exit()

wn = turtle.Screen()
wn.bgcolor("DarkSlateGrey")
wn.title("Hello, Tosbik")

keratta = turtle.Turtle()
keratta.color("light salmon")
keratta.pensize(3)

def draw_polygons(keratta, side_length, sides):
    for i in range(sides):
        keratta.forward(side_length)
        keratta.left(360 / sides)

draw_polygons(keratta, length, polygons)

wn.mainloop()