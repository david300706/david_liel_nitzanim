import consts
import random as nd
import screen
import soldier

game_field_grid = []


def create():
    global game_field_grid
    for row in range(consts.GRID_WIDTH):
        game_field_grid.append([])
        for col in range(consts.GRID_HEIGHT):
            game_field_grid[row].append("free")


create()
for x in game_field_grid:
    print(x)
