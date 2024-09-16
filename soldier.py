import game_field


def soldier_feet_cords(soldier, feet):
    soldier_feet = [[0, 0], [-1, 0]]
    soldier_feet[1] = soldier[1] + 2
    soldier_feet[0] = soldier[0] + 1
    # return soldier_feet
    print(soldier_feet)

# def is_eliminated(state):
#     index1 = soldier_feet_cords(stat
#     if soldier_feet_cords(state) == "mine" in game_field:
