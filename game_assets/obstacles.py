import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

CACTUS_IMAGE = pygame.image.load(get_resource_path("cactus_01.png")).convert_alpha()
CACTUS_RECT = CACTUS_IMAGE.get_rect(x=WINDOW_SIZE[0], y=250)

BIRD_FRAMES = [
    pygame.image.load(get_resource_path("bird_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("bird_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
BIRD_IMAGE = BIRD_FRAMES[FRAME]
BIRD_X_POS = 1800
BIRD_RECT = BIRD_IMAGE.get_rect(x=1800, y=120)


def draw_cactus(screen):
    if CACTUS_RECT.right < 0:
        CACTUS_RECT.left = WINDOW_SIZE[0]

    CACTUS_RECT.x -= GROUND_SPEED
    screen.blit(CACTUS_IMAGE, CACTUS_RECT)

    #pygame.draw.rect(screen, "red", CACTUS_RECT, 4)


def get_cactus_rect():
    return CACTUS_RECT


def reset_cactus():
    CACTUS_RECT.left = WINDOW_SIZE[0]


def draw_bird(screen):
    global FRAME, BIRD_X_POS, BIRD_IMAGE

    if BIRD_RECT.right < 0:
        BIRD_RECT.left = 1800

    screen.blit(BIRD_IMAGE, (BIRD_X_POS, 120))

    BIRD_RECT.x -= GROUND_SPEED
    BIRD_IMAGE = BIRD_FRAMES[int(FRAME)]
    BIRD_X_POS -= GROUND_SPEED

    #pygame.draw.rect(screen, "red", BIRD_RECT, 4)

    FRAME += ANIM_SPEED
    if FRAME >= len(BIRD_FRAMES):
        FRAME = 0





def get_bird_rect():
    return BIRD_RECT


def reset_bird():
    global BIRD_X_POS, BIRD_RECT
    BIRD_RECT = BIRD_IMAGE.get_rect(x=1800, y=120)
    BIRD_X_POS = 1800
