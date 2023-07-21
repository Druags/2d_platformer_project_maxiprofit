import pygame  # импортируем pygame для создания игры
import world  # импортируем world для отрисовки мира игры
import player  # импортируем player для работы с персонажем
import enemy
import coin
import lava


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

game_over = False
score = 0

map_world = world.create_world()  # создаём список объектов для отрисовки
player.create_player()  # создаём игрока, которым можно управлять

font = pygame.font.SysFont('arial', 36)
final_text = font.render('Потрачено', False, 'red')

pygame.mixer.music.load('sound/joshua-mclean-mountain-trials.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()

run = True  # переменная run отвечает за работу игрового цикла


def check_coin():
    global score
    for coin_object in coin.coin_list:
        if player.rect_player.colliderect(coin_object):
            coin.coin_list.remove(coin_object)
            score += 1


def check_player():
    global game_over
    for enemy_element in enemy.enemy_list:
        if enemy_element.colliderect(player.rect_player):
            game_over = True

    for lava_element in lava.lava_list:
        if lava_element.colliderect(player.rect_player):
            game_over = True


while run:  # игровой цикл
    # через pygame.event.get() получаем все события(нажатия на клавиатуру, мышку и т.п.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если мы нажали на выход из программы,
            # то run становится False и цикл while заканчивается, так как условие не выполняется, т.е. False
            run = False
    screen.blit(background, (0, 0))  # отрисовка заднего фона
    screen.blit(sun, (100, 100))  # отрисовка солнца
    world.draw_world(screen, map_world)  # отрисовка элементов мира
    enemy.draw_enemy(screen)
    enemy.update_enemy()

    score_text = font.render(f'Счёт: {score}', True, 'gold')
    check_coin()
    check_player()
    screen.blit(score_text, (20, 10))
    coin.draw_coin(screen)
    lava.draw_lava(screen)
    world.draw_grid(screen, screen_width, screen_height)  # отрисовка сетки
    player.update_player(screen, map_world)  # обновляем состояние персонажа
    if game_over:
        screen.fill('black')
        screen.blit(final_text, (screen_width/2, screen_height/2))
        pygame.display.update()
        pygame.time.wait(2000)
        player.rect_player.topleft = (80,720)
        game_over = False
    pygame.display.update()  # обновление экрана, чтобы увидеть новые рисунки
    clock.tick(FPS)  # ограничение ФПС
pygame.quit()  # закрытие игры после того, как игровой цикл
# закончится, после этой строки нет смысла взаимодействовать с pygame
