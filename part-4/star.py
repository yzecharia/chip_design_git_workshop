from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(50)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
write("May the force be with you!", align="right")
exitonclick()

