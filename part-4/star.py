from turtle import *
speed(10)
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
write("May the force be with you!", align="right")
exitonclick()

