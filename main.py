import pygame
from pygame.locals import *
from sys import exit
import random

ball_x = 10
ball_y = 10
basket_x = 0
basket_y = 600
screen_width = 1920
screen_height = 1080
score = 0

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('catch the ball by Rick')
basket = pygame.image.load('C:/Users/rguo2/Pictures/PYTHON/basket2.jpg').convert()
basket_w, basket_h = basket.get_size()
ball = pygame.image.load('C:/Users/rguo2/Pictures/PYTHON/Ball4.webp').convert()
ball_w, ball_h = ball.get_size()


def update_basket():
    global basket_x
    global basket_y
    basket_x, ignore = pygame.mouse.get_pos()  # Detect mouse events
    basket_x = basket_x - basket_w / 2
    screen.blit(basket, (basket_x, basket_y))


def update_ball():
    global ball_x
    global ball_y
    ball_y += 1
    if ball_y + ball_h > basket_y:
        ball_y = 0
        ball_x = random.randint(0, screen_width - ball_w)

    ball_x += random.randint(-1, 1)
    if ball_x <= 0:
        ball_x = 0
    if ball_x >= screen_width - ball_w:
        ball_x = screen_width - ball_w
    screen.blit(ball, (ball_x, ball_y))


def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, (255, 255, 255))
    screen.blit(text, (0, 0))


def check_for_catch():
    global score
    if ball_y + ball_h == basket_y and basket_x < ball_x < basket_x + basket_w - ball_w:
        score += 1
    display('score:' + str(score))


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((0, 0, 0))
    update_ball()
    update_basket()
    check_for_catch()
    pygame.display.update()
    clock.tick(1000)  # lower if too fast
