import pygame
from player import rect_player

coin_list = []
coin_img = pygame.transform.scale(pygame.image.load('image/coin.png'), (40, 40))
coin_rect = None


def create_coin(x, y):
    global coin_rect, coin_img, coin_list
    coin_rect = coin_img.get_rect(topleft=(x, y))
    coin_list.append(coin_rect)


def draw_coin(screen):
    for coin in coin_list:
        screen.blit(coin_img, coin)


