import consts
import random as nd
import screen
import soldier



def create():
    game_field_grid = []

    # global game_field_grid
    for row in range(consts.GRID_HEIGHT):
        game_field_grid.append([])
        for col in range(consts.GRID_WIDTH):
            game_field_grid[row].append("SAFE")
    mine_spread()
    return game_field_grid




def find_bushes():
    pass


def mine_spread():
    mine_amount = 0
    while mine_amount != 20:
        num1 = nd.randint(0, 24)
        num2 = nd.randint(1, 48)
        while game_field_grid[num1][num2] != "mine" and game_field_grid[num1][num2 - 1] != "mine" and \
                game_field_grid[num1][num2 + 1] != "mine":
            game_field_grid[num1][num2] = "mine"
            game_field_grid[num1][num2 - 1] = "mine"
            game_field_grid[num1][num2 + 1] = "mine"
        mine_amount += 1


def bush_spread():
    bush_cords = []
    for i in range(20):
        num1 = nd.randint(0, consts.SCREEN_HEIGHT - consts.GRASS_HEIGHT * consts.FRAME_HEIGHT)
        num2 = nd.randint(1, consts.SCREEN_WIDTH - consts.GRASS_WIDTH * consts.FRAME_WIDTH)
        bush_cords.append((num2, num1))
    return bush_cords


# mine_spread()
for x in game_field_grid:
    print(x)
