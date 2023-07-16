import pygame

lava_list = []
lava_img = pygame.transform.scale(pygame.image.load('image/lava.png'), (40, 40))
lava_rect = None


def create_lava(x, y):
    global lava_rect, lava_img, lava_list
    lava_rect = lava_img.get_rect(topleft=(x, y))
    lava_list.append(lava_rect)


def draw_lava(screen):
    for lava in lava_list:
        screen.blit(lava_img, lava)