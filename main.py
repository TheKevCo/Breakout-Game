from turtle import Screen, Turtle
from player import Player
from board import Board
from ball import Ball
import time

screen = Screen()
screen.title('Breakout!')
screen.setup(width=600, height=900)
screen.bgcolor('black')
player = Player()
board = Board()
ball = Ball()
screen.listen()
screen.onkeypress(player.move_up, key="Right")
screen.onkeypress(player.move_down, key="Left")
list_blocks = []
game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(0.01)

    # ball bounce mechs with walls
    if ball.xcor() > 270:
        ball.bounce_x()
    elif ball.xcor() < -285:
        ball.bounce_x()
    if ball.ycor() > 434:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(player) < 60 and ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with block
    for block in board.rows:
        if ball.distance(block) < 50 and ball.ycor() > (block.ycor() - 30):
            ball.bounce_y()
            Turtle.hideturtle(block)
            block.goto(400, block.ycor())
            list_blocks.append(block)

    # this code below is game over
    if ball.ycor() < -434:
        board.game_over()
        game_on = False
    elif len(list_blocks) == 35:
        board.win()
        game_on = False

screen.exitonclick()
