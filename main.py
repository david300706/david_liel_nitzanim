import consts
import soldier
import game_field
import pygame
import screen
import time

state = {"bushes":game_field.bush_spread(),
         "showed_welcome_massage": False,
         "game_running": True,
         "soldier_location": (0, 0),
         }


def main():
    pygame.init()
    user_events()
    screen.draw_start_massage()
    pygame.display.update()
    time.sleep(3)
    while state["game_running"]:

        user_events()

        screen.draw_game(state)

        pygame.display.flip()

def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                print("Key UP has been pressed")

            if event.key == pygame.K_DOWN:
                print("Key DOWN has been pressed")

            if event.key == pygame.K_RIGHT:
                print("Key RIGHT has been pressed")

            if event.key == pygame.K_LEFT:
                print("Key LEFT has been pressed")
user_events()

main()
