"""These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678
Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

input map -> answer is 518
"""
import numpy as np
# read into x
num_list = []
with open('data/puzzle9.txt', 'r') as f:
    for numbers in f.readlines():
        numbers = numbers.replace('\n', '')
        numbers = [int(x) for x in numbers]
        num_list.append(numbers)
x = np.array(num_list)
y = np.ones((x.shape[0]+2, x.shape[1]+2))*11
x_max, y_max = y.shape

y[1:(x_max-1), 1:(y_max-1)] = x
# Gets the "highest" points -> but should just multiply everything else by -1
high_points = (np.roll(y,1,axis=1)>y) & (np.roll(y,1,axis=0)>y) &\
     (np.roll(y,-1,axis=0)>y) & (np.roll(y,-1,axis=1)>y)

n_high_points = np.sum(high_points)
risk_scores = np.sum(high_points*y) + n_high_points
print(f"Sum of lowest points is {risk_scores}")


"""
PART 2: FInd size of top 3 basins and  multipy their sizes together.
Will need to grow, and ignore /stop when basins combine.
A basin  is all the points which are directly uphill from a sink.

Potentially: For each seed. Start from mask, and update immediate neighbors if feasible.
Reset boundaries
"""
