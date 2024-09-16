import time

import pygame
import consts

screen = pygame.display.set_mode(
    (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)



def draw_start_massage():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_message(consts.START_MESSAGE, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_LOCATION)



def draw_soldier(location):
    soldier = consts.SOLDIER_IMAGE.get_rect(topleft=(location[0] * consts.FRAME_WIDTH, location[1] * consts.FRAME_HEIGHT))
    screen.blit(consts.SOLDIER_IMAGE, soldier)

def draw_night_soldier(location):
    soldier = consts.SOLDIER_NIGHT_IMAGE.get_rect(topleft=(location[0] * consts.FRAME_WIDTH, location[1] * consts.FRAME_HEIGHT))
    screen.blit(consts.SOLDIER_NIGHT_IMAGE, soldier)


def draw_bushes(bushes):
    for bush in bushes:
        bush_img = consts.GRASS_IMAGE.get_rect(topleft=bush)
        screen.blit(consts.GRASS_IMAGE, bush_img)


def draw_flag():
    flag = consts.FLAG_IMAGE.get_rect(topleft=(consts.SCREEN_WIDTH - consts.FLAG_WIDTH * consts.FRAME_WIDTH - 100,
                                               consts.SCREEN_HEIGHT - consts.FLAG_HEIGHT * consts.FLAG_WIDTH - 300))
    screen.blit(consts.FLAG_IMAGE, flag)



def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)

    draw_bushes(game_state["bushes"])
    draw_soldier(game_state["soldier_location"])
    draw_flag()

def draw_grid():
    for x in range(0, consts.SCREEN_WIDTH, consts.FRAME_WIDTH):
        for y in range(0, consts.SCREEN_HEIGHT, consts.FRAME_HEIGHT):
            rect = pygame.Rect(x, y, consts.FRAME_WIDTH, consts.FRAME_HEIGHT)
            pygame.draw.rect(screen, consts.START_COLOR, rect, 1)

def draw_mines(mines):
    for mine in mines:
        mine_img = consts.MINE_IMAGE.get_rect(topleft=(mine[0] * consts.FRAME_WIDTH, mine[1] * consts.FRAME_HEIGHT))
        screen.blit(consts.MINE_IMAGE, mine_img)

def show_mines(game_state):
    screen.fill(consts.NIGHT_COLOR)
    draw_grid()
    draw_mines(game_state["mines"])
    draw_night_soldier(game_state["soldier_location"])



def print_lost_and_exit():
    draw_message(consts.LOST_MASSAGE, consts.START_FONT_SIZE,
                 consts.START_COLOR, consts.START_LOCATION)
    time.sleep(1)
    pygame.quit()

