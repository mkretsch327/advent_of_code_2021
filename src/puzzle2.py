import pandas as pd
import numpy as np

"""
Part 1: Calculate final horizontal and vertical position, then multiply integers
"""
data = pd.read_csv('data/puzzle2.txt', sep=" ")
data['sign'] = data['step'].apply(lambda x: -1 if x == 'down' else 1)
data['step_vector'] = data['increment']*data['sign']
vertical_mask = data['step'].isin(['up', 'down'])
y_final = data[vertical_mask].step_vector.sum()
x_final = data[~vertical_mask].step_vector.sum()
print(f"Final coordinates - ({x_final}, {y_final}). \n Product is {np.abs(x_final*y_final)}")


"""
Part 2: New commands - still find final position and multiple 

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
"""

data = pd.read_csv('data/example2.txt', sep=" ")
data['sign'] = data['step'].map({'forward': 0, 'up': -1, 'down': 1})
data['step_vector'] = data['increment']*data['sign']
data['aim'], data['x'], data['y'] = 0, 0, 0
data['aim'] = data['step_vector'].cumsum()

data['step_vector'] = data['step'].map({'forward': 1}).fillna(0)*data['increment']
data['x'] = data['step_vector'].cumsum()
data['y'] = (data['aim']*data['step_vector']).cumsum()
data.tail(1)
