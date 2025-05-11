from operator import index
from tabnanny import check

import pygame
import random

# Инициализация Pygame
pygame.init()

# Загрузка изображения
image_of_maze = pygame.image.load("game_skript/image_menu.png")
image_of_maze = pygame.transform.scale(image_of_maze, (1920, 1080))

# добавили лабиринт картинку на 2экране
image_of_maze2 = pygame.image.load("game_skript/lvl1.png")
image_of_maze2 = pygame.transform.scale(image_of_maze2, (1900, 1060))

image_of_maze3 = pygame.image.load("game_skript/lvl2.png")
image_of_maze3 = pygame.transform.scale(image_of_maze3, (1920, 1060))

# Настройка экрана
screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w * 0.96)
screen_height = int(screen_info.current_h * 0.96)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("hi")

# Цвета
Green = (255, 255, 255)
White = (255, 255, 255)
Transparent = (0, 0, 0, 0)

# Прямоугольник кнопки PLAY
button_play = pygame.Rect(600, 30, 600, 140)
button_sound = pygame.Rect(1400, 800, 400, 200)
ball_pickup_rekt = pygame.Rect(50, 50, 100, 300)

# Прозрачная поверхность для кнопки PLAY
transparent_surface = pygame.Surface((button_play.width, button_play.height), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 0))

transparent_surface2 = pygame.Surface((button_sound.width, button_sound.height), pygame.SRCALPHA)
transparent_surface2.fill((0, 225, 0, 0))

# Работа с шрифтами
pygame.font.init()
button_font = pygame.font.SysFont("Arial", 100)
text_start = button_font.render("PLAY", True, White)
text_sound = button_font.render("SOUND", True, White)

# Загрузка изображений
ball_pickup = pygame.image.load(("game_skript/ball.png"))
ball_pickup2 = pygame.image.load("game_skript/ball2.png")
ball_pickup3 = pygame.image.load("game_skript/ball3.png")


bomb=pygame.image.load("game_skript/bomb.png")

player_original = pygame.image.load("game_skript/Taylor_standing.png").convert_alpha()
player_original = pygame.transform.scale(player_original, (40, 40))

bomb=pygame.transform.scale(bomb,(150,109))

ball_pickup = pygame.transform.scale(ball_pickup, (50, 50))
ball_pickup2 = pygame.transform.scale(ball_pickup2, (50, 50))
ball_pickup3 = pygame.transform.scale(ball_pickup3, (50, 50))

# Параметры игрока и игры
player_width = 60
player_height = 60


maze_mask = pygame.mask.from_threshold(image_of_maze2, (0, 0, 0), (1, 1, 1, 255))
maze_mask1 = pygame.mask.from_threshold(image_of_maze3, (0, 0, 0), (1, 1, 1, 255))

x_bomb=300
y_bomb=250

x_bomb2=500
y_bomb2=930

x_bomb3=500
y_bomb3=400


x = 910
y = 950
old_x = x  # Инициализируем old_x и old_y здесь, чтобы они были доступны во всем цикле
old_y = y
gradus_rotate = 0
state_screen = 1

# Координаты мячей
a = [(100, 300), (200, 790), (400, 380), (250, 550), (250, 100)]
random_indices = random.sample(range(5), 3)
random_item = a[random_indices[0]]
random_item2 = a[random_indices[1]]
random_item3 = a[random_indices[2]]
ball_x = random_item[0]
ball_y = random_item[1]
ball_x2 = random_item2[0]
ball_y2 = random_item2[1]
ball_x3 = random_item3[0]
ball_y3 = random_item3[1]

ball1 = pygame.Rect(ball_x, ball_y, 50, 50)
ball2 = pygame.Rect(ball_x2, ball_y2, 50, 50)
ball3 = pygame.Rect(ball_x3, ball_y3, 50, 50)

# Основной цикл
running = True
clock = pygame.time.Clock()  # Добавляем часы для контроля FPS

ball_collect1=0
ball_collect2=0
ball_collect3=0

check=0

while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    check=check+1
    print(check)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            old_x = x  # Сохраняем текущие координаты до перемещения
            old_y = y
            if event.key == 97:  # 'a' key
                x = x - 39
                gradus_rotate = 180
            if event.key == 100:  # 'd' key
                x = x + 39
                gradus_rotate = 0
            if event.key == 119:  # 'w' key
                y = y - 39
                gradus_rotate = 90
            if event.key == 115:  # 's' key
                y = y + 39
                gradus_rotate = -90

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < 1230 and event.pos[0] > 630 and event.pos[1] < 174 and event.pos[1] > 27:
                state_screen = 2
            if button_sound.collidepoint(event.pos):
                print("вы нажали на sound")

    # 2. ОБНОВЛЕНИЕ СОСТОЯНИЯ ИГРЫ
    player = pygame.Rect(x, y, 40, 40)
    rotated_player = pygame.transform.rotate(player_original, gradus_rotate)
    player_mask = pygame.mask.from_surface(rotated_player)

    # Проверка столкновений со стенами
    if state_screen == 2 and maze_mask.overlap(player_mask, (x, y)):
        x = old_x
        y = old_y

    if state_screen == 3 and maze_mask1.overlap(player_mask, (x, y)):
        x = old_x
        y = old_y

    # Проверка столкновений с мячами

    if state_screen == 2:
        if ball1.colliderect(player):
            print("Собран мяч 1!")
            ball_collect1=1
        if ball2.colliderect(player):
            print("Собран мяч 2!")
            ball_collect2=1
        if ball3.colliderect(player):
            print("Собран мяч 3!")
            ball_collect3=1
        # Проверка перехода на следующий уровень


        if x > 806 and x < 936 and y > 3 and y < 30 and ball_collect1 == 1 and ball_collect2 == 1 and ball_collect3 == 1 :
            state_screen = 3
            x = 570
            y = 1000
    # 3. ОТРИСОВКА
    if state_screen == 1:  # Экран меню
        screen.blit(image_of_maze, (0, 0))
        screen.blit(transparent_surface, button_play.topleft)
        screen.blit(transparent_surface2, button_sound.topleft)
        screen.blit(text_start, (button_play.x + 234, button_play.y + 20))
        screen.blit(text_sound, (button_sound.x + 50, button_sound.y + 20))

    elif state_screen == 2:  # Первый уровень
        screen.fill("white")
        screen.blit(image_of_maze2, (0, 0))
        screen.blit(rotated_player, (x, y))
        screen.blit(bomb,(x_bomb,y_bomb))
        screen.blit(bomb,(x_bomb2,y_bomb2))
        screen.blit(bomb,(x_bomb3,y_bomb3))
        if ball_collect1==0 :
            screen.blit(ball_pickup, (ball_x, ball_y))
        if ball_collect2==0:
            screen.blit(ball_pickup2, (ball_x2, ball_y2))
        if ball_collect3==0:
            screen.blit(ball_pickup3, (ball_x3, ball_y3))

    elif state_screen == 3:  # Второй уровень
        screen.fill("white")
        screen.blit(image_of_maze3, (0, 0))
        screen.blit(rotated_player, (x, y))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # Ограничение FPS до 60

pygame.quit()