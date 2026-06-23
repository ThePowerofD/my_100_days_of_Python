from turtle import *
import random

franklin = Turtle()
tim = Turtle()

colors = ["bisque3", "black", "chartreuse2", "cyan2", "DeepPink1"]
dir = [0,90,180,270]
steps = int(input("How many steps do you want: "))

franklin.shape("turtle")
franklin.color("cyan4")
franklin.left(90)
franklin.speed(1)

def randomWalk(colorChoice,directions,steps):
    directions = directions
    speed = float(1)
    speed_increment = float(10/steps)
    newSpeed = speed
    for _ in range(steps):
        franklin.color(random.choice(colorChoice))
        franklin.left(random.choice(directions))
        franklin.fd(25)
        newSpeed += speed_increment
        franklin.speed(newSpeed)
        
        print(newSpeed)

randomWalk(colors,dir,steps)





screen = Screen()
screen.exitonclick()