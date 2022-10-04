import pygame, sys
from pygame import mixer

# init pygame and pygame audio mixer
pygame.init()
mixer.init()

from utilities.settings import *

# set window size
SCREEN = pygame.display.set_mode(size=WINDOW_SIZE)

# import game assets
from game_assets.background import draw_background
from game_assets.ground import draw_ground
from game_assets.obstacles import *
from game_assets.trex import draw_trex, jump, crounch, get_trex_rect
from game_assets.gameover_screen import draw_game_over_screen

# set window title
pygame.display.set_caption(GAME_TITLE)

# set screen fps
CLOCK = pygame.time.Clock()

GAME_OVER = False


def main():
    def game_loop():
        while True:
            # get input events
            check_events()

            # clear previous screen
            SCREEN.fill("#3282C1")

            if not GAME_OVER:
                # draw background image
                draw_background(SCREEN)

                # draw ground
                draw_ground(SCREEN)

                # draw obstacles
                draw_cactus(SCREEN)
                draw_bird(SCREEN)

                # draw T-Rex
                draw_trex(SCREEN)

                # run collision tests
                check_collisions()
            else:
                draw_game_over_screen(SCREEN)

            pygame.display.update()
            CLOCK.tick(FPS)


    def check_events():
        global GAME_OVER

        for event in pygame.event.get():
            #exit game with window X button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # exit game with ESC button
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            # SPACE event for jump
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if GAME_OVER:
                    GAME_OVER = False
                else:
                    jump()

            # LCTRL event for crounch
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
                crounch(SCREEN)
            #if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
             #   crounch(SCREEN)


    def check_collisions():
        global GAME_OVER

        trex_rect = get_trex_rect()
        cactus_rect = get_cactus_rect()
        bird_rect = get_bird_rect()

        # pygame.draw.rect(SCREEN, "red", trex_rect, 4)

        if trex_rect.colliderect(cactus_rect) or trex_rect.colliderect(bird_rect):
            GAME_OVER = True
            reset_cactus()
            reset_bird()

    game_loop()

main()
