import game_field
import consts
import screen


def soldier_feet_cords(soldier):
    soldier_feet = [[0, 0], [0, 0]]
    soldier_feet[0][1] = soldier[1] + consts.SOLDIER_HEIGHT - 1
    soldier_feet[0][0] = soldier[0]
    soldier_feet[1][0] = soldier[0] + 1
    soldier_feet[1][1] = soldier[1] + consts.SOLDIER_HEIGHT - 1
    return soldier_feet


def is_eliminated(state):
    x = soldier_feet_cords(state["soldier_location"])
    # print(state["game_field"])
    for feet in x:
        # print(feet)
        if state["game_field"][feet[1]][feet[0]] == "mine":
            screen.draw_explo(state["soldier_location"])
            return True
    return False


def is_winning(state):
    x = soldier_feet_cords(state["soldier_location"])
    for feet in x:
        if feet[0] >= consts.GRID_WIDTH - consts.FLAG_WIDTH and \
                feet[1] >= consts.GRID_HEIGHT - consts.FLAG_HEIGHT:
            return True
    return False
