from turtle import *

#we want to paint house 

#step 1:  draw a square
#speed(10)
shape("turtle")
color("red")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of square
#drawing door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(150, 90)
pendown()

color("green")
begin_fill()
right(150)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

penup()
goto(20, 90)
pendown()

color("green")
begin_fill()
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)
forward(35)
end_fill()

exitonclick()

