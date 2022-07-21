from turtle import Turtle
import random
COLORS = ['white']

class Snake:
    def __init__(self):
        self.segments = []
        self.create_segment()
        self.head = self.segments[0]

    def create_segment(self):
        temp = Turtle()
        temp.penup()
        temp.shape("square")
        temp.color(random.choice(COLORS))
        temp.shapesize(1.5, 1.5)
        self.segments.append(temp)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for it in range(len(self.segments) - 1, 0, -1):
            self.segments[it].goto(self.segments[it - 1].position())
        self.head.forward(30)

    def head_pos(self):
        return self.head.position()

    def check_head_with_body_collision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg.position()) <= 20:
                return True
        return False