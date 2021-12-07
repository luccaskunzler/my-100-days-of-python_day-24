from turtle import Turtle


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        with open('high_score.txt', "r") as file:
            self.high_score = int(file.read())
        self.color('white')
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0,260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()