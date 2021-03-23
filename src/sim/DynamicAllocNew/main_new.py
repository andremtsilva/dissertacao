#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:42:54 2021

@author: amts
"""
import random
import numpy as np
import networkx as nx
#import copy
import operator
import logging.config
import os
import time
import argparse

from pathlib import Path

from yafs.core import Sim
from yafs.application import Application,Message
from yafs.topology import Topology
from yafs.placement import NoPlacementOfModules
from yafs.distribution import deterministic_distribution
from yafs.distribution import deterministicDistributionStartPoint
from yafs.population import Population
from yafs.path_routing import DeviceSpeedAwareRouting


RANDON_SEED = 1

def create_application(name):
    # Application
    a = Application(name=name)
    
    a.set_modules([{"Generator":{"Type":Application.TYPE_SOURCE}},
                   {"Actuator": {"Type": Application.TYPE_SINK}}
                   ])
    
    m_egg = Message("M.Action", "Generator", "Actuator", instructions=100,
                    bytes=10)
    a.add_source_messages(m_egg)
    return a

class Evolutive(Population):

    def __init__(self,fog,srcs, **kwargs):
       #TODO arreglar en otros casos
        self.fog_devices = fog
        self.number_generators = srcs
        super(Evolutive, self).__init__(**kwargs)

    def initial_allocation(self, sim, app_name):
        #ASSIGNAMENT of SOURCE - GENERATORS - ACTUATORS
        id_nodes = list(sim.topology.G.nodes())
        for ctrl in self.src_control:
            msg = ctrl["message"]
            dst = ctrl["distribution"]
            for item in range(self.number_generators):
                id = random.choice(id_nodes)
                for number in range(ctrl["number"]):
                    idsrc = sim.deploy_source(app_name, id_node=id, msg=msg, 
                                              distribution=dst)

        # ASSIGNAMENT of the first SINK
        fog_device = self.fog_devices[0][0]
        del self.fog_devices[0]
        for ctrl in self.sink_control:
            module = ctrl["module"]
            for number in range(ctrl["number"]):
                sim.deploy_sink(app_name, node=fog_device, module=module)


    def run(self, sim):
        if len(self.fog_devices)>0:
            fog_device = self.fog_devices[0][0]
            del self.fog_devices[0]
            self.logger.debug("Activiting - RUN - Evolutive - Deploying a new" 
                              "actuator at position: %i"%fog_device)
            for ctrl in self.sink_control:
                module = ctrl["module"]
                app_name = ctrl["app"]
                for number in range(ctrl["number"]):
                    sim.deploy_sink(app_name, node=fog_device, module=module)



def main(stop_time, it):
    
    folder_results = Path("results/")
    folder_results.mkdir(parents=True, exist_ok=True)
    folder_results = str(folder_results)+"/"
    
    """
    TOPOLOGY
    """
    # Fix position of nodes for drawing
    random.seed(RANDON_SEED)
    np.random.seed(RANDON_SEED)
    
    t = Topology()
    
    size = 40
    t.G = nx.fast_gnp_random_graph(size, p=0.2, seed=RANDON_SEED)
    
    ls = list(t.G.nodes)
    li = {x: int(x) for x in ls}
    nx.relabel_nodes(t.G, li, False) # Transform str-labels to int-labels
    
    # Graph visualization
    """
    pos = nx.spring_layout(t.G)
    nx.draw(t.G, pos, with_labels=True, edge_color='black', width=1, 
            alpha=0.7)
    """
    
    print(f"Nodes: {len(t.G.nodes())}")
    print(f"Edges: {len(t.G.edges())}")
    
    # Definition of mandatory attributes of a Topology
    ## Attr. on edges
    # PR (link propagation) and BW (bandwith) are 1 unit
    attPR_BW = {x: random.randint(1,3) for x in t.G.edges()}
    nx.set_edge_attributes(t.G, name="PR", values=attPR_BW)
    nx.set_edge_attributes(t.G, name="BW", values=attPR_BW)
    
    ## Attr. on nodes
    # IPT
    attIPT = {x: random.randrange(100, 900, 100) for x in t.G.nodes()}
    nx.set_node_attributes(t.G, name="IPT", values=attIPT)
    
    # Centrality measures
    centrality = nx.betweenness_centrality(t.G)
    nx.set_node_attributes(t.G, name="centrality", values=centrality)

    sorted_clustMeasure = sorted(centrality.items(), 
                                 key=operator.itemgetter(1), reverse=True)
    
    top5_devices = sorted_clustMeasure[:5]
    # main_fog_devices = copy.copy(top5_devices[0][0])
    
    print("-" * 20)
    print("Top 5 centralized nodes:")
    for item in top5_devices:
        print(item)
    print("-" * 20)
    
    """
    APPLICATION
    """
    apps = create_application("apps")
    
    """
    PLACEMENT
    """
    # There are no modules to place
    placement = NoPlacementOfModules("NoPlacement")
    
    """
    USERS or Messages generators
    """
    number_generators = int(len(t.G)*0.1)
    print(f"Number of users {number_generators}")
    
    dDistribution = deterministicDistributionStartPoint(3000,300,
                                                        name="Deterministic")
    dDistributionSrc = deterministic_distribution(name="Deterministic",
                                                  time=10)
    
    pop1 = Evolutive(top5_devices,number_generators,name="top",
                     activation_dist=dDistribution)
    
    pop1.set_sink_control({"apps":apps.name,"number": 1, 
                           "module": apps.get_sink_modules()})
    
    pop1.set_src_control(
        {"number": 1, "message": apps.get_message("M.Action"), 
         "distribution": dDistributionSrc})
    
   
    
    
    """
    Defining ROUTING algorithm to define how path messages in the topology 
    among modules
    """
    selectorPath = DeviceSpeedAwareRouting()
    
    
    """
    SIMULATION ENGINE
    """
    s = Sim(t, default_results_path=folder_results+"sim_trace")
    
    """
    Deploy services == APP's modules
    """
    s.deploy_app(apps, placement, selectorPath)
    
    
   
   
    #s.deploy_monitor("DynamicAlloc", pop1, dDistribution)
    
    """
    RUNNING - last step
    """
    logging.info(" Performing simulation: %i " % it)
    s.run(stop_time)
    s.print_debug_assignaments()
    
    
if __name__ == '__main__':
    
    
    logging.config.fileConfig(os.getcwd() + '/logging.ini')

    nIterations = 1  # iteration for each experiment
    simulationDuration = 12000

    # Iteration for each experiment changing the seed of randoms
    for iteration in range(nIterations):
        logging.info("Running experiment it: - %i" % iteration)

        start_time = time.time()
        main(stop_time=simulationDuration,
             it=iteration)

        print("\n--- %s seconds ---" % (time.time() - start_time))
        
    print("Simulation Done!")
    