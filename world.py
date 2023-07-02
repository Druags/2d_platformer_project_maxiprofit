import pygame

world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
    [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
    [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]  # этот список отображает какие именно блоки мы рисуем, 0 - пустота, 1 - земля, 2 - трава
tile_size = 40  # размер тайла

grass = pygame.image.load('image/grass.png')  # загружаем изображение травы
dirt = pygame.image.load('image/dirt.png')  # загружаем изображение земли
grass = pygame.transform.scale(grass,
                               (tile_size, tile_size))  # делаем размер загруженной картинки в соответствии с тайлом
dirt = pygame.transform.scale(dirt,
                              (tile_size, tile_size))  # делаем размер загруженной картинки в соответствии с тайлом


def create_world():  # функция отвечает за создание мира
    world_map = []  # пустой список, в который будут помещать пары элементов (картинка, координаты картинки)
    for r in range(len(world_data)):  # перебираем строки списка world_data, где хранятся обозначения тайлов
        for c in range(len(world_data[r])):  # перебираем колонки в каждой строке списка, получая отдельные элементы
            if world_data[r][c] == 1:  # если значение равняется одному, то загружаем грязь и её координаты
                # которые получаем через c (обозначает колонку или x) и r (обозначает строку или y)
                world_map.append((dirt, (c * tile_size, r * tile_size)))
                # с помощью метода append добавляем пару значений в конец списка
            elif world_data[r][c] == 2:  # проверяем, что элемент равен двойке
                world_map.append((grass, (c * tile_size, r * tile_size)))  # добавляем траву и её координаты
    return world_map  # возвращаем список world_map, чтобы можно было получить его в файле game.py


# функция для отрисовки сетки, чтобы было проще ориентироваться,
# принимает параметры: экран, на котором рисует, ширину и высоту экрана
def draw_grid(screen, width, height):
    for i in range(len(world_data)):  # перебираем количество строчек в списке, чтобы нарисовать горизонтальные линии
        pygame.draw.line(screen, 'white', (0, i * tile_size), (width, i * tile_size))  # рисуем линию

    for i in range(len(world_data[0])):  # перебираем количество колоноко в списке, чтобы нарисовать вертикальные линии
        pygame.draw.line(screen, 'white', (i * tile_size, 0), (i * tile_size, height))  # рисуем линию


# функция для отрисовки мира, принимает экран для рисование и список элементов для отрисовки, который мы получаем
# из функции create_world
def draw_world(screen, world_map):
    for element in world_map:
        screen.blit(element[0], element[1])