from operator import index

import pygame#импортировали библиотеку pygame

# Инициализация Pygame
pygame.init()

# Загрузка изображения
image_of_maze = pygame.image.load("game_skript/image_menu.png")
image_of_maze = pygame.transform.scale(image_of_maze, (1920, 1080))


#добавили лабиринт картинку на 2экране
image_of_maze2=pygame.image.load("game_skript/lvl1.png")#указал путь к картинке
image_of_maze2=pygame.transform.scale(image_of_maze2,(1900,1060))#установили размер для картинки лабиринта

image_of_maze3=pygame.image.load("game_skript/lvl2.png")
image_of_maze3=pygame.transform.scale(image_of_maze3,(1920,1060))


# Настройка экрана
screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w * 0.96)
screen_height = int(screen_info.current_h * 0.96)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("hi")

# Цвета
Green = (255, 255, 255)#сохранили цвета RGB
White = (255, 255, 255)#сохранили цвета RGB
Transparent = (0, 0, 0, 0)

# Прямоугольник кнопки PLAY
button_play = pygame.Rect(600, 30, 600, 140)#указали размеры кнопки play

button_sound=pygame.Rect(1400,800,400,200)#создали обычный прямоугольник(1)

ball_pickup_rekt = pygame.Rect(50, 50, 100, 300)

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

ball_pickup=pygame.image.load(("game_skript/ball.png"))


player_original=pygame.image.load("game_skript/Taylor_standing.png").convert_alpha()#указал путь к картинке
player_original=pygame.transform.scale(player_original, (40,40))#указал размер картинке

ball_pickup=pygame.transform.scale(ball_pickup,(50,50))

player_width=60
player_height=60
#шаг1 создли маску для стен лабиринта
maze_mask=pygame.mask.from_threshold(image_of_maze2,(0,0,0),(1,1,1,255))#treshold решает пропускать ли персонажа через объект или нет
maze_mask1=pygame.mask.from_threshold(image_of_maze3,(0,0,0),(1,1,1,255))
x = 910#переменная отвечает за координату Xперсонажа
y = 950#переменная отвечает за координату Yперсонажа
gradus_rotate=0#с помощью этой переменной делаем вращение персонажу
state_screen=1#создали переменную для смены экранов
# Основной цикл

running = True
while running:#создали главный цикл
    for event in pygame.event.get():#цикл for проверяет и отвечает только за СОБЫТИЯ
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:#проверяем через ключ нажатой буквы
            old_x=x#создали старую версию координат x чтобы при столкновения персонажа и стенки возвращать персонажа в старые координаты
            old_y=y#создали старую версию координат y чтобы при столкновения персонажа и стенки возвращать персонажа в старые координаты
            if event.key==97:
                x=x-39
                gradus_rotate=180#a


            if event.key==100:
                x=x+39
                gradus_rotate=0#d


            if event.key==119:
                y=y-39
                gradus_rotate=90#w


            if event.key==115:
                y=y+39#s
                gradus_rotate=-90

            rotated_player = pygame.transform.rotate(player_original, gradus_rotate)
            player_mask = pygame.mask.from_surface(rotated_player)  # создаем маску персонажа ВНУТРИ ЦИКЛА(чтобы она обновлялась постоянно)
            #с помощью old_x и old_y после столкновения возвращаяем персонажа в предыдущее положение
            if maze_mask.overlap(player_mask,(x,y)) and state_screen==2:
                x=old_x
                y=old_y
            if maze_mask1.overlap(player_mask,(x,y)) and state_screen==3:
                x=old_x
                y=old_y

        if event.type==pygame.KEYUP:#если клавиша вернулась после нажатия
            print("123")
        elif event.type == pygame.MOUSEBUTTONDOWN:#если клавиша нажата
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
    if state_screen==1:#проверяем стоит ли первый экран
        screen.blit(image_of_maze, (0, 0))  # Фон


            # Прямоугольник и текст для кнопки PLAY
        screen.blit(transparent_surface, button_play.topleft)
        screen.blit(transparent_surface2,button_sound.topleft)#вывели прямоугольник на экран(шаг 4)

        screen.blit(text_start, (button_play.x + 234, button_play.y + 20))#вывели на экран кнопку Play

        screen.blit(text_sound,(button_sound.x+50,button_sound.y+20))#вывели на экран кнопку Sound


    if state_screen == 2 :#проверка на работу 2экрана
        screen.fill("white")#залили фон белым
        screen.blit(image_of_maze2,(0,0))#вывели на экран картинку лабиринта
        Taylor_standing1=pygame.transform.rotate(player_original,(gradus_rotate))#дали персонажу возможность поворота
        screen.blit(Taylor_standing1,(x,y))#разместили картинку мальчика на втором экране
        screen.blit(ball_pickup,(100,300))
        print(x,y,"ddgf")
        #шаг2 создали маску для персонажа
        player_mask = pygame.mask.from_surface(player_original)#сделали маску персонаж
        if x>806 and x<936 and y>3 and y<30:
            state_screen=3
            x=570
            y=1000
    if state_screen==3:
        screen.fill("white")#залили фон белым
        screen.blit(image_of_maze3,(0,0))#вывели на экран картинку лабиринта
        screen.blit(Taylor_standing1,(x,y))#разместили картинку мальчика на втором экране
        player_mask = pygame.mask.from_surface(player_original)
        Taylor_standing1=pygame.transform.rotate(player_original,(gradus_rotate))


    pygame.display.flip()  # Обновление экрана

pygame.quit()
#конец кода


