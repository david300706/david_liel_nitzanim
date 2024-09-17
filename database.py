import pandas as pd
import game_field

state1 = {"bushes": game_field.bush_spread(),
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [],
         "game_field": game_field.create(),
         "show_mines": False,
         "is_winning": False,
         "is_losing": False,
         }

state1["game_field"], state1["mines"] = game_field.create()
# print(state)


def create_df(number, state):
    state_list = [state[i] for i in state.keys()]
    df = pd.DataFrame({number:state})


def retrieve_state(number, state):
    df = pd.read_csv('FlagGameSave.csv')
    df.to_dict()
    df = df[number]

    count = 0
    for i in state.keys():
        state[i] = df[count]
        count += 1
    return state
