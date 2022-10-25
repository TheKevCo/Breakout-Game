from turtle import Turtle

STARTING_X = 0
STARTING_Y = 0
MOVE_INCREMENT = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.goto(STARTING_X, STARTING_Y)
        self.speed(2)
        self.x_dir = 1
        self.y_dir = 1

    def move(self):
        position_x = self.xcor()
        position_y = self.ycor()
        new_x = self.xcor() + (MOVE_INCREMENT * self.x_dir)
        new_y = self.ycor() - (MOVE_INCREMENT * self.y_dir)
        self.goto(new_x, new_y)
        # if position_x > 270:
        #     self.x_dir *= -1
        # elif position_x <= -275:
        #     self.x_dir *= -1
        # if position_y >= 434:
        #     self.y_dir *= -1
        # if position_y <= -434:
        #     self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1

    def bounce_y(self):
        self.y_dir *= -1
