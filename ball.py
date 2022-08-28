from turtle import Turtle


class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.speeed=0.1


    def move_to(self):
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x_cor,y_cor)


    def bounce(self ):
        self.speeed*=0.9
        self.y_move*=-1

    def bounce_x(self):
        self.speeed*=0.9
        self.x_move*=-1



