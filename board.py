from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]

ROW_INCREMENT = (85, 25)
STARTING_X = -258
STARTING_Y = 260


class Board:
    def __init__(self):
        self.rows = []
        self.row_creation()

    def row_creation(self):
        for y in range(5):
            for i in range(7):
                block = Turtle()
                block.shape("square")
                block.speed(10)
                block.penup()
                block.color(COLORS[y])
                block.shapesize(stretch_wid=1, stretch_len=4)
                block.goto((STARTING_X + (ROW_INCREMENT[0] * i)), (STARTING_Y + (ROW_INCREMENT[1] * y)))
                self.rows.append(block)

    def game_over(self):
        over = Turtle()
        over.color('white')
        over.write("Game Over")
        over.hideturtle()

    def win(self):
        over = Turtle()
        over.color('white')
        over.write("You Won!")
        over.hideturtle()
