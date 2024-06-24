from turtle import Turtle, Screen

screen = Screen()


# paddle = Turtle()
# paddle2 = Turtle()

class Paddle(Turtle):
    def __init__(self, position):
        # self.paddle1()
        # self.paddle3()

        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def paddle3(self):
    #
    #         paddle2.color("white")
    #         paddle2.shape("square")
    #         paddle2.speed("fastest")
    #         paddle2.shapesize(stretch_wid=5, stretch_len=1)
    #         paddle2.penup()
    #         paddle2.goto(x=-550,y=0)
    #
    # def go_up2(self):
    #     new_y = paddle2.ycor() + 40
    #     paddle2.goto(paddle2.xcor(), new_y)
    # def go_down2(self):
    #     new_y = paddle2.ycor() - 40
    #     paddle2.goto(paddle2.xcor(), new_y)
    #
    #
