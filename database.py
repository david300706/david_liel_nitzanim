import pandas as pd

# import game_field

# print(state)

df = pd.DataFrame(list())
df.to_csv("FlagGameSave.csv")


def create_df(number, state):
    df = pd.read_csv("FlagGameSave.csv")
    state_list = [state[i] for i in state.keys()]
    df[number] = state_list
    df.to_csv("FlagGameSave.csv")


def retrieve_state(number, state):
    df = pd.read_csv('FlagGameSave.csv')
    df.to_dict()
    df = df[number]

    count = 0
    for i in state.keys():
        state[i] = df[count]
        count += 1
    return state
