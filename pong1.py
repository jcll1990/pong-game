import turtle

wn = turtle.Screen()
wn.title("Pong by JC")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:0    Player B : 0", align="center", font=("Courier", 24 , 'normal'))

PAS = 0
PBS = 0


def paddle_a_up():
    if paddle_a.ycor() < 250:
        y = paddle_a.ycor()
        y += 25
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() > -250:
        y = paddle_a.ycor()
        y -= 25
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < 250 :
        y = paddle_b.ycor()
        y += 25
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -250 :
        y = paddle_b.ycor()
        y -= 25
        paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        PAS += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}    Player B : {}".format(PAS, PBS), align="center", font=("Courier", 24 , 'normal'))

    if ball.xcor() < -390:
        PBS +=1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}    Player B : {}".format(PAS, PBS), align="center", font=("Courier", 24 , 'normal'))

    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor () -50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor () -50):
        ball.setx(-340)
        ball.dx *= -1