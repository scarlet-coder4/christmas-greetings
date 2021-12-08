#CHRISTMAS WISHES ✨✨✨✨✨✨

import turtle
turtle.hideturtle()
turtle.delay(20)
turtle.bgpic("49346.gif")
turtle.pen(pencolor="green", pensize=4)
i=1

#THE TREE ✨✨✨✨✨✨

while(i<=4):         #down the tree
    turtle.setheading(300)
    if(i==1):
        turtle.forward(55)
    else:
        turtle.forward(50)
    turtle.setheading(0)
    turtle.backward(15)
    i+=1
turtle.backward(100)
i=1
while(i<=4):          #up the tree
    turtle.setheading(60)
    if(i==4):
        turtle.forward(55)
    else:
        turtle.forward(50)
    if(i!=4):
        turtle.setheading(0)
        turtle.backward(15)
    i+=1

#TREE TOPPER ✨✨✨✨✨✨

turtle.pencolor("yellow")
turtle.write("🌟",align="center",font=('Comic Sans MS', 20, 'normal'))

#FOR MERRY CHRISTMAS ✨✨✨✨✨✨

turtle.up()
turtle.setheading(90)
turtle.forward(60)
turtle.pencolor("red")

text="MERRY CHRISTMAS"
turtle.setheading(0)
turtle.backward(150)
for e in text:
    turtle.write(e, font=('Comic Sans MS', 25, 'bold'))
    turtle.forward(28)

#FOR BY MAHIMA ✨✨✨✨✨✨

turtle.backward(255)
turtle.setheading(270)
turtle.forward(25)
turtle.pencolor("black")
turtle.write("~by mahima",font=('Comic Sans MS', 15, 'normal'))

#FOR TIS THE SEASON ✨✨✨✨✨✨

turtle.forward(257)
turtle.setheading(180)
turtle.forward(130)
turtle.setheading(270)
turtle.pencolor("yellow")
turtle.write("✨",font=('Comic Sans MS', 15, 'bold'))
turtle.pencolor("blue")
turtle.write("      Tis' the season to be jolly",font=('Comic Sans MS', 15, 'normal'))
turtle.forward(20)
turtle.write("Deck the halls with boughs of holly",font=('Comic Sans MS', 15, 'normal'))
turtle.setheading(0)
turtle.forward(335)
turtle.pencolor("yellow")
turtle.write("✨",font=('Comic Sans MS', 15, 'bold'))

#FINISH ✨✨✨✨✨✨

turtle.exitonclick()