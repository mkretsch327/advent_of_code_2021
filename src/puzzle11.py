"""Let's model some octopus flashing"""
import numpy as np

coord_list = []
with open('data/puzzle11.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        coord_list.append([int(x) for x in line])
cave = np.array(coord_list)

flash_counter = 0
N_SIM = 1000

x0r, x1r = cave.shape
cave_embed = np.ones((x0r+2, x1r+2))*-1
x_max, y_max = cave_embed.shape

cave_embed[1:(x_max-1), 1:(y_max-1)] = cave

def mask(i,j,x,t):
    n_up = (x[(i-1):(i+2), (j-1):(j+2)] >= 10).sum() - (x[i,j]>=10).astype(int)
    if t[i,j] == 0:
        r = x[i,j]+n_up
    else:
        r = x[i,j] 
    return r

for gen in range(N_SIM):
    cave_embed[1:(x_max-1), 1:(y_max-1)] += 1 
    tracker = np.zeros_like(cave_embed)
    counter = 0
    if cave_embed[1:(x_max-1), 1:(y_max-1)].sum()==(x0r*x1r):
        print(f'Synced at {gen}')
        break
    while ((cave_embed>=10).sum()) > 0:
        cave_update = np.copy(cave_embed)
        # import pdb;pdb.set_trace()

        for x0 in range(1, x_max-1):
            for x1 in range(1, y_max-1):
                cave_update[x0,x1] = mask(x0,x1,cave_embed, tracker)
        # reset if greater than 10
        tracker[cave_update>=10] = 1
        cave_update[cave_embed >=10] = 0
        cave_embed = cave_update
        counter += 1
    flash_counter += (tracker ==1).sum()

