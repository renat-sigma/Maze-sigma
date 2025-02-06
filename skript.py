from operator import index

import pygame
from pygame import MOUSEBUTTONDOWN

# Инициализация Pygame
pygame.init()

# Загрузка изображения
image_of_maze = pygame.image.load("game_skript/image_menu.png")
image_of_maze = pygame.transform.scale(image_of_maze, (1920, 1080))


#добавили лабиринт картинку на 2экране
image_of_maze2=pygame.image.load("game_skript/lvl1.png")
image_of_maze2=pygame.transform.scale(image_of_maze2,(1000,1000))#установили размер для картинки лабиринта


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

button_sound=pygame.Rect(1400,800,400,200)#создали обычный прямоугольник(1)

# Прозрачная поверхность для кнопки PLAY
transparent_surface = pygame.Surface((button_play.width, button_play.height), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 0, 0))  # Чёрный цвет с 50% прозрачности

transparent_surface2=pygame.Surface((button_sound.width,button_sound.height),pygame.SRCALPHA)#превратили прямокгольник в прозрачный(2)
transparent_surface2.fill((0,225,0,0))#указали цвет и прозрачность прямоугольнику(3)

# Работа с шрифтами
pygame.font.init()
button_font = pygame.font.SysFont("Arial", 100)  # Название шрифта
text_start = button_font.render("PLAY", True, White)
text_sound=button_font.render("SOUND",True,White)

player_original=pygame.image.load("game_skript/Taylor_standing.png").convert_alpha()#указал путь к картинке
player_original=pygame.transform.scale(player_original, (60,60))#указал размер картинке
player_width=60
player_height=60

maze_mask=pygame.mask.from_threshold(image_of_maze2,(0,0,0),(1,1,1,255))#treshold решает пропускать ли персонажа через объект или нет

x = 910#переменная отвечает за координату Xперсонажа
y = 950#переменная отвечает за координату Yперсонажа
gradus_rotate=0
state_screen=1
# Основной цикл
running = True
while running:
    for event in pygame.event.get():#цикл for проверяет и отвечает только за СОБЫТИЯ
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            old_x=x
            old_y=y
            if event.key==97:
                x=x-10
                gradus_rotate=90
            if event.key==100:
                x=x+10
                gradus_rotate=-90
            if event.key==119:
                y=y-10
                gradus_rotate=360
            if event.key==115:
                y=y+10
                gradus_rotate=180
        if event.type==pygame.KEYUP:
            print("123")
        elif event.type == MOUSEBUTTONDOWN:
            print("Клик мыши:")
            print(event.pos[0],"клик мыши по x")
            print(event.pos[1],"клик мыши по y")
            if event.pos[0]<1230 and event.pos[0]>630 and event.pos[1]<174 and event.pos[1] > 27:
                state_screen=2#сменили переменную на 2 благодаря которой меняется экран
                print(state_screen)
            if button_sound.collidepoint(event.pos):#запрограммировали нажатия по прямоугольнику с помощью collidepoint
                print("вы нажали на sound")

#конец цикла for

    # Отображение
    #цикл while отвечает за действие работа с картинками
    if state_screen==1:
        screen.blit(image_of_maze, (0, 0))  # Фон


            # Прямоугольник и текст для кнопки PLAY
        screen.blit(transparent_surface, button_play.topleft)
        screen.blit(transparent_surface2,button_sound.topleft)#вывели прямоугольник на экран(шаг 4)

        screen.blit(text_start, (button_play.x + 234, button_play.y + 20))

        screen.blit(text_sound,(button_sound.x+50,button_sound.y+20))



    if state_screen == 2 :
        screen.fill("white")
        screen.blit(image_of_maze2,(400,0))
        Taylor_standing1=pygame.transform.rotate(player_original,(gradus_rotate))
        screen.blit(Taylor_standing1,(x,y))#разместили картинку мальчика на втором экране
        player_mask = pygame.mask.from_surface(player_original)

        rotated_player=pygame.transform.rotate(player_original,gradus_rotate)
        player_mask=pygame.mask.from_surface(rotated_player)

    pygame.display.flip()  # Обновление экрана

pygame.quit()
#конец кода