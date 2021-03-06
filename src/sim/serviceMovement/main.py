"""
In this simulation, the modules/services of the apps changes the allocation on
the nodes randomly each time.

@author: Isaac Lera
"""
import os
import random
import time
import json
import logging.config
import networkx as nx

from pathlib import Path
from collections import defaultdict

from yafs.topology import Topology
from yafs.application import create_applications_from_json
from yafs.placement import JSONPlacement
from yafs.path_routing import DeviceSpeedAwareRouting
from yafs.core import Sim
from yafs.distribution import deterministic_distribution, \
    deterministicDistributionStartPoint


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
        
        # We move all the service to other random node.
        for service in current_services:
            for currentNode in current_services[service]:
                newNode = random.sample(sim.topology.G.nodes(),1)[0]
                if not self.is_already_deployed(sim, service, newNode):
                    self.undeploy_module(sim, service, currentNode)
                    self.deploy_module(sim, service, newNode)
                    logging.info(f"Moving Service {service} from "
                                 f"{currentNode} to {newNode} node")
        

def main(stop_time, it):
    
    folder_results = Path("results/")
    folder_results.mkdir(parents=True, exist_ok=True)
    folder_results = str(folder_results)+"/"
    
    """
    TOPOLOGY
    """
    t = Topology()
    
    # see examples folder to create topology from Json file
    size = 5
    t.G = nx.generators.binomial_tree(size) # see networkx for more generators
    
    # Definition of mandatory attributes of a Topology
    
    # Attr. on Edges
    # PR and BW are 1 unit
    attPR_BW = {x: 1 for x in t.G.edges()}
    nx.set_edge_attributes(t.G, name="PR", values=attPR_BW)
    nx.set_edge_attributes(t.G, name="BW", values=attPR_BW)
    
    #Attr. on Nodes
    # IPT
    attIPT = {x: 100 for x in t.G.nodes()}
    nx.set_node_attributes(t.G, name="IPT", values=attIPT)
    
    nx.write_graphml(t.G, folder_results+f"graph_binomial_tree_{size}")
    
    print(t.G.nodes()) # nodes id can be str or int
    
    """
    APPLICATION or SERVICES
    """    
    dataApp = json.load(open('data/appDefinition.json'))
    apps = create_applications_from_json(dataApp)
    
    """
    SERVICE PLACEMENT
    """
    placementJson = json.load(open('data/allocDefinition.json'))
    placement = JSONPlacement(name="Placement", json=placementJson)
    
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
    Deploy services == App's modules
    """
    for aName in apps.keys():
        s.deploy_app(apps[aName], placement, selectorPath)

    """
    Deploy users
    """    
    userJSON = json.load(open('data/usersDefinition.json'))
    for user in userJSON["sources"]:
        app_name = user["app"]
        app = s.apps[app_name]
        msg = app.get_message(user["message"])
        node = user["id_resource"]
        dist = deterministic_distribution(100, name="Deterministic")
        idDES = s.deploy_source(app_name, id_node=node, msg=msg,\
                                distribution=dist)

    """
    This internal monitor in the simulator (a DES process) changes the sim's
    behaviour. You can have multiples monitors doing different or same tasks.
    
    In this case, it changes the service's allocation, the node where the
    service is.
    """    
    dist = deterministicDistributionStartPoint(stop_time/4.0,
                                               stop_time/2.0/10.0,
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
    simulationDuration = 20000
    
    # Iteration for each experiment changing the seed of randoms
    for iteration in range(nIterations):
        random.seed(iteration)
        logging.info(f"Running experiment it: - {iteration}")
        
        start_time = time.time()
        main(stop_time=simulationDuration, it=iteration)
        
        print(f"\n----{time.time() - start_time} seconds ----")

    print("Simulation Done!")        
        
    