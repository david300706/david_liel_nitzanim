import consts
import database
import guard
import soldier
import screen
import game_field
import pygame
import screen
import time
import pandas as pd

state = {"bushes": game_field.bush_spread(),
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [[], []],
         "guard_location": [0, 11],
         "guard_forward": False,
         "game_field": game_field.create(),
         "show_mines": False,
         "is_winning": False,
         "is_losing": False,
         "is_eaten": False
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
        if state["is_losing"] or state["is_eaten"]:
            screen.print_lost()
            state["game_running"] = False
        elif state["is_winning"]:
            screen.print_won()
            state["game_running"] = False

        if state["show_mines"]:
            screen.show_mines(state)
            state["show_mines"] = False
            time.sleep(1)
        else:
            screen.draw_game(state)

        state["is_losing"] = soldier.is_eliminated(state)
        state["is_winning"] = soldier.is_winning(state)
        state["is_eaten"] = guard.guard_eat(state)

        soldier.soldier_feet_cords(state["soldier_location"])
        state["guard_location"], state["guard_forward"] = guard.guard_movement(state["guard_location"],
                                                                               state["guard_forward"])


time_down = 0
number_to_save = 0


def user_events():
    pygame.init()
    global time_down
    global number_to_save
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                state["show_mines"] = True

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                state["soldier_location"][1] -= 1

            if event.key == pygame.K_DOWN and state["soldier_location"][1] < consts.GRID_HEIGHT - consts.SOLDIER_HEIGHT:
                state["soldier_location"][1] += 1

            if event.key == pygame.K_RIGHT and state["soldier_location"][0] < consts.GRID_WIDTH - consts.SOLDIER_WIDTH:
                state["soldier_location"][0] += 1

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                state["soldier_location"][0] -= 1

            if event.key in consts.keys_to_save:
                time_down = pygame.time.get_ticks()
                number_to_save = consts.keys_to_save.get(event.key)


        elif event.type == pygame.KEYUP:
            if event.key in consts.keys_to_save:
                time_to_release = pygame.time.get_ticks()

                is_over_second = (time_to_release - time_down) / 1000

                if int(is_over_second) < 1:
                    database.create_df(number_to_save, state)

                else:
                    state = database.retrieve_state(number_to_save, state)

                time_down = 0
                number_to_save = 0


main()
