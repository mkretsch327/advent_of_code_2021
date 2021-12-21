"""
Advent of Code[About][Events][Shop][Settings][Log Out]Matt Kretschmer 19*
  {year=>2021}[Calendar][AoC++][Sponsors][Leaderboard][Stats]
Our sponsors help make Advent of Code possible:
McGraw Hill - Join us in transforming education. We are looking for talented, passionate, mission-driven software engineers and leaders looking to make a difference globally. COVID has provided the inflection point, come set the direction.
--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
How many paths through this cave system are there that visit small caves at most once?

"""
import numpy as np
from collections import Counter
import networkx as nx
from networkx.algorithms.simple_paths import all_simple_paths


edge_list = []
# Create graph from edge list
with open('data/puzzle12.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        pre, post = line.split('-')
        edge_list.append((pre, post))
G = nx.Graph()
G.add_edges_from(edge_list)
# Set the "seed"
sinks = ['start', 'end']
nn = lambda x: [neighbor for neighbor in G.neighbors(x)]
PATH_COUNTER = []
# Need breadth first with queue, not necessarily
def recursive_search(G, node, visited):
    if node.islower() and (node not in visited):
        if node != "end":
            visited.append(node)    
    # update counter, return if hit end
    if node == 'end':
        PATH_COUNTER.append(1)
        return
    # update counter if i'm at a sink
    if node.islower() and all([x in visited for x in nn(node)]):
        return
    
    # Go to neighbors and traverse
    for new_node in nn(node):
        if new_node.isupper() or (new_node not in visited):
            recursive_search(G, new_node, [*visited])
    return
    
pc = recursive_search(G,'start', [])
print(f"n-paths = {len(PATH_COUNTER)}")

#: Part 1 - answer 3450. 
# Part 2: Same but can visit small caves 2x -> 96528


PATH_COUNTER = []
# Need to correct: ONLY 1 cave can be visited 2x.
# Only continue to a lower node if no places have been visited multiple times
any_vis = lambda c: any([c[n]==2 for n in c.keys() ])
# Need breadth first with queue, not necessarily
def recursive_search_2(G, node, visited):
    if node.islower() and (((visited[node] ==1) and not any_vis(visited)) or ((visited[node] ==0)  ) ):
        if node != 'end':
            visited[node] += 1

    # update counter, return if hit end
    if node == 'end':
        PATH_COUNTER.append(1)
        return
    
    # Go to neighbors and traverse
    for new_node in nn(node):
        if new_node.isupper() or (new_node.islower() and (((visited[new_node] ==1) and not any_vis(visited)) or ((visited[new_node] ==0)  ) )):
            print(visited, node, new_node)
            if new_node != 'start':
                # import pdb;pdb.set_trace()
                recursive_search_2(G, new_node, Counter(visited))
    # import pdb;pdb.set_trace()
    return
from collections import Counter
pc = recursive_search_2(G,'start', Counter())
print(f"n-paths = {len(PATH_COUNTER)}")
