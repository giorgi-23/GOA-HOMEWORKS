from turtle import *
#step 1:   draw a square

speed(60)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square


#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #heigth of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,  200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()



color("brown")
begin_fill()
left(30)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
end_fill()




penup()
goto(200, 200)
pendown()



begin_fill()
forward(50)
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
end_fill()





exitonclick()