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
    game_field_grid = mine_spread(game_field_grid)
    return game_field_grid





def find_bushes():
    pass


def mine_spread(game_field):
    game_field_grid = game_field
    mine_amount = 0
    mines = []
    while mine_amount != 20:
        num1 = nd.randint(3, 48)
        num2 = nd.randint(2, 24)
        while game_field_grid[num2][num1] != "mine" and game_field_grid[num2][num1 -1] != "mine" and \
                game_field_grid[num2][num1 + 1] != "mine":
            game_field_grid[num2][num1] = "mine"
            game_field_grid[num2][num1 - 1] = "mine"
            game_field_grid[num2][num1 + 1] = "mine"
            mines.append((num1, num2))
        mine_amount += 1
    return game_field_grid, mines


def bush_spread():
    bush_cords = []
    for i in range(20):
        num1 = nd.randint(0, consts.SCREEN_HEIGHT - consts.GRASS_HEIGHT * consts.FRAME_HEIGHT)
        num2 = nd.randint(1, consts.SCREEN_WIDTH - consts.GRASS_WIDTH * consts.FRAME_WIDTH)
        bush_cords.append((num2, num1))
    return bush_cords


# mine_spread()
# for x in game_field_grid:
#     print(x)
