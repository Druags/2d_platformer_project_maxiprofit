import pygame  # импортируем pygame для создания игры
import world  # импортируем world для отрисовки мира игры
import player

pygame.init()  # инициализируем pygame

screen_width = 800  # ширина экрана
screen_height = 800  # высота экрана

FPS = 60  # ФПС

screen = pygame.display.set_mode((screen_width, screen_height))  # создание экрана
background = pygame.image.load('image/sky.png')  # создание заднего фона
background = pygame.transform.scale(background,
                                    (screen_width,
                                     screen_height))  # изменение размеров в соответствии с размерами экрана
sun = pygame.image.load('image/sun.png')  # загружаем солнце
clock = pygame.time.Clock()  # создаём часы, которые пригодятся для отслеживания времени работы программы

map_world = world.create_world()  # создаём список объектов для отрисовки
character = player.create_player()
run = True  # переменная run отвечает за работу игрового цикла
while run:  # игровой цикл
    # через pygame.event.get() получаем все события(нажатия на клавиатуру, мышку и т.п.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если мы нажали на выход из программы,
            # то run становится False и цикл while заканчивается, так как условие не выполняется, т.е. False
            run = False
    screen.blit(background, (0, 0))  # отрисовка заднего фона
    screen.blit(sun, (100, 100))  # отрисовка солнца
    world.draw_world(screen, map_world)  # отрисовка элементов мира
    world.draw_grid(screen, screen_width, screen_height)  # отрисовка сетки
    player.update_player(screen)
    pygame.display.update()  # обновление экрана, чтобы увидеть новые рисунки
    clock.tick(FPS)  # ограничение ФПС
pygame.quit()  # закрытие игры после того, как игровой цикл
# закончится, после этой строки нет смысла взаимодействовать с pygame
