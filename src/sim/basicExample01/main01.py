#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:21:57 2021

@author: amts
"""

import os
import time
import json
import random
import logging.config

import networkx as nx
import numpy as np
from pathlib import Path

from yafs.core import Sim
from yafs.application import create_applications_from_json
from yafs.topology import Topology

from yafs.placement import JSONPlacement
from yafs.path_routing import DeviceSpeedAwareRouting
from yafs.distribution import deterministic_distribution
from yafs.stats import Stats


RANDOM_SEED = 1



def main(stop_time, it):
    
    folder_results = Path("results/")
    folder_results.mkdir(parents=True, exist_ok=True)
    folder_results = str(folder_results)+"/"
    
    """
    TOPOLOGY
    """
    # Fix position of nodes for drawing
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    
    t = Topology()
    
    size = 5
    t.G = nx.fast_gnp_random_graph(size, p=0.7, seed=RANDOM_SEED)
    
    #ls = list(t.G.nodes)
    #li = {x: int(x) for x in ls}
    #nx.relabel_nodes(t.G, li, False) # Transform str-labels to int-labels
    
    # Graph visualization
    pos = nx.spring_layout(t.G)
    nx.draw(t.G, pos, with_labels=True, edge_color='black', width=1, 
            alpha=0.7)
    
    
    print(f"Nodes: {len(t.G.nodes())}")
    print(f"Edges: {len(t.G.edges())}")
    
    # Definition of mandatory attributes of a Topology
    ## Attr. on edges
    # PR (link propagation) and BW (bandwith) are 1 unit
    attPR_BW = {x: random.randint(1,1) for x in t.G.edges()}
    nx.set_edge_attributes(t.G, name="PR", values=attPR_BW)
    nx.set_edge_attributes(t.G, name="BW", values=attPR_BW)
    
    ## Attr. on nodes
    # IPT
    attIPT = {x: random.randrange(100, 900, 100) for x in t.G.nodes()}
    nx.set_node_attributes(t.G, name="IPT", values=attIPT)
    
    # nx.write_gexf(t.G,folder_results+"graph_binomial_tree_%i"%size) # you can export the Graph in multiples format to view in tools like Gephi, and so on.
    nx.write_graphml(t.G,folder_results+"graph.graphml")
    
    
    """
    APPLICATION or SERVICES
    """
    dataApp = json.load(open('data/appDefinition1.json'))
    apps = create_applications_from_json(dataApp)
    
    # print(apps)

    """
    SERVICE PLACEMENT 
    """
    placementJson = json.load(open('data/allocDefinition1.json'))
    placement = JSONPlacement(name="Placement", json=placementJson)

    """
    Defining ROUTING algorithm to define how path messages in the topology among modules
    """
    selectorPath = DeviceSpeedAwareRouting()

    """
    SIMULATION ENGINE
    """
    s = Sim(t, default_results_path=folder_results+"sim_trace")

    """
    Deploy services == APP's modules
    """
    for aName in apps.keys():
        s.deploy_app(apps[aName], placement, selectorPath) # Note: each app can have a different routing algorithm

    """
    Deploy users
    """
    userJSON = json.load(open('data/usersDefinition1.json'))
    for user in userJSON["sources"]:
        app_name = user["app"]
        app = s.apps[app_name]
        msg = app.get_message(user["message"])
        node = user["id_resource"]
        dist = deterministic_distribution(100, name="Deterministic")
        idDES = s.deploy_source(app_name, id_node=node, msg=msg, distribution=dist)





    """
    RUNNING - last step
    """
    logging.info(" Performing simulation: %i " % it)
    s.run(stop_time)  # To test deployments put test_initial_deploy a TRUE
    s.print_debug_assignaments()
    
    
    
if __name__ == '__main__':
    
    
    logging.config.fileConfig(os.getcwd() + '/logging.ini')

    nIterations = 1  # iteration for each experiment
    simulationDuration = 200

    # Iteration for each experiment changing the seed of randoms
    for iteration in range(nIterations):
        logging.info("Running experiment it: - %i" % iteration)

        start_time = time.time()
        main(stop_time=simulationDuration,
             it=iteration)

        print("\n--- %s seconds ---" % (time.time() - start_time))
        
    print("Simulation Done!")
    
    m = Stats(defaultPath="results/sim_trace")
    
    # print ("\tNetwork bytes transmitted:")
    # print (f"\t\t{m.bytes_transmitted():.1f}")
    
    # m.df_link.head(15) # from Stats class
    time_loops = [["M.USER.APP.0"]]

    
    m.showResults2(1000, time_loops=time_loops)
    
    m.compute_times_df()
    
    