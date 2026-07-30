import math
from turtle import *
def star(cx, cy, side=200, turn=170):
    dy = (side / 2) / math.tan(math.radians(turn / 2))
    penup()
    goto(cx - side / 2, cy - dy)
    setheading(0)
    pendown()

    start = pos()
    begin_fill()
    while True:
        forward(side)
        left(turn)
        if distance(start) < 1:
            break
    end_fill()

color('green', 'blue')
star(-220, 0)
star(0, 0)
star(220, 0)

exitonclick()
