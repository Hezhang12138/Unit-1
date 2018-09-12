import turtle


for x in range(8):
    turtle.forward(100)
    turtle.left(45)

fillcolor('#00CCFF')

turtle.setx(-300)
turtle.sety(-300)

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.setx(200)
turtle.sety(200)

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.setx(200)
turtle.sety(-200)

for x in range(8):
    turtle.forward(100)
    turtle.left(45)