import turtle as t
import random

t.speed(0)

t.penup()
t.goto(-300, 150)
t.pendown()
t.color("red")

for _ in range(4):
    t.forward(80)
    t.left(90)

t.penup()
t.goto(-150, 150)
t.pendown()
t.color("green")

for _ in range(3):
    t.forward(80)
    t.left(120)

t.penup()
t.goto(50, 150)
t.pendown()
t.color("blue")

for _ in range(5):
    t.forward(60)
    t.left(72)


t.penup()
t.goto(-100, -100)
t.pendown()
t.color("black", "yellow")

t.begin_fill()
for _ in range(4):
    t.forward(150)
    t.left(90)
t.end_fill()

t.color("black", "red")
t.begin_fill()

t.left(30)
for _ in range(3):
    t.forward(150)
    t.left(120)

t.end_fill()





t.penup()
t.goto(200, -50)
t.pendown()

colors = ["red", "blue", "green", "orange", "purple", "black", "pink"]

for _ in range(36):
    t.color(random.choice(colors))

    for _ in range(4):
        t.forward(70)
        t.left(90)

    t.right(10)


t.hideturtle()
t.done()