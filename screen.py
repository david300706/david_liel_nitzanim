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

# def show_mines(game_state):





