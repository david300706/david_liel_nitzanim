import pygame

SOLDIER_HEIGHT = 3
SOLDIER_WIDTH = 2
GRID_HEIGHT = 25
GRID_WIDTH = 50
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1500
FRAME_HEIGHT = SCREEN_HEIGHT / GRID_HEIGHT
FRAME_WIDTH = SCREEN_WIDTH / GRID_WIDTH
SOLDIER_X_LENGTH = SOLDIER_WIDTH * FRAME_WIDTH
SOLDIER_Y_LENGTH = SOLDIER_HEIGHT * FRAME_HEIGHT

FLAG_HEIGHT = 4
FLAG_WIDTH = 4



MINE_WIDTH = 3
MINE_HEIGHT = 1
START_MESSAGE = "Welcome To The Flag Game, Have Fun!"




BACKGROUND_COLOR = (25, 115, 22)

FLAG_IMAGE = pygame.image.load("flag.png").convert()
GRASS_IMAGE = pygame.image.load("grass.png").convert()
MINE_IMAGE = pygame.image.load("mine.png").convert()
SOLDIER_IMAGE = pygame.image.load("soldier.png").convert()
SOLDIER_NIGHT_IMAGE = pygame.image.load("soldier_night.png").convert()
EXPLOSION_IMAGE = pygame.image.load("explosion.png").convert()















