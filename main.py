import consts
import soldier
import screen
import game_field
import pygame
import screen
import time

state = {"bushes": game_field.bush_spread(),
         "showed_welcome_massage": False,
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [],
         "game_field": game_field.create()
         }


def main():
    pygame.init()
    # game_field.create()

    user_events()
    screen.draw_start_massage()
    pygame.display.update()
    time.sleep(1)
    while state["game_running"]:
        user_events()

        screen.draw_game(state)

        pygame.display.update()


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                print("Key UP has been pressed")
                state["soldier_location"][1] -= 1

            if event.key == pygame.K_DOWN and state["soldier_location"][1] < consts.GRID_HEIGHT - 1:
                print("Key DOWN has been pressed")
                state["soldier_location"][1] += 1

            if event.key == pygame.K_RIGHT and state["soldier_location"][0] < consts.GRID_WIDTH - 1:
                print("Key RIGHT has been pressed")
                state["soldier_location"][0] += 1

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                print("Key LEFT has been pressed")
                state["soldier_location"][0] -= 1


user_events()

# soldier.soldier_feet_cords(state["soldier_location"])
main()
