from turtle import Turtle as T, Screen

t1 = T()
t1.shape("turtle")

for _ in range(5):
    t1.forward(10)
    t1.penup()
    t1.forward(10)
    t1.pendown()

window = Screen()
window.canvwidth = 800
window.canvheight = 500
window.exitonclick()
