from turtle import Turtle
import time

INITIAL_STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


# classes for the game so far


# classes have attributes and methods

# initialising attributes involves using the __init__ function

class Snake:

    def __init__(self):
        self.current_snake = []
        self.snake_body_generator()
        self.head = self.current_snake[0]

    def snake_body_generator(self):


        for pos in INITIAL_STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self,pos):
        snake_segment = Turtle('square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(pos)
        print(snake_segment.position())
        self.current_snake.append(snake_segment)

    def extend(self):
        self.add_segment(self.current_snake[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.current_snake) - 1, 0, -1):
            print(seg_num)
            new_position = self.current_snake[seg_num - 1].position()
            self.current_snake[seg_num].goto(new_position)
        self.current_snake[0].forward(20)

    def up(self):
        head = self.current_snake[0]
        if head.heading() != DOWN:
            head.setheading(90)

    def down(self):
        head = self.current_snake[0]
        if head.heading() != UP:
            head.setheading(270)

    def left(self):
        head = self.current_snake[0]
        if head.heading() != RIGHT:
            head.setheading(0)

    def right(self):
        head = self.current_snake[0]
        if head.heading() != LEFT:
            head.setheading(180)
