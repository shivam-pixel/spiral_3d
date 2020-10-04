import turtle
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
list=["red","blue","yellow","orange","pink"]
for i in range(500):
    t.color(list[i%5])
    t.circle(15+i)
    t.clone()
    t.forward(i+5)
    t.circle(i+2)
    t.pensize(3)
    t.left(180)
    t.speed(0000)
