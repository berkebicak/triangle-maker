import colorsys
import turtle

t= turtle.Turtle()
t.screen.bgcolor("black")

t.penup()
t.goto(-200,-100)
t.pendown()
t.speed(10)

a=400
h=0.2
n=50

def tri():
    global a,n,h
    for i in range(40):
        c = colorsys.hsv_to_rgb(h,0.5,0.4)
        h= h+(1/n)
        t.color(c)
        t.forward(a)
        t.left(120)
        a= a-10
tri()
tri()


t.hideturtle()
turtle.done()

