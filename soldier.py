import game_field


def soldier_feet_cords(state):
    soldier_feet = [[0, 0], [-1, 0]]
    soldier_feet[1] = state[1] + 2
    soldier_feet[0] = state[0] + 1
    # return soldier_feet
    print(soldier_feet)
