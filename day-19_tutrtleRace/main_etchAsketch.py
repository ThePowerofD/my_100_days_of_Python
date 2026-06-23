from turtle import *

frank = Turtle()
screen = Screen()
frank.shape("turtle")
frank.color("PaleGreen1")

def move_forward():
    frank.fd(10)
def move_backwards():
    frank.bk(10)
def tilt_left():
    frank.lt(10)
def tilt_right():
    frank.rt(10)
def clear_baord():
    frank.reset()
    frank.color("PaleGreen1")


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=tilt_left)
screen.onkey(key="d", fun=tilt_right)
screen.onkey(key="c",fun=clear_baord)

screen.exitonclick()



#TODO W = Forward/ s = Backwards/ A = Counter Clowck / D = Clockwise
#TODO C = Cleat drawing and turtle in the center

# Keyword arguments exampple = 
# my_function=(c=3,a=1,b=2)