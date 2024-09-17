import consts
import time


def guard_movement(location, direction):
    if location[0] == 47 or location[0] == 0:
        direction = not direction
        print(direction)
    if direction:
        location[0] += 1
        time.sleep(0.1)
    else:
        location[0] -= 1
        time.sleep(0.1)
    return location, direction
