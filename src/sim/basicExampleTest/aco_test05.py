#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 13:17:38 2021

@author: amts
"""

import networkx as nx
import numpy as np
import random
import acopy

RANDOM_SEED = 1

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

size = 8

G = nx.fast_gnp_random_graph(size, .7)
#G = nx.complete_graph(size)
#G = nx.binomial_tree(size)

for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 4)

pos = nx.spring_layout(G, weight='weight')


#with_labels=true is to show the node number in the output graph
nx.draw(G, pos=pos, with_labels = True, edge_color = 'black',
        width = 1, alpha = 0.7) 

# draw weights on edges
#labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)


class IncompleteGraphSolver(acopy.Solver):
    """My custom solver for incomplete graphs.
    
    If the retry_limit is None then there is no limit. Careful when not setting
    this option since it means there could be infinite or otherwise time
    consuming loops.

    :param int retry_limit: maximum number of tries for each ant to find a tour
    """

    def __init__(self, retry_limit=None):
        super().__init__()
        self.retry_limit = retry_limit

    def _should_retry(self, tries):
        # return true if we should retry given the current number of tries
        if not self.retry_limit:
            return True
        return tries < self.retry_limit

    def find_solutions(self, graph, ants):
        """Return the solutions found for the given ants.

        :param graph: a graph
        :type graph: :class:`networkx.Graph`
        :param list ants: the ants to use
        :return: one solution per ant
        :rtype: list
        """
        # base implementation assumes every ant succeeds:
        # return [ant.tour(graph) for ant in ants]
        
        print(type(ants))
        
        solutions = []
        tries = 0
        for i in range(len(ants)):
            # try until we have a solution or we hit the retry limit
            solution = None
            while solution is None and self._should_retry(tries):
                try:
                    solution = ants[i].tour(graph)
                except KeyError:
                    tries += 1  # try again
            # we may or may not have a solution for every ant
            if solution is not None:
                solutions.append(solution)
        return ants



# then use your custom logic
my_solver = IncompleteGraphSolver()
colony = acopy.Colony(alpha=1, beta=3)
tour = my_solver.solve(G, colony, limit=100)
