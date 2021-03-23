# -*- coding: utf-8 -*-
"""
Spyder Editor


"""

import networkx as nx
import random



#size =10
size = 4

#G = nx.complete_graph(size)
G = nx.binomial_tree(size)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 4)

#M = nx.to_numpy_array(G)
#M = nx.adjacency_matrix(G)

#print(M)
 

pos = nx.spring_layout(G)

print(pos)
   
def create_graph(n):
    number_nodes = n
    p = 0.4
    G = nx.fast_gnp_random_graph(number_nodes, p)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 4)
    return G
