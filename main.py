import consts
import soldier
import screen
import game_field
import pygame

state = {"bushes": game_field.find_bushes()}


def main():
    pass


def user_events():
    import sys

    pygame.init()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    print("Key UP has been pressed")

                if event.key == pygame.K_DOWN:
                    print("Key DOWN has been pressed")

                if event.key == pygame.K_RIGHT:
                    print("Key RIGHT has been pressed")

                if event.key == pygame.K_LEFT:
                    print("Key LEFT has been pressed")
