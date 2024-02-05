#simple pong in python3 for beginners
#By digonto
#part 1

import turtle 

wind = turtle.Screen()
wind.title("PINGPONG @DIGS")
wind.bgcolor("green")
wind.setup(width=800,height=600)
wind.tracer(0)


#paddle a
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-360,0)
#paddle b
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(360,0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .1
ball.dy = .1

#function
def paddle_a_up():
    y= paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


def paddle_b_down():
    y= paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#keyboard binding
wind.listen()
wind.onkeypress(paddle_a_up,"w")
wind.onkeypress(paddle_a_down,"s")
wind.onkeypress(paddle_b_up,"Up")
wind.onkeypress(paddle_b_down,"Down")

 #main game loop
while True:
  wind.update()


  #move the ball
  ball.setx(ball.xcor()+ball.dx)
  ball .sety(ball.ycor() +ball.dy)

  #border checking
  if ball.ycor()>290:
    ball.sety(290)
    ball.dy *=-1
  if ball.ycor()<-290:
    ball.sety(-290)
    ball.dy *=-1

  if ball.xcor()<-390:
    ball.goto(0,0)
    ball.dx *=-1

  if ball.xcor()>390:
    ball.goto(0,0)
    ball.dx *=-1
  
  #paddle and ball collisions
  if (ball.xcor()> 340 and ball.xcor()<350) and (ball.ycor()< paddle_b.ycor() +40 and ball.ycor()>paddle_b.ycor()-40):
    ball.setx(340)
    ball.dx *=-1

  if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddle_a.ycor() +40 and ball.ycor()>paddle_a.ycor()-40):
    ball.setx(-340)
    ball.dx *=-1
    