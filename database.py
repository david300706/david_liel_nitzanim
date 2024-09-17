import pandas as pd
import os

if not os.path.exists("FlagGameSave.csv"):
    df = pd.DataFrame(list())
    df.to_csv("FlagGameSave.csv")


def create_df(number, state):
    df = pd.read_csv("FlagGameSave.csv")
    state_list = [state[i] for i in state.keys()]
    df[str(number)] = state_list
    df.to_csv("FlagGameSave.csv")


def retrieve_state(number, state):
    df = pd.read_csv('FlagGameSave.csv')

    new_state = list(df[str(number)])
    count = 0
    for i in state.keys():
        state[i] = eval(new_state[count])
        count += 1
    print(state)

    return state
