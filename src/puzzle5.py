import numpy as np
from numpy.lib.stride_tricks import broadcast_shapes

"""
Part 1:Read in lists of line segment end points. Find out where at least 2 lines intersect
"""
coords = []
with open('data/puzzle5.txt', 'r') as f:
    for line in f.readlines():
        numbers = line.replace('\n', '')
        start_end = numbers.split(" -> ")
        start = [int(x) for x in start_end[0].split(',')]
        end = [int(x) for x in start_end[1].split(',')]
    
        coords.append(start + end)
coords_array = np.array(coords)
min_x = np.min(coords_array[:,0])
max_x = np.max(coords_array[:,2])
min_y = np.min(coords_array[:,1])
max_y = np.max(coords_array[:,3])

START = 0
END = 1000

# Make a 1000 by 1000 Grid

board = np.zeros((END, END))

for row in coords_array:
    # Horizontal
    if row[0] == row[2]:
        if row[3]< row[1]:
            row[1], row[3] = row[3], row[1] 
        board[row[1]:(row[3]+1), row[0]] += 1
    elif row[1] == row[3]:
        # vertical
        if row[0] > row[2]:
            row[0], row[2] = row[2], row[0]
        board[row[3], row[0]:(row[2]+1)] += 1    
total = (board >= 2).sum()
print(f"Total: {total}")

# 6189 - Correct answer


# Part 2: Diagonal lines too

board = np.zeros((END, END))

for row in coords_array:
    # Horizontal
    if row[0] == row[2]:
        if row[3]< row[1]:
            row[1], row[3] = row[3], row[1] 
        board[row[1]:(row[3]+1), row[0]] += 1
    elif row[1] == row[3]:
        # vertical
        if row[0] > row[2]:
            row[0], row[2] = row[2], row[0]
        board[row[3], row[0]:(row[2]+1)] += 1 
    # diagonal   
    elif np.abs(row[1]-row[3]) == np.abs(row[0]-row[2]):
        sign_x = np.sign(row[3] - row[1])
        sign_y = np.sign(row[2]-row[0])
        """
        (0,0) (0,1) (0,2)
        (1,0) (1,1) (1,2)
        (2,0) (2,1) (2,2)
        """
        
        
        if sign_x < 0 and sign_y < 0:
            x_indices = [x for x in range(row[3], row[1]+1)]
            y_indices = [x for x in range(row[2], row[0]+1)]
        elif sign_x> 0 and sign_y > 0:
            x_indices = [x for x in range(row[1], row[3]+1)]
            y_indices = [x for x in range(row[0], row[2]+1)]
        elif sign_x > 0 and sign_y <0:
            x_indices = [x for x in range(row[1], row[3]+1)]
            y_indices = [x for x in range(row[2], row[0]+1)][::-1]    
        elif sign_y > 0 and sign_x < 0:
            x_indices = [x for x in range(row[3], row[1]+1)][::-1]
            y_indices = [x for x in range(row[0], row[2]+1)]
        board[x_indices, y_indices] += 1
total = (board >= 2).sum()
print(f"Total with diagonals: {total}")
