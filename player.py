from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.left(90)

    def turtle_position(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def forwards(self):
        self.forward(MOVE_DISTANCE)

    def backwards(self):
        self.back(MOVE_DISTANCE)

    def move(self):
        self.screen.listen()
        self.screen.onkey(self.forwards, "Up")
        self.screen.onkey(self.backwards, "Down")
