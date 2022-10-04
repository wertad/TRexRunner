import pygame
from utilities.resources import get_resource_path
from utilities.settings import *

BIG_FONT = pygame.font.Font(get_resource_path("dogicabold.ttf"), 40)
SMALL_FONT = pygame.font.Font(get_resource_path("dogica.ttf"), 20)

GAME_OVER_TEXT = BIG_FONT.render("game over", False, "white")
GAME_OVER_TEXT_REACT = GAME_OVER_TEXT.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))

PRESS_SPACE_TEXT = SMALL_FONT.render("Press Space to coninue...", False, "white")
PRESS_SPACE_TEXT_RECT = PRESS_SPACE_TEXT.get_rect(midtop=(GAME_OVER_TEXT_REACT.midbottom[0], GAME_OVER_TEXT_REACT.midbottom[1] + 20))


def draw_game_over_screen(screen):
    screen.blit(GAME_OVER_TEXT, GAME_OVER_TEXT_REACT)
    screen.blit(PRESS_SPACE_TEXT, PRESS_SPACE_TEXT_RECT)
