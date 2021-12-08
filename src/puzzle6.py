import numpy as np
import pandas as pd
from collections import Counter

"""
Part 1:Model lantern fish population
Example inputs:
N_GEN = 18 # 26
N_GEN = 80 # 5934

80 days 360268 fish
256 days 1632146183902 fish
"""
N_GEN = 256
with open('data/puzzle6.txt', 'r') as f:
    numbers = f.readline()
    numbers = numbers.split(",")
    starting_pop = [int(x) for x in numbers]

starting_gens  = Counter(starting_pop)
starting_ints = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for starting_pop in starting_ints:
    if starting_pop not in starting_gens:
        starting_gens[starting_pop] = 0
df = pd.DataFrame.from_dict(starting_gens, orient='index')
# Sort values
df = df.loc[df.index.sort_values()]
for gen in range(1, N_GEN+1):
    ng_df = df[gen-1].copy()
    # Shift indices
    ng_df.index -= 1
    ng_df = ng_df.to_frame().rename(columns={(gen-1):gen})
    df = df.join(ng_df, how='left', rsuffix=f"_{gen}")
    df.fillna(0, inplace=True)
    # Reset timers
    df[gen].loc[6] = df[gen-1].loc[0] + df[gen].loc[6]
    # Make new fish
    df[gen].loc[8] = df[gen-1].loc[0] + df[gen].loc[8]


print(f"After {gen} generations there are {df[gen].sum()} fish")


"""
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""
# Same as above, with gen = 256