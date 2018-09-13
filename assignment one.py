# Frank Zhang
# 9/13/18
# assignment one.py
# I have tried this assignment for many times, and finally succeed at last. In addition, this is my first program that I have everdone.



import turtle

turtle.color("black","red")
turtle.begin_fill()

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.end_fill()

turtle.penup()
turtle.goto(-300,-300)
turtle.pendown()

turtle.color("black","green")
turtle.begin_fill()

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.end_fill()

turtle.penup()
turtle.goto(200,200)
turtle.pendown()

turtle.color("black","yellow")
turtle.begin_fill()

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.end_fill()

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()

turtle.color("black","pink")
turtle.begin_fill()

for x in range(8):
    turtle.forward(100)
    turtle.left(45)

turtle.end_fill()

turtle.exitonclick()