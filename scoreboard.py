from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        # ocultar el objeto toruga
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        # solo se llamara la primera ve<
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Couriel", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Couriel", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
