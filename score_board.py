from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_mid):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.shape("square")
        self.goto(*screen_mid)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Arial", 25, "bold"))
