import pygame

enemy_list = []
img_enemy = pygame.image.load('image/blob.png')
rect_enemy = None
move_direction = 1
move_counter = 0


def create_enemy(x, y):
    global rect_enemy, img_enemy, enemy_list
    rect_enemy = img_enemy.get_rect(topleft=(x, y))
    enemy_list.append(rect_enemy)


def update_enemy():
    global enemy_list, move_direction, move_counter
    move_counter += 1
    if move_counter > 50 or move_counter < -50:
        move_direction *= -1
        move_counter *= -1

    for enemy in enemy_list:
        enemy.right += move_direction


def draw_enemy(screen):
    for enemy in enemy_list:
        screen.blit(img_enemy, enemy)
