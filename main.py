import consts
import soldier
import screen
import game_field
import pygame
import screen
import time

state = {"bushes": game_field.bush_spread(),
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [],
         "game_field": game_field.create(),
         "show_mines": False
         }


def main():
    pygame.init()
    user_events()
    screen.draw_start_massage()
    pygame.display.update()
    time.sleep(1)
    while state["game_running"]:
        user_events()
        if state["show_mines"]:
            screen.show_mines(state)
            state["show_mines"] = False
            time.sleep(1)
        else:
            screen.draw_game(state)

        pygame.display.flip()
        soldier.is_eliminated(state)
        if soldier.is_eliminated(state):
            state["game_running"] = False

        soldier.soldier_feet_cords(state["soldier_location"])


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("enter")
                state["show_mines"] = True

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                # print("Key UP has been pressed")
                state["soldier_location"][1] -= 1

            if event.key == pygame.K_DOWN and state["soldier_location"][1] < consts.GRID_HEIGHT - 1:
                # print("Key DOWN has been pressed")
                state["soldier_location"][1] += 1

            if event.key == pygame.K_RIGHT and state["soldier_location"][0] < consts.GRID_WIDTH - 1:
                # print("Key RIGHT has been pressed")
                state["soldier_location"][0] += 1

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                # print("Key LEFT has been pressed")
                state["soldier_location"][0] -= 1


main()
