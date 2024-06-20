from turtle import *

#draw a house

#draw a square

width(7)
color(red)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#draw a door

forward(70)
color(yellow)
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()

color(blue)
begin_fill()
roght(150)
forward(200)
left(120)
forward(200)

#draw 1st window
color(black)
begin_fill()
penup()
goto(30,0)
pendown()
 #draw 2nd window
color(black)
begin_fill()
penup()
goto(-70,0)
pendown()

exitonclick()
