#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:32:26 2021

@author: amts
"""


import os
import time
import json
import random
import logging.config
import operator
import itertools

import networkx as nx
import numpy as np
from pathlib import Path
from collections import defaultdict


from yafs.core import Sim
from yafs.application import create_applications_from_json
from yafs.topology import Topology

from yafs.placement import JSONPlacement
from yafs.path_routing import DeviceSpeedAwareRouting
from yafs.distribution import deterministic_distribution, \
    deterministicDistributionStartPoint

#from yafs.stats import Stats


RANDOM_SEED = 1


class CustomStrategy():
    
    def __init__(self, pathResults):
        self.activations = 0
        self.pathResults = pathResults
        
    def deploy_module(self, sim, service, node):
        app_name = int(service[0:service.index("_")])
        app = sim.apps[app_name]
        services = app.services
        idDES = sim.deploy_module(app_name, service, services[service],
                                  [node])
        # with this `identifier of the DES processs`(idDES) you can control it
        
    def undeploy_module(self, sim, service, node):
        app_name = int(service[0:service.index("_")])
        des = sim.get_DES_from_Service_In_Node(node, app_name, service)
        sim.undeploy_module(app_name, service, des)
        
    def is_already_deployed(self, sim, service_name, node):
        app_name = service_name[0:service_name.index("_")]
        
        all_des = []
        for k, v in sim.alloc_DES.items():
            if v == node:
                all_des.append(k)
                
        # Clearing other related structures
        for des in sim.alloc_module[int(app_name)][service_name]:
            if des in all_des:
                return True
            
    def get_current_services(self, sim):
        """Returns a dictionary with name_service and a list of node where
        they are deployed.
        example: defaultdict(<type 'list'>, {u'2_19': [15], u'3_22': [5]})
        """
        # It returns all entities related to a node: modules, sources/users,
        # etc.
        current_services = sim.get_alloc_entities()
        # here, we only need modules (not users)
        current_services = dict((k, v) for k, v in current_services.items()
                                if len(v)>0)
        deployed_services = defaultdict(list)
        for node, services in current_services.items():
            for service_name in services:
                if not "None" in service_name:
                    deployed_services[service_name[service_name.index("#")+1
                                                   :]].append(node)
                    
        return deployed_services
    
    def __call__(self, sim, routing):
        logging.info(f"Activating Custom Process - number {self.activations}")
        self.activations += 1
        routing.invalid_cache_value = True # when the service change the cache
        # of the Path.routing is outdated.
        
        # Current deployed services
        print("Current deployed services > module: list(nodes)")
        current_services = self.get_current_services(sim)
        print(current_services)
        print(sim.alloc_module)
        
        
        # Defining top nodes by centrality measure
        centrality = nx.betweenness_centrality(sim.topology.G)
        nx.set_node_attributes(sim.topology.G, name="centrality", 
                               values=centrality)
        sorted_clustMeasure = sorted(centrality.items(), 
                                     key=operator.itemgetter(1), reverse=True)
        top4_devices = sorted_clustMeasure[:4]
        
        top4_list = []
        for top in top4_devices:
            top4_list.append(top[0])
            
        
        print(top4_list)
        
        # We add a new module service to other random node.
        # Without duplicating the number of services deployed
        for service in current_services:
            newNode = random.sample(top4_list, 1)[0]
            if not self.is_already_deployed(sim, service, newNode):
                self.deploy_module(sim, service, newNode)
                logging.info(f"Adding new module of Service {service} "
                         f"to {newNode} node")
            
        
               
        """
        # We move all the service to other random node.
        for service in current_services:
            for currentNode in current_services[service]:
                newNode = random.sample(sim.topology.G.nodes(),1)[0]
                if not self.is_already_deployed(sim, service, newNode):
                    self.undeploy_module(sim, service, currentNode)
                    self.deploy_module(sim, service, newNode)
                    logging.info(f"Moving Service {service} from "
                                 f"{currentNode} to {newNode} node")
        """


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
    
    size = 20
    t.G = nx.fast_gnp_random_graph(size, p=0.3, seed=RANDOM_SEED)
    
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
    dataApp = json.load(open('data/appDefinition2.json'))
    apps = create_applications_from_json(dataApp)
    
    # print(apps)

    """
    SERVICE PLACEMENT 
    """
    placementJson = json.load(open('data/allocDefinition2.json'))
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
    userJSON = json.load(open('data/usersDefinition2.json'))
    for user in userJSON["sources"]:
        app_name = user["app"]
        app = s.apps[app_name]
        msg = app.get_message(user["message"])
        node = user["id_resource"]
        dist = deterministic_distribution(100, name="Deterministic")
        idDES = s.deploy_source(app_name, id_node=node, msg=msg, distribution=dist)


    """
    This internal monitor in the simulator (a DES process) changes the sim's
    behaviour. You can have multiples monitors doing different or same tasks.
    
    In this case, it changes the service's allocation, the node where the
    service is.
    """    
    dist = deterministicDistributionStartPoint(stop_time/4.0,
                                               stop_time/6.0,
                                               name="Deterministic")
    evol = CustomStrategy(folder_results)
    s.deploy_monitor("RandomAllocation", evol, dist, 
                     **{"sim": s, "routing": selectorPath}) # __call__ args
    


    """
    RUNNING - last step
    """
    logging.info(f" Performing simulation: {it}")
    s.run(stop_time) # To test deployment put test_initial_deploy a TRUE
    s.print_debug_assignaments()
    
    
    
if __name__ == '__main__':
    
    
    logging.config.fileConfig(os.getcwd() + '/logging.ini')

    nIterations = 1  # iteration for each experiment
    simulationDuration = 1200

    # Iteration for each experiment changing the seed of randoms
    for iteration in range(nIterations):
        logging.info("Running experiment it: - %i" % iteration)

        start_time = time.time()
        main(stop_time=simulationDuration,
             it=iteration)

        print("\n--- %s seconds ---" % (time.time() - start_time))
        
    print("Simulation Done!")
    
    """
    m = Stats(defaultPath="results/sim_trace")
    
    # print ("\tNetwork bytes transmitted:")
    # print (f"\t\t{m.bytes_transmitted():.1f}")
    
    # m.df_link.head(15) # from Stats class
    time_loops = [["M.USER.APP.0"]]

    
    m.showResults2(1000, time_loops=time_loops)
    
    m.compute_times_df()
    """