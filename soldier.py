import game_field


def soldier_feet_cords(soldier):
    soldier_feet = [[0, 0], [-1, 0]]
    soldier_feet[0][1] = soldier[1] + 2
    soldier_feet[0][0] = soldier[0] + 1
    soldier_feet[1][0] = soldier[0] + 1
    soldier_feet[1][1] = soldier[1] + 2
    return soldier_feet


def is_eliminated(state):
    x = soldier_feet_cords(state["soldier_location"])
    for feet in x:
        if state["game_field"][feet[0]][feet[1]] == "mine":
            return True
    return False
