import turtle
from turtle import Screen
import winsound
import math

#global variables
game_is_playing = True
score1 = 0
score2 = 0
speed= 2
step =2
paddle_speed = 3
x_position =1
y_position =1
ball = turtle.Turtle()
left_paddle = turtle.Turtle()
right_paddle = turtle.Turtle()
screen = Screen()

#screen properties
screen.bgcolor("black")
screen.screensize(400,400)
screen.setup(450,450)

#ball properties
def initialize_ball():
    ball.penup()
    ball.color("white")
    ball.shape("circle")
    ball.shapesize(1.5,1.5,1.5)
    ball.goto(0,0)
    
#for score board
score_board = turtle.Turtle()
score_board.hideturtle()
score_board.color("white")
score_board.shape("square")
score_board.penup()
score_board.goto(0, 180)

def write_score():
    global score_board
    score_board.clear()
    score_board.write(f'Player 1: {int(score1)} \nPlayer 2: {int(score2)}', align="center", font=("Times New Roman", 15 , "bold"))

def draw_left_paddle():
    left_paddle.penup()
    left_paddle.goto(-200,0)
    left_paddle.shape("square")
    left_paddle.color("white")
    left_paddle.shapesize(1,3,1)
    left_paddle.setheading(90)
    
def draw_right_paddle():
    right_paddle.penup()
    right_paddle.goto(200,0)
    right_paddle.shape("square")
    right_paddle.color("white")
    right_paddle.shapesize(1,3,1)
    right_paddle.setheading(90)
    
def move_ball():
    global step
    global speed
    global x_position
    global y_position
    x_position = ball.setx(ball.xcor() + step )
    y_position = ball.sety(ball.ycor() + speed )
       
def play_collision_sound():
    winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
def detect_collision_with_paddle():
    global step
    global score1
    global score2
    
    # Check collision with right paddle
    if ball.distance(right_paddle)<50:
        play_collision_sound()
        step *= -1  
        score1 += 1
        write_score()

    # Check collision with left paddle
    if ball.distance(left_paddle)<50:
        play_collision_sound()
        step *= -1  
        score2 += 1  
        write_score()
      
def detect_collision_with_wall():
    global speed
    if ball.xcor()> 200 or ball.xcor() < -200:
        speed *=-1 
    elif ball.ycor()> 200 or ball.ycor() < -200:
         speed *=-1

def right_paddle_go_down():
    if right_paddle.ycor()>-180:
        right_paddle.backward(paddle_speed)
     
def right_paddle_go_up():
    if right_paddle.ycor()<180:
        right_paddle.forward(paddle_speed)

def left_paddle_go_down():
    if left_paddle.ycor()>-180:
        left_paddle.backward(paddle_speed)
     
def left_paddle_go_up():
    if left_paddle.ycor()<180:
        left_paddle.forward(paddle_speed)

def set_level():
    global score2
    global score1
    global speed
    global step
    if score1>=50 or score2>=50:
        speed+=1
        step+=1   
        score1=0
        score2=0
screen.listen()
screen.onkeypress(right_paddle_go_up , "Up")
screen.onkeypress(right_paddle_go_down , "Down")
screen.onkeypress(left_paddle_go_up , "w")
screen.onkeypress(left_paddle_go_down , "s")

initialize_ball()
write_score()
draw_left_paddle()
draw_right_paddle()

while game_is_playing:
    
    move_ball()
    detect_collision_with_paddle()
    detect_collision_with_wall()
    set_level()
screen.exitonclick()