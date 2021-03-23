import networkx as nx
import random

from AntColonyOptimizer import AntColonyOptimizer


size =10
#size = 4

#G = nx.complete_graph(size)
G = nx.binomial_tree(size)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 4)

M = nx.to_numpy_array(G)
#M = nx.adjacency_matrix(G)

#print(M)



problem = M
optimizer = AntColonyOptimizer(ants=10, evaporation_rate=.1, intensification=2, alpha=1, beta=1,
                               beta_evaporation_rate=0, choose_best=.1)

best = optimizer.fit(problem, 100)
optimizer.plot()

