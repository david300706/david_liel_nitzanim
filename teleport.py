import random

import consts
import random as nd
import soldier


def create_teleports(mines):
    teleports = []
    while len(teleports) != consts.TELEPORT_AMOUNT:
        num1 = nd.randint(4, 47)
        num2 = nd.randint(2, 20)
        if [num1, num2] not in teleports and [num1, num2] not in mines:
            teleports.append([num1, num2])
    print(teleports)
    return teleports


def is_touching(location, field):
    legs = soldier.soldier_feet_cords(location)
    for feet in legs:
        if field[feet[1]][feet[0]] == "tp":
            return True, [[feet[1] - consts.SOLDIER_HEIGHT, feet[0]], [feet[1] - consts.SOLDIER_HEIGHT, feet[0] + 1], [feet[1] - consts.SOLDIER_HEIGHT, feet[0] - 1]]
    return False, ""


def random_teleport(teleports, location):
    location[0] += consts.SOLDIER_HEIGHT
    loc = random.choice(teleports).copy()
    while loc == location:
        loc = random.choice(teleports).copy()
    loc[1] -= consts.SOLDIER_HEIGHT
    return loc
