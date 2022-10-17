# includes pause
import time

import pygame
import sys
import random
import pickle
from pygame.locals import *
from pygame import mixer
from pygame.surface import Surface, SurfaceType

pygame.init()
# All game needed variable
FPS = 15
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 5
SNAKE_WIDTH = 19
APPLE_SIZE = 19
FOOD_SIZE = 20
TOP_WIDTH = 40
high_s = 0
# Game Window or Canvas
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# music Initialization part
mixer.init()
mixer.music.load('bensound-summer_mp3_music (1).mp3')
sound = mixer.Sound("1_snake_game_resources_crash.mp3")
mixer.Sound.set_volume(sound, 0)
sound1 = mixer.Sound("1_snake_game_resources_ding.mp3")
mixer.Sound.set_volume(sound1, 0)
sound2 = mixer.Sound("mixkit-extra-bonus-in-a-video-game-2045.mp3")
mixer.Sound.set_volume(sound2, 0)
# Setting up font
small_font = pygame.font.SysFont('Courier New', 25)
medium_font = pygame.font.SysFont('Courier New', 20, True)
large_font = pygame.font.SysFont('Courier New', 40, True, True)

clock = pygame.time.Clock()

# Loading all the images need for game
bg_img1 = pygame.image.load("zldaLS2.jpg")
bg_img1 = pygame.transform.scale(bg_img1, (WINDOW_WIDTH, WINDOW_HEIGHT))
bg_img2 = pygame.image.load("background.jpg")
bg_img2 = pygame.transform.scale(bg_img2, (WINDOW_WIDTH, WINDOW_HEIGHT))
snake_img = pygame.image.load('snake.png')
apple_img = pygame.image.load('food.png')
food_img = pygame.image.load('big_apple.jpg')
tail_img = pygame.image.load('snake.png')
apple_img_rect = apple_img.get_rect()
food_img_rect = food_img.get_rect()

# Starting of game method and Logic

def start_game():  # Here we will build Home Screen button and logic for their work;;
    # canvas.fill(WHITE)
    canvas.blit(bg_img1, (0, 0))
    start_font1 = large_font.render("WELCOME TO SNAKE GAME", True, BLUE)
    start_font2 = medium_font.render("PLAY GAME", True, BLACK, GREEN)
    start_font3 = medium_font.render("INSTRUCTIONS", True, BLACK, GREEN)
    start_font4 = medium_font.render("QUIT", True, RED, GREEN)

    start_font1_rect = start_font1.get_rect()
    start_font2_rect = start_font2.get_rect()
    start_font3_rect = start_font3.get_rect()
    start_font4_rect = start_font4.get_rect()

    start_font1_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 200)
    start_font2_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 10)
    start_font3_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 70)
    start_font4_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 130)

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_font3_rect.left and x < start_font3_rect.right:
                    if y > start_font3_rect.top and y < start_font3_rect.bottom:
                        start_inst(start_font1, start_font1_rect)
                if x > start_font2_rect.left and x < start_font2_rect.right:
                    if y > start_font2_rect.top and y < start_font2_rect.bottom:
                        gameloop()
                if x > start_font4_rect.left and x < start_font4_rect.right:
                    if y > start_font4_rect.top and y < start_font4_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def start_inst(start_font1, start_font1_rect):  # This function is only for INSTRUCTION button;;
    canvas.fill(WHITE)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = small_font.render("* Do not cross the edges", True, BLUE)
    start_inst2 = small_font.render("* Continues food +1, special food +3", True, BLUE)
    start_inst3 = small_font.render("* Do not cross over yourself", True, BLUE)
    start_inst4 = small_font.render("* Keep playing......", True, BLUE)
    start_inst6 = small_font.render("* Press 1 for turn music ON", True, BLUE)
    start_inst7 = small_font.render("* Press 0 for turn music OFF", True, BLUE)
    start_inst5 = medium_font.render("BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect()
    start_inst5_rect.center = (WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100)

    canvas.blit(start_inst1, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2))
    canvas.blit(start_inst2, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2 + 30))
    canvas.blit(start_inst3, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2 + 60))
    canvas.blit(start_inst6, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2 + 90))
    canvas.blit(start_inst7, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2 + 120))
    canvas.blit(start_inst4, (WINDOW_WIDTH / 16, WINDOW_HEIGHT / 2 + 150))
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > start_inst5_rect.left and x < start_inst5_rect.right:
                    if y > start_inst5_rect.top and y < start_inst5_rect.bottom:
                        start_game()
        pygame.display.update()


def gameover(sc):  # Here we work on game over screen;;
    # canvas.fill(WHITE)
    global high_s
    mixer.Sound.set_volume(sound, 0)
    mixer.Sound.set_volume(sound1, 0)
    mixer.Sound.set_volume(sound2, 0)
    mixer.music.stop()
    canvas.blit(bg_img1, (0, 0))
    font_gameover1 = large_font.render('GAME OVER', True, BLACK)
    font_gameover2 = medium_font.render("PLAY AGAIN", True, RED, YELLOW)
    font_gameover3 = medium_font.render("QUIT", True, RED, YELLOW)
    with open("savegame", "rb") as f:
        foo = pickle.load(f)
        font_gameover4 = medium_font.render("CURRENT SCORE: " + str(foo), True, RED, YELLOW)
        font_gameover4_rect = font_gameover4.get_rect()
        font_gameover4_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 110)
        canvas.blit(font_gameover4, font_gameover4_rect)
    if high_s < sc:
        with open("highsavegame", "wb") as f:
            high_s = sc
    font_gameover5 = medium_font.render("HIGH SCORE: " + str(high_s), True, BLACK, WHITE)
    font_gameover5_rect = font_gameover5.get_rect()
    font_gameover5_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 190)
    canvas.blit(font_gameover5, font_gameover5_rect)

    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()

    font_gameover1_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2 - 100)
    font_gameover2_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 20)
    font_gameover3_rect.center = (WINDOW_WIDTH / 2 + 10, WINDOW_HEIGHT / 2 + 65)

    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                    if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                        gameloop()
                if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                    if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


def snake(snakelist, direction):  # This method is for snake movement between specific direction;;
    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    if direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    if direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    if direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for x, y in snakelist[1:-1]:
        pygame.draw.rect(canvas, BLUE, (x, y, SNAKE_WIDTH, SNAKE_WIDTH))


def game_paused():  # This is logic for game paused screen;;
    # canvas.fill(BLACK)

    paused_font1 = large_font.render("GAME PAUSED", True, RED)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    canvas.blit(paused_font1, paused_font_rect1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        mixer.music.unpause()
                        return
        pygame.display.update()


def gameloop():  # This is main loop, here we call all the method and logic after run the code;;
    global sound, FPS
    global sound1
    global sound2
    while True:

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Score:0", True, YELLOW)
        APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
        FOOD_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
        FOOD_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
        snakelist = []
        snakelength = 3
        sc = 0
        if sc == 0:
            FPS = 10
        pause_font = medium_font.render('II', True, RED)
        # sound_stop = medium_font.render('V', True, GREEN)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        mixer.music.play(-1, 0)
                        mixer.Sound.set_volume(sound, 1)
                        mixer.Sound.set_volume(sound1, 1)
                        mixer.Sound.set_volume(sound2, 1)
                    if event.key == pygame.K_0:
                        mixer.music.stop()
                        mixer.Sound.set_volume(sound, 0)
                        mixer.Sound.set_volume(sound1, 0)
                        mixer.Sound.set_volume(sound2, 0)
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            mixer.music.pause()
                            game_paused()
            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    mixer.Sound.play(sound)
                    if snakelength <= 3:
                        with open("savegame", "wb") as f:
                            pickle.dump(0, f)
                    pygame.time.delay(400)
                    gameover(sc)

            if direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > WINDOW_HEIGHT - SNAKE_WIDTH:
                    mixer.Sound.play(sound)
                    if snakelength <= 3:
                        with open("savegame", "wb") as f:
                            pickle.dump(0, f)
                    pygame.time.delay(400)
                    gameover(sc)
            if direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > WINDOW_WIDTH - SNAKE_WIDTH:
                    mixer.Sound.play(sound)
                    if snakelength <= 3:
                        with open("savegame", "wb") as f:
                            pickle.dump(0, f)
                    pygame.time.delay(400)
                    gameover(sc)
            if direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    mixer.Sound.play(sound)
                    if snakelength <= 3:
                        with open("savegame", "wb") as f:
                            pickle.dump(0, f)
                    pygame.time.delay(400)
                    gameover(sc)

            snakehead = [LEAD_X, LEAD_Y]
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            food_rect = pygame.Rect(FOOD_X, FOOD_Y, FOOD_SIZE, FOOD_SIZE)

            if len(snakelist) > snakelength:
                del snakelist[0]
            for point in snakelist[:-1]:
                if point == snakehead:
                    mixer.Sound.play(sound)
                    pygame.time.delay(400)
                    gameover(sc)

            # canvas.fill(BLACK)
            canvas.blit(bg_img2, (0, 0))

            snake(snakelist, direction)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                mixer.Sound.play(sound1)
                snakelength += 1
                sc += 1
                if 10 <= FPS <= 90:
                    FPS += 2
                print(FPS)
                score = small_font.render("Score:" + str(sc), True, YELLOW)
                with open("savegame", "wb") as f:
                    pickle.dump(sc, f)
            if snake_head_rect.colliderect(food_rect):
                FOOD_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                FOOD_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                mixer.Sound.play(sound2)
                sc += 3
                if FPS >= 30:
                    FPS -= 4
                print(FPS)
                score = small_font.render("Score:" + str(sc), True, YELLOW)
                with open("savegame", "wb") as f:
                    pickle.dump(sc, f)
            canvas.blit(score, (20, 10))
            pygame.draw.line(canvas, GREEN, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, YELLOW, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, YELLOW, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            if (sc % 8) == 0 and snakelength != 3:
                canvas.blit(food_img, (FOOD_X, FOOD_Y))
            pygame.display.update()
            clock.tick(FPS)


start_game()
gameloop()
