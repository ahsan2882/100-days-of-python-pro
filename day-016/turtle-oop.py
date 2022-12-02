from turtle import Turtle, Screen

turtle1 = Turtle()
myScreen = Screen()
myScreen.canvheight = 300
myScreen.canvwidth = 300

turtle1.shape("turtle")
turtle1.color("coral")
turtle1.forward(100)

myScreen.exitonclick()
