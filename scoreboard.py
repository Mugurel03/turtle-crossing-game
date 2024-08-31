from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.score_board = Turtle()
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.goto(-280, 250)

    def write_score(self):
        self.score_board.clear()
        self.score_board.write(f"Level {self.score}", False, align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_game_over(self):
        self.score_board.clear()
        self.score_board.goto(0, 0)
        self.score_board.write("Game Over", align='center', font=FONT)
