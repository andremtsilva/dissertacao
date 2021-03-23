import acopy
import networkx as nx

def main():
    G = nx.read_graphml('graph_binomial_tree_5.graphml')
    
    print(G.nodes())
    print(nx.get_node_attributes(G, 'IPT'))
    """
    solver = acopy.Solver(rho=.03, q=1)
    colony = acopy.Colony(alpha=1, beta=3)

    tour = solver.solve(G, colony, limit=100)

    print(tour.cost)
    print(tour.nodes)
    """

if __name__ == '__main__':
    main()
