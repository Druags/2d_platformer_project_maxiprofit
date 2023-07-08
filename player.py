import pygame

pygame.init()

img_player = None  # переменная, в которой будет храниться картинка игрока
rect_player = None  # переменная, в которой будет храниться управляемый объект(игрок)
gravity = 0  # сила гравитации
jumped = False  # состояние игрока(прыжок = True, падение = False)


def create_player():  # функция, создающая игрока
    global img_player, rect_player  # получаем доступ к переменным, объявленным вне функции
    img_player = pygame.image.load('image/guy1.png')  # загружаем картинку
    rect_player = img_player.get_rect(topleft=(100, 100))  # из картинки создаём прямоугольник(управляемый объект)


def update_player(screen):  # фукнция для обновления состояния игрока
    global img_player, rect_player, images_right, index  # получаем доступ к переменным, объявленным вне функции
    dx = 0  # переменная для перемещения по оси х(влево, вправо)
    dy = 0  # переменная для перемещения по оси y(вверх, вниз)
    keys = pygame.key.get_pressed()  # получаем все нажатые клавиши
    if keys[pygame.K_LEFT]:  # если нажата стрелка влево
        dx = -5  # то идём влево
    elif keys[pygame.K_RIGHT]:  # если нажата стрелка вправо
        dx = 5  # то идём вправо
    player_jumped(keys)  # вызываем функцию, обрабатывающую прыжок
    dy = player_gravity(dy)  # вызываем функцию, обрабатывающую гравитацию, сохраняем её значение в переменной
    rect_player.x += dx  # передвигаем персонажа по оси х на значение из dx
    rect_player.y += dy  # передвигаем персонажа по оси y на значение из dy
    screen.blit(img_player, rect_player)  # отрисовываем персонажа


def player_jumped(keys):  # фукнция для обработки прыжка
    global gravity, jumped  # получаем доступ к переменным, объявленным вне функции
    if keys[
        pygame.K_SPACE] and jumped == False:  # проверяем, что нажата клавиша пробел и игрок в данный момент не прыгает
        gravity = -15  # уменьшаем притяжение, чтобы игрок подлетел вверх
        jumped = True  # вводим игрока в состояние прыжка
    if keys[pygame.K_SPACE] == False:  # если клавиша не нажата
        jumped = False  # то отменяем прыжок


def player_gravity(dy):  # функция для обработки гравитации
    global gravity  # получаем доступ к к переменной, объявленной вне функции
    gravity += 1  # постоянно увеличиваем гравитацию
    if gravity > 10:  # если гравитация достигла значения 10
        gravity = 10  # то оставляем её на 10
    dy += gravity  # изменяем переменную для перемещения по оси у
    return dy  # возврвщаем ранее изменённую пременную
