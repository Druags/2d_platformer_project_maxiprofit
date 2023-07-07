import pygame

pygame.init()

img_player = None
rect_player = None
gravity = 0
jumped = False


def create_player():
    global img_player, rect_player
    img_player = pygame.image.load('image/guy1.png')
    rect_player = img_player.get_rect(topleft=(700, 100))


def update_player(screen):
    global img_player, rect_player, images_right, index
    dx = 0
    dy = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -5
    elif keys[pygame.K_RIGHT]:
        dx = 5
    player_jumped(keys)
    dy = player_gravity(dy)
    rect_player.x += dx
    rect_player.y += dy
    screen.blit(img_player, rect_player)


def player_jumped(keys):
    global gravity, jumped, air
    if keys[pygame.K_SPACE] and jumped == False:
        gravity = -15
        jumped = True
    if keys[pygame.K_SPACE] == False:
        jumped = False


def player_gravity(dy):
    global gravity
    gravity += 1
    if gravity > 10:
        gravity = 10
    dy += gravity
    return dy
