from Snake_body import Snake
from turtle import Screen
from time import sleep
from score_board import ScoreBoard
from food import Food
import winsound
from playsound import playsound
from pygame import mixer

# Screen Setup
screen = Screen()
screen.listen()
screen.title("Snake Game")
width, height = 400, 300
screen.screensize(width, height)
screen.bgcolor("Black")

# Snake initialization
snake = Snake()
screen.tracer(0)

# ScoreBoard Setup
score_board = ScoreBoard((0, height - 50))

# Food Object initialization
food = Food()

# Music initialization
mixer.init()
while True:
    sleep(0.1)
    snake_x, snake_y = snake.head_pos()
    if abs(snake_x) >= 330 or abs(snake_y) >= 270 or snake.check_head_with_body_collision():
        score_board.game_over()
        mixer.music.load("sound_effects/game-over-arcade.mp3")
        mixer.music.play()
        break

    if food.distance(snake.head_pos()) <= 30:
        mixer.music.load("sound_effects/snake_bite.mp3")
        mixer.music.play()
        food.respawn()
        snake.create_segment()
        score_board.update_score()
    screen.onkeypress(snake.right, 'd')
    screen.onkeypress(snake.left, 'a')
    screen.onkeypress(snake.up, 'w')
    screen.onkeypress(snake.down, 's')
    snake.move()
    screen.update()

screen.mainloop()
