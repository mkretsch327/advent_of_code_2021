import numpy as np
import pandas as pd

"""
Part 1: Find optimal horizontal crab placement
- Minimize absolute value of residuals: this is done by the median
"""
with open('data/puzzle7.txt', 'r') as f:
    numbers = f.readline()
    numbers = numbers.split(",")
    start_positions = [int(x) for x in numbers]

start_array = np.array(start_positions)
x_opt = np.median(start_array)#.round()

residuals = np.abs(x_opt - start_array)
fuel_cost = np.sum(residuals)
# x_opt = 321, fuel cost is 335330
print(f"Fuel cost to move to {x_opt} is {fuel_cost}")


"""Part 2: Find optimal horizontal crab placement, 
but with differential cost. Each unit of movement costs 1 extra unit of fuel.

Now: x:opt is 5, fuel is 168 for test
16,1,2,0,4,2,7,1,2,14 -> 
"""

with open('data/puzzle7.txt', 'r') as f:
    numbers = f.readline()
    numbers = numbers.split(",")
    start_positions = [int(x) for x in numbers]

# Test positions
# start_positions = [16,1,2,0,4,2,7,1,2,14]

start_array = np.array(start_positions)[:, np.newaxis]
# Brute force - calculate with grid
grid = np.tile(np.arange(np.max(start_positions)), (start_array.shape[0], 1))
grid_d = start_array - grid
grid_cost = (grid_d*grid_d + np.abs(grid_d))/2
grid_cost = np.sum(grid_cost, axis=0)

x_opt = np.argmin(grid_cost)
print(f"GRID: Fuel cost to move to {x_opt} is {grid_cost[x_opt]}")

# Mean x_opt - test end points of segment since mean could be non-int
x_opt_l, x_opt_h = np.floor(np.mean(start_array)), np.ceil(np.mean(start_array))

cost_func = lambda x: np.sum(((start_array - x)**2 + np.abs(start_array-x))/2)
dl = cost_func(x_opt_l)
dh = cost_func(x_opt_h)
if dl<dh:
    x_opt = x_opt_l
    opt_cost = dl
else:
    x_opt = x_opt_h
    opt_cost = dh
print(f"x_opt from mean is {x_opt}, cost is {opt_cost}")