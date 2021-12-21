"""Reflection and "folds"
Count how many visible dots, when given the coordinates of the original dots



For vertical folds (at y = F)
if y > F:
    y = 2*F - y

if x > F:
    x = 2*F - y


for transformation in transformations:
    if 
    for pt in points_list:


"""
fold_list = [] 
with open('data/puzzle13a.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '').replace('fold along ', '')
        axis, val = line.split('=')
        fold_list.append((axis, int(val)))

coord_list = []
with open('data/puzzle13.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        x, y = line.split(',')
        coord_list.append((int(x), int(y)))
# fold_list = [fold_list[0]] # uncomment to run part 1
for fold in fold_list:
    print(f"Fold is: {fold} ")
    new_coord_list = []
    for idx, (x0,x1) in enumerate(coord_list):
        if fold[0] == 'x' and x0 > fold[1]:
            x0_new =  2*fold[1]- coord_list[idx][0]
            print(f"{x0},{x1} goes to {x0_new, x1}")
            new_coord_list.append((x0_new, x1))
        elif fold[0] == 'y' and x1 > fold[1]:
            x1_new = 2*fold[1] - coord_list[idx][1]
            print(f"{x0},{x1} goes to {x0, x1_new}")
            new_coord_list.append((x0, x1_new))
        else:
            new_coord_list.append((x0,x1))
    coord_list = new_coord_list

print(f"The number of remaining dots is {len(set(coord_list))}")

import numpy as np
coords = set(coord_list)
max_x = np.max([x[0] for x in coords])
max_y = np.max([x[1] for x in coords])
viz = np.zeros((max_x+1, max_y+1))

coords = set(coord_list)
for x,y in coords:
    viz[x,y] +=100
print(viz)
for i in range(1,9):
    print(viz[5*(i-1):(5*i),:].T)
    print('\n\n\n')
# Part 1: 653 are visible if you do only 1 fold