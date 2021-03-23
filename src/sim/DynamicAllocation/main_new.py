#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:06:16 2021

@author: amts
"""

import networkx as nx


from pathlib import Path


from yafs.topology import Topology
from yafs.core import Sim

def main(stop_time, it):
    #folder_results = Path("results/")
    #folder_results.mkdir(parents=True, exist_ok=True)
    #folder_results = str(folder_results)+"/"
    
    
    """
    TOPOLOGY
    """
    
    t = Topology()
    
    size = 400
    t.G = nx.random_geometric_graph(size, 0,2)
    
    nx.draw(t.G, with_labels = True, edge_color = 'black' ,
        width = 1, alpha = 0.7) 
    

if __name__ == '__main__':
    
    # loggin.config.fileConfig(os.getcwd() + '/logging.ini')
    
    nIterations = 1
    simulationDuration = 20000
    
    main(stop_time=simulationDuration, it=nIterations)