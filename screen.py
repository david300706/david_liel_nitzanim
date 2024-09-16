import pygame
import time
import consts

screen = pygame.display.set_mode(
    (1000, consts.SCREEN_HEIGHT))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


def draw_start_massage():
    draw_message(consts.START_MESSAGE, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_LOCATION)


def draw_soldier(location):
    soldier = consts.SOLDIER_IMAGE.get_rect(topleft=location)
    screen.blit(consts.SOLDIER_IMAGE, soldier)


def draw_bushes(bushes):
    for bush in bushes:
        bush_img = consts.GRASS_IMAGE.get_rect(topleft=bush)
        screen.blit(consts.GRASS_IMAGE, bush_img)


def draw_flag():
    flag = consts.SOLDIER_IMAGE.get_rect(topleft=(consts.FLAG_WIDTH * consts.FRAME_WIDTH,
                                                  consts.FLAG_HEIGHT * consts.FLAG_WIDTH))
    screen.blit(consts.SOLDIER_IMAGE, flag)


def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    draw_start_massage()
    time.sleep(3)
    draw_bushes(game_state["bushes"])
    draw_soldier(game_state["soldier_location"])
    draw_flag()
