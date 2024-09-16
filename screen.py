import pygame

import consts


screen = pygame.display.set_mode(
        (1000, consts.SCREEN_HEIGHT))








def draw_soldier(location):
    soldier = consts.SOLDIER_IMAGE.get_rect(topleft=location)
    screen.blit(consts.SOLDIER_IMAGE, soldier)

def draw_bushes(bushes):
    for bush in bushes:
        bush_img = consts.GRASS_IMAGE.get_rect(topleft=bush)
        screen.blit(consts.GRASS_IMAGE, bush_img)

def draw_flag():
    flag = consts.SOLDIER_IMAGE.get_rect(topleft=consts.FLAG_WIDTH * consts.)
    screen.blit(consts.SOLDIER_IMAGE, soldier)





def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_bushes() # TODO
    draw_soldier(): # TODO




