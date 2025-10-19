import turtle
import time

speed = 0

def go_left():
   t.seth(180)
   t.fd(3)

def go_right():
   t.seth(0)
   t.fd(3)

def go_up():
   t.seth(90)
   t.fd(3)

def go_down():
   t.seth(270)
   t.fd(3)

screen = turtle.Screen()
screen.setup(400, 300)
screen.tracer(0,0)
t = turtle.Turtle()
t.shape("turtle")
t.pu()
f = turtle.Turtle()
f.pu()
f.shape("circle")
f.color("gold")
f.goto(0,150)
f.seth(-90)
p = turtle.Turtle()
p.shape("triangle")
p.color("purple")
p.pu()


screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.listen()


while True:
   if speed > 0:
       speed-= 0.1
   if f.distance(t) < 20:
        f.sety(150)
   if p.distance(t) < 20:
        p.sety(150)  
   screen.update()
   time.sleep(0.0166)
   f.forward(1)




