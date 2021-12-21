"""
--- Day 15: Chiton ---
You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

What is the lowest total risk of any path from the top left to the bottom right?
"""
import numpy as np
import networkx as nx
# read into x
num_list = []
with open('data/puzzle15.txt', 'r') as f:
    for numbers in f.readlines():
        numbers = numbers.replace('\n', '')
        numbers = [int(x) for x in numbers]
        num_list.append(numbers)

# make edge-list
edge_list = []
max_x = len(num_list)
max_y = len(num_list[0])
for idx, row in enumerate(num_list):
    for idy, val in enumerate(row):
        # up # remembering cost of val for *entering idx,idy
        if idy-1 >= 0:
            edge_list.append(((idx,idy-1),(idx,idy), val))
        # down
        if idy+1 < max_y:
            edge_list.append(((idx,idy+1),(idx,idy), val))
        # left
        if idx-1>=0:
            edge_list.append(((idx-1,idy),(idx,idy), val))
        if idx+1 < max_x:
            edge_list.append(((idx+1,idy),(idx,idy), val))

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_weighted_edges_from(edge_list, weight='weight')
shortest_path_length = nx.shortest_path_length(G, source=(0,0), target=(max_x-1,max_y-1), weight='weight')
print(f"Shortest path length is {shortest_path_length}")

# P1 - 698
# P2 - Tile existing and add then modulo 9
num_array = np.array(num_list)

p2_grid = np.concatenate([np.concatenate([num_array+idx+idy for idx in range(5)], axis=1) for idy in range(5)],axis=0)
p2_grid[p2_grid>=10] -=9

num_list = p2_grid.tolist()
# make edge-list
edge_list = []
max_x = len(num_list)
max_y = len(num_list[0])
for idx, row in enumerate(num_list):
    for idy, val in enumerate(row):
        # up # remembering cost of val for *entering idx,idy
        if idy-1 >= 0:
            edge_list.append(((idx,idy-1),(idx,idy), val))
        # down
        if idy+1 < max_y:
            edge_list.append(((idx,idy+1),(idx,idy), val))
        # left
        if idx-1>=0:
            edge_list.append(((idx-1,idy),(idx,idy), val))
        if idx+1 < max_x:
            edge_list.append(((idx+1,idy),(idx,idy), val))

G = nx.DiGraph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_weighted_edges_from(edge_list, weight='weight')
print(f'Num list size = {max_x, max_y}')
shortest_path_length = nx.shortest_path_length(G, source=(0,0), target=(max_x-1,max_y-1), weight='weight')
print(f"Shortest path length is {shortest_path_length}")

# p2 3022