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
         "soldier_feet_location": []
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

            if event.key == pygame.K_UP and state["soldier_location"][1] > 0:
                print("Key UP has been pressed")
                state["soldier_location"][1] -= consts.FRAME_HEIGHT

            if event.key == pygame.K_DOWN and state["soldier_location"][
                1] < consts.SCREEN_HEIGHT - consts.SOLDIER_Y_LENGTH:
                print("Key DOWN has been pressed")
                state["soldier_location"][1] += consts.FRAME_HEIGHT

            if event.key == pygame.K_RIGHT and state["soldier_location"][
                0] < consts.SCREEN_WIDTH - consts.SOLDIER_X_LENGTH:
                print("Key RIGHT has been pressed")
                state["soldier_location"][0] += consts.FRAME_WIDTH

            if event.key == pygame.K_LEFT and state["soldier_location"][0] > 0:
                print("Key LEFT has been pressed")
                state["soldier_location"][0] -= consts.FRAME_WIDTH


user_events()

# soldier.soldier_feet_cords(state["soldier_location"])
main()
