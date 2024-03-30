import pygame
from pygame.locals import *
import random

from datetime import datetime

start_time = datetime.today().second

player_x = 200
player_y = 200

player_score = 0


def player_movement():
    global player_x, player_y
    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        player_x = player_x + 3

    if key[pygame.K_LEFT]:
        player_x = player_x - 3

    if key[pygame.K_UP]:
        player_y = player_y - 3

    if key[pygame.K_DOWN]:
        player_y = player_y + 3


fruit_x = 50
fruit_y = 50


def display_score():
    font = pygame.font.Font("fonts\Sevillana-Regular.ttf", 36)
    #                                                                  R    G    B
    text = font.render("Player Score: {}".format(player_score), True, (12, 245, 39))
    screen.blit(text, (0, 0))


def display_remaining_time():
    global start_time, player_score
    current_time = datetime.today().second

    font = pygame.font.Font("fonts\Sevillana-Regular.ttf", 36)
    #                                                                           R    G    B
    time_counter = (current_time - start_time)
    text = font.render("Remaining Time: {}".format(5 - time_counter), True, (12, 245, 39))
    # print(time_counter)
    if time_counter == 5 or time_counter < 0:
        start_time = datetime.today().second
        player_score = player_score - 1
        # print("updated")
    screen.blit(text, (330, 0))


def displaying():
    screen.blit(background_image, (0, 0))
    screen.blit(my_fruit, (fruit_x, fruit_y))
    screen.blit(my_player, (player_x, player_y))

    display_score()
    display_remaining_time()
    pygame.display.update()


def check_collision():
    global fruit_x, fruit_y, player_score, start_time
    player_rect = my_player.get_rect(topleft=[player_x, player_y])

    fruit_rect = my_fruit.get_rect(topleft=[fruit_x, fruit_y])

    if fruit_rect.colliderect(player_rect):
        fruit_x = random.randint(1, 550)
        fruit_y = random.randint(1, 550)

        player_score = player_score + 1
        start_time = datetime.today().second
        print("Player Score: {}".format(player_score))


# initialize our package

pygame.init()

screen = pygame.display.set_mode((600, 600))

app_icon = pygame.image.load(r"images\icon.png")

pygame.display.set_icon(app_icon)

pygame.display.set_caption("Eating Fruits")

background_image = pygame.image.load(r"images\background.jpg")

my_player = pygame.image.load(r"images\frog.png")
my_player = pygame.transform.scale(my_player, (70, 70))

my_fruit = pygame.image.load(r"images\fruit.png")
my_fruit = pygame.transform.scale(my_fruit, (70, 70))

app_running = True

while app_running:  # Forever = Infinite Loop

    for event in pygame.event.get():  # list of events
        if event.type == QUIT:
            app_running = False
            break

    player_movement()

    check_collision()

    displaying()