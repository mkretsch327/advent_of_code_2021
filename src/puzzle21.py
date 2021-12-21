import numpy as np

x1 = 6
x2 = 9 



N_TURNS = 100
p1_points = 0
p2_points = 0
dice_rols = np.arange(100)
n = 1
while p1_points < 1000 and p2_points < 1000:
    if n%2 == 1:
        p1_rolls = np.arange(3*(n-1), 3*n)+1
        x1 += np.sum(p1_rolls)
        # mod x1
        x1 %= 10
        if x1 == 0:
            x1+=10
        p1_points += x1
        print(f"Player 1 rolls {p1_rolls} and moves to space {x1} for a total score of {p1_points}")
    elif n%2 == 0:
        p2_rolls = np.arange(3*(n-1), 3*n)+1
        x2 += np.sum(p2_rolls)
        x2 %=10
        if x2 == 0:
            x2 += 10 
        p2_points += x2
        # print(f"Player 2 rolls {p2_rolls} and moves to space {x2} for a total score of {p2_points}")
    n += 1
min_points = min(p1_points, p2_points)
print(f"Score is {3*(n-1)*min_points}. Turn {n}")
# p1 answer: 925605

# Part 2:
# dice roll is 0, 1 or 2 with equal probability
x1 = 6
x2 = 9 

n = 1
from collections import Counter
from itertools import product

def mod_sum(x,y):
    v = (x+y)%10
    if v == 0:
        v+=10
    return v


# elem_update = lambda x,y: {mod_sum(e[0][0],e[1]):e[0][1] for e in product(x.items(),y)}

def elem_update(x,y):
    return_dict = {}
    for e in product(x.items(),y):
        k, v = mod_sum(e[0][0],e[1]), e[0][1]
        if k in return_dict:
            return_dict[k]+=v
        else:
            return_dict[k]=v
    return return_dict
def cust_count(states):
    return_dict = {}
    for k,v in states.items():
        if k[1] in return_dict:
            return_dict[k[1]] +=v
        else:
            return_dict[k[1]]=v
    return return_dict

pts_update = lambda x,y: [e[0]+e[1] for e in product(x,y)]

p1_states = {(6,0):1}
p2_states = {(9,0):1}
def update_pos_pts(states, rolls):
    new_states = {}
    rolls = Counter(rolls)
    for s in states:
        for r in rolls:
            new_state = mod_sum(s[0],r)
            new_pts = s[1]+new_state
            if (new_state, new_pts) not in new_states:
                # import pdb;pdb.set_trace()
                new_states[(new_state, new_pts)] = states[s]*rolls[r]
            else:
                # import pdb;pdb.set_trace()
                new_states[(new_state, new_pts)] += states[s]*rolls[r]
    return new_states

n=0
moves = [sum(x) for x in product([1,2,3],[1,2,3],[1,2,3])]
p1_counter = {}
p2_counter = {}
m1_games = 0
m2_games = 0
while n<22:
    if n%2 == 0:
        p1_states = update_pos_pts(p1_states, moves)
        p1_counter = cust_count(p1_states)
        print(f'Player 1 total states: {sum(p1_counter.values())}')

    else:
        p2_states = update_pos_pts(p2_states, moves)
        p2_counter = cust_count(p2_states)
        print(f'Player 2 total states: {sum(p2_counter.values())}')

    n+=1
    # Check if games won
    if any([x>=21 for x in p1_counter.keys()]) or any([x>=21 for x in p2_counter.keys()]):
        m1 = sum([v for k,v in p1_counter.items() if k>=21])
        m2 = sum([v for k,v in p2_counter.items() if k>=21])
        # Each game wins * number of ways p2 lost
        if m1>0:
            m1_games += m1*sum([v for k,v in p2_counter.items() if k<21])
        if m2 > 0:
            # p1 lost. p2 won m2 games, each of p1_counter < 21 times
            m2_games += m2*sum([v for k,v in p1_counter.items() if k<21])
        # Remake counters because they're only updated every other tern
        p1_states = {k:v for k,v in p1_states.items() if k[1]<21}
        p1_counter = cust_count(p1_states)
        p2_states = {k:v for k,v in p2_states.items() if k[1]<21}
        p2_counter = cust_count(p2_states)

print(f"Game counter is {m1_games} and {m2_games} and {m1_games+m2_games}")
