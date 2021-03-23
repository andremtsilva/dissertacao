#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 07:57:49 2021

@author: amts
"""

import networkx as nx
import random
from ant_colony import ant_colony
import math


size =16
#size = 4

G = nx.fast_gnp_random_graph(size, .3)
#G = nx.complete_graph(size)
#G = nx.binomial_tree(size)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(2, 5)

#M = nx.to_numpy_array(G)
#M = nx.adjacency_matrix(G)

#print(M)


pos = nx.spring_layout(G, weight='weight')


new_pos = {}

for key, arr in pos.items():
    new_pos.update({key: tuple(arr)})

#with_labels=true is to show the node number in the output graph
nx.draw(G, pos=pos, with_labels = True, edge_color = 'black' ,
        width = 1, alpha = 0.7) 

labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

# print(type(new_pos.keys()))



# given some nodes, and some locations...
test_nodes = new_pos


"""
# function to get distance between nodes
def distance(start, end):
    x_distance = abs(start[0] - end[0])
    y_distance = abs(start[1] - end[1])
    
    # c = sqrt(a² + b²)
    return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))
"""


# test function
def distance(start, end):
    global G
    return nx.shortest_path_length(G, source=start, target=end,
                                   weight='weight' )
    # erro division by zero


# make a colony of ants
colony = ant_colony(test_nodes, distance)

# that will find the optimal, solution with ACO
answer = colony.mainloop()

