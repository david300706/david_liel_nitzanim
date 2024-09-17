import pandas as pd
import game_field

state = {"bushes": game_field.bush_spread(),
         "game_running": True,
         "soldier_location": [0, 0],
         "soldier_feet_location": [],
         "game_field": game_field.create(),
         "show_mines": False,
         "is_winning": False,
         "is_losing": False,
         }

state["game_field"], state["mines"] = game_field.create()
# print(state)

df = pd.DataFrame(list())
df.to_csv("FlagGameSave.csv")


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
