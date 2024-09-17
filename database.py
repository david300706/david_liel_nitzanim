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
df = [state[i] for i in state.keys()]
print(df)
df = pd.DataFrame({1:df})
# df[2] = df

for i in df:
    print(df[i])

df.to_dict()
df = df[1]


args = list(state.keys())
