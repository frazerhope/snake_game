from turtle import Turtle

with open('Data.txt', 'r') as score:
    current_score = score.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        with open('Data.txt') as data:
            current_data  = data.read()
            current_data = int(current_data)
            self.high_score = current_data
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 30, 'normal'))

    def score_refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def high_score_update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode="w") as data:
                data.write(f"{self.high_score}")


    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 50, 'normal'))
