import networkx as nx
import acopy
import random

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
        solutions = []
        tries = 0
        for ant in ants:
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



def main():

    """
    Topology
    """
    size = 5

    G = nx.generators.binomial_tree(size)

    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 4)


#    E = list(G.edges())
#    att_weight = {x: random.randint(1,4) for x in E}
#    nx.set_edge_attributes(G, name="weight", values=att_weight)

    my_solver = IncompleteGraphSolver(retry_limit=1000)
    colony = acopy.Colony(alpha=1, beta=3)

    tour = my_solver.solve(G, colony, limit=100)

    print(tour.cost)
    print(tour.nodes)
    print(tour.path)


if __name__ == '__main__':
    main()

