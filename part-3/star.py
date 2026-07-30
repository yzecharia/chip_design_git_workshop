from turtle import *
import random
pencolor([random.random() for i in range(3)])
shape("turtle")
delay(5)
width(8)
circle(150)
color('green', 'blue')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()

