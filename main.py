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
         "show_mines": False,
         "is_winning": False,
         "is_losing": False,
         }


def main():
    pygame.init()

    state["game_field"], state["mines"] = game_field.create()

    user_events()
    screen.draw_start_massage()
    pygame.display.update()
    time.sleep(1)

    while state["game_running"]:
        user_events()
        if state["is_losing"]:
            screen.print_lost()
            state["game_running"] = False

        if state["show_mines"]:
            screen.show_mines(state)
            state["show_mines"] = False
            time.sleep(1)
        else:
            screen.draw_game(state)




        state["is_losing"] = soldier.is_eliminated(state)


        soldier.soldier_feet_cords(state["soldier_location"])


def user_events():
    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state["show_mines"] = True

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                state["soldier_location"][1] -= 1

            if event.key == pygame.K_DOWN and state["soldier_location"][1] < consts.GRID_HEIGHT - 1:
                state["soldier_location"][1] += 1

            if event.key == pygame.K_RIGHT and state["soldier_location"][0] < consts.GRID_WIDTH - 1:
                state["soldier_location"][0] += 1

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                state["soldier_location"][0] -= 1


main()
