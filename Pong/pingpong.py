#Pong game in python
import turtle
import os

wn=turtle.Screen()
wn.title("Pong by Monkey D Luffy")
wn.bgcolor('#070d59')
wn.setup(width=800,height=600)
wn.tracer(0) # speeds up the game


#Ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1 #moving ball by 0.9 pixels

#scores

score_a = 0
score_b = 0 

# game title

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #length of the paddle
paddle_a.penup()
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #length of the paddle
paddle_b.penup()
paddle_b.goto(350,0)


#Functionalities of the paddle

def paddle_a_up():
    y=paddle_a.ycor() # gets the coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor() # gets the coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor() # gets the coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor() # gets the coordinate
    y -= 20
    paddle_b.sety(y)

wn.listen() #input from the keyboard 
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
while True:
    wn.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    # padddle collision

    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    if (ball.xcor() < -340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")


    