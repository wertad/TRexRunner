import pygame
from utilities.resources import get_resource_path

JUMP_SOUND = pygame.mixer.Sound(get_resource_path("jump.wav"))
JUMP_SOUND.set_volume(0.1)

TREX_FRAMES = [
    pygame.image.load(get_resource_path("trex_run_01.png")).convert_alpha(),
    pygame.image.load(get_resource_path("trex_run_02.png")).convert_alpha()
]
FRAME = 0
ANIM_SPEED = 0.1
GRAVITY = 0
ON_GROUND = True
TREX_IMAGE = TREX_FRAMES[FRAME]
TREX_RECT = TREX_IMAGE.get_rect(x=0, y=250)


def draw_trex(screen):
    global FRAME, GRAVITY, ON_GROUND

    FRAME += ANIM_SPEED
    if FRAME >= len(TREX_FRAMES):
        FRAME = 0

    # apply gravity
    GRAVITY += 1
    TREX_RECT.y += GRAVITY
    if TREX_RECT.y >= 250:
        GRAVITY = 0
        TREX_RECT.y = 250
        ON_GROUND = True

    TREX_IMAGE = TREX_FRAMES[int(FRAME)]
    screen.blit(TREX_IMAGE, TREX_RECT)

    #pygame.draw.rect(screen, "red", TREX_RECT, 4)


def get_trex_rect():
    return TREX_RECT.inflate(-150, -30)


def jump():
    global GRAVITY, ON_GROUND

    if not ON_GROUND:
        return

    GRAVITY -= 23
    JUMP_SOUND.play()
    ON_GROUND = False