"""Part 1: Find the initial velocity that causes the probe to reach the highest y position and 
still eventually be within the target area after any step. What is the highest y position it 
reaches on this trajectory?"""
import numpy as np
# target area: x=138..184, y=-125..-71
target_x = [138,184]
target_y = [-125, -71]


starting = np.array([0,0])

"""
The probe's x position increases by its x velocity.
The probe's y position increases by its y velocity.
Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, 
it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, 
or does not change if it is already 0.
Due to gravity, the probe's y velocity decreases by 1.
"""

# Time to zero x velocity: np.abs(v0x)
# So to hit target area, v0x needs to be in 138 to 184
# t_high = v_high
# y(t) = vo_y*t - t^2 / 2
# Cause of decreasing ingeers, total x distance is v0*(v0+1)/2!
# Max height reached is (v0y*v0y+1)/2

"""
So: max height is (v0y*(v0y+1)/2)
x_final = (v0x*(v0x+1)/2)
Timesteps to hit x_final: v0x
peak_height
"""
target_x = [138,184]
target_y = [-125, -71]
max_height = 0
for v0x in range(1, 185):
    for v0y in range(500):
        x = 0
        y = 0
        vx = v0x
        vy = v0y
        y_max = 0
        for t in range(500):
            x += vx
            y += vy
            vx -= 1
            if vx < 0:
                vx = 0
            vy -= 1
            if max(y, y_max) > y_max:
                y_max = y
            if (x >= target_x[0] and x<= target_x[1]) and \
               (y >= target_y[0] and y<= target_y[1]):
                print(f'Leaving with v0y = {v0y} and v0x = {v0x}, at {x},{y}. Max height was {y_max}')
                break
        if max(y_max,max_height) > max_height:
            max_height = y_max
            print(v0x,v0y, max_height)
# p1: brute force: 7750 is max height: v0x 24, v0y 185
counter = 0

for v0x in range(1, target_x[1]+1):
    for v0y in range(-126,500):
        x = 0
        y = 0
        vx = v0x
        vy = v0y
        y_max = 0
        for t in range(500):
            x += vx
            y += vy
            vx -= 1
            if vx < 0:
                vx = 0
            vy -= 1
            if (x >= target_x[0] and x<= target_x[1]) and \
               (y >= target_y[0] and y<= target_y[1]):
               counter += 1
               break
print(f"Total number of good trajectories are {counter}")
#p2 4120 (brute force)