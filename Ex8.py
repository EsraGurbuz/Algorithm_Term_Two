import turtle

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

wn = turtle.Screen()
wn.title("Drunk Pirate's Path")

pirate = turtle.Turtle()
pirate.color("blue")
pirate.pensize(2)

for angle in angles:
    pirate.left(angle)  
    pirate.forward(100)  

wn.exitonclick()
