#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:17:38 2021

@author: amts
"""

import networkx as nx
import random

size = 15

G = nx.fast_gnp_random_graph(size, .3)
#G = nx.complete_graph(size)
#G = nx.binomial_tree(size)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 4)

pos = nx.spring_layout(G, weight='weight')

# test function
def distance(start, end):
    global G
    return nx.shortest_path_length(G, source=start, target=end,
                                   weight='weight' )

t = distance(0, 12)

print(t)


#with_labels=true is to show the node number in the output graph
nx.draw(G, pos=pos, with_labels = True, edge_color = 'black' ,
        width = 1, alpha = 0.7) 

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)

