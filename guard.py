import consts
import time

import screen
import soldier


def guard_movement(location, direction):
    if location[0] == 47 or location[0] == 0:
        direction = not direction
    if direction:
        location[0] += 1
        time.sleep(0.01)
    else:
        location[0] -= 1
        time.sleep(0.01)
    return location, direction


def guard_eat(state):
    if state["soldier_location"] == state["guard_location"]:
        screen.draw_injury(state["soldier_location"])
        return True
    return False
