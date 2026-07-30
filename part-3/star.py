from turtle import *
shape("turtle")
delay(5)
color('green', 'blue')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()

