from turtle import Turtle
STEPS = 20
direction = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create()
        self.last_position = ()

    def create(self):
        for _ in range(0,3):
            newsquare = Turtle(shape="square")
            newsquare.color('white')
            newsquare.penup()
            global direction
            newsquare.setheading(0)
            newsquare.setposition(_*-20,0)
            self.snake.append(newsquare)

    def move(self):
        self.last_position = self.snake[0].pos()
        self.snake[0].setheading(direction)
        self.snake[0].forward(STEPS)
        for i in range(1, len(self.snake)):
            previous_position = self.snake[i].pos()
            self.snake[i].setpos(self.last_position)
            self.last_position = previous_position
    
    def reset(self):
        for block in self.snake:
            block.goto(1000,1000)
        self.snake.clear()
        self.create()



    def plus_one(self):
        print("activated plus one")
        newsquare = Turtle(shape="square")
        newsquare.color('white')
        newsquare.penup()
        global direction
        newsquare.setheading(0)
        newsquare.setposition(self.snake[-1].position())
        self.snake.append(newsquare)

    def turn_up(self):
        global direction
        if direction != 270:
            direction = 90
        return direction

    def turn_right(self):
        global direction
        if direction != 180:
            direction = 0
        return direction

    def turn_left(self):
        global direction
        if direction != 0:
            direction = 180
        return direction

    def turn_down(self):
        global direction
        if direction != 90:
            direction = 270
        return direction