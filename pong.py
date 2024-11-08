#getting started
import turtle
import random
import tkinter
from tkinter import *

wn=turtle.Screen()
wn.title("Pong by ENTHS")
wn.bgcolor("midnight blue")
wn.setup(width=800,height=600)
wn.tracer(0)



#Score
score_a=0
score_b=0



# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("tomato")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)



# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("tomato")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)



# Ball
ball=turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
#speed of the ball
dispersement=[0.3,-0.3]
rd=random.choice(dispersement)
ball.dx=rd
ball.dy=-rd


# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center", font=("arial", 24,"normal"))



# Function for paddle_a up
def paddle_a_up():
     y=paddle_a.ycor()
     y+=20
     paddle_a.sety(y)



# Function for paddle_a down
def paddle_a_down():
     y=paddle_a.ycor()
     y-=20
     paddle_a.sety(y)



# Keyboard binding
wn.listen()

wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_up,"W")

wn.onkeypress(paddle_a_down,"s") 
wn.onkeypress(paddle_a_down,"S")


# Function for paddle_b up
def paddle_b_up():
     y=paddle_b.ycor()
     y+=20
     paddle_b.sety(y)



# Function for paddle_a down
def paddle_b_down():
     y=paddle_b.ycor()
     y-=20
     paddle_b.sety(y)



# Keyboard binding
wn.listen()

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


#diving line




#main game loop
while True:
    wn.update()

    # Moving the ball
    ball.setx(ball.xcor()-ball.dx)
    ball.sety(ball.ycor()-ball.dy)

    # Top-Border checking
    if ball.ycor()>290:
         ball.sety(290)
         ball.dy*=-1
    
    #Bottom-Border checking
    if ball.ycor()<-290:
         ball.sety(-290)
         ball.dy*=-1
     
    # Right-Border checking
    if ball.xcor()>390:
         ball.goto(0,0)
         ball.dx*=-1
         score_a+=1
         pen.clear()
         pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center", font=("Arial", 24,"normal"))
    
    # Left-Border checking
    if ball.xcor()<-390:
         ball.goto(0,0)
         ball.dx*=-1
         score_b+=1
         pen.clear()
         pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center", font=("Courier", 24,"normal"))

    # Right_Paddle Ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and ((ball.ycor()<paddle_b.ycor()+40) and (ball.ycor()>paddle_b.ycor()-50)):
         ball.setx(340)
         ball.dx*=-1

    # Left_Paddle Ball collision
    if (ball.xcor()<-340 and ball.xcor()>-350) and ((ball.ycor()<paddle_a.ycor()+40) and (ball.ycor()>paddle_a.ycor()-50)):
         ball.setx(-340)
         ball.dx*=-1
