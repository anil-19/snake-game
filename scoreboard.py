from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('courier', 25, 'normal')

class ScoreBoard(Turtle):
    with open('data.txt', mode='r') as file:
        HIGH_SCORE = int(file.read())
        #if HIGH_SCORE.isdigit():
         #   integer = int(HIGH_SCORE)
    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = self.integer
        self.color('white')
        self.penup()
        self.goto(10, 270)
        self.hideturtle()
        self.Update()

    def increment(self):
        self.score = self.score + 1
        self.Update()

    def reset(self):
        if self.score > self.HIGH_SCORE:
            self.HIGH_SCORE = self.score
            with open('data.txt', mode='w') as file:
                self.SCORE = str(self.score)
                file.write(self.SCORE)
        self.score = 0
        self.Update()
    def Update(self):
        self.clear()
        self.write(f"Score: {self.score} , HighScore: {self.HIGH_SCORE}", align=ALIGNMENT, font=FONT)