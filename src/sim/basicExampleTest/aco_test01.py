import networkx as nx
import numpy as np
import acopy
import random


RANDOM_SEED = 1

def main():

    """
    Topology
    """
    # Fix position of nodes for drawing
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    
        
    size = 10

    G = nx.complete_graph(size)

    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 4)

    pos = nx.spring_layout(G, weight='weight')
    nx.draw(G, pos, with_labels = True, edge_color = 'black' ,
            width = 1, alpha = 0.7) 
    
    labels = nx.get_edge_attributes(G,'weight')
    #nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    
    #    E = list(G.edges())
    #    att_weight = {x: random.randint(1,4) for x in E}
    #    nx.set_edge_attributes(G, name="weight", values=att_weight)
    
    solver = acopy.Solver(rho=.03, q=1)
    colony = acopy.Colony(alpha=1, beta=3)
    
    tour = solver.solve(G, colony, limit=100)
    
    print(f"The tour cost is: {tour.cost}")
    print()
    print(f"The tous passing nodes are: {tour.nodes}")
    print()
    print(f"The tour path is: {tour.path}")


if __name__ == '__main__':
    main()

