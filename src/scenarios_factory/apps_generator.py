#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:52:37 2021

@author: amts
"""
import networkx as nx
import random
import json

#APP and SERVICES
TOTALNUMBEROFAPPS = 2
func_APPGENERATION = "nx.gn_graph(2)" # original nx.gn_graph(random.randint(1,2)) algorithm for the generation of the random applications
func_SERVICEINSTR = "random.randint(30,30)" #INSTR --> teniedno en cuenta nodespped esto nos da entre 200 y 600 MS
func_SERVICEMESSAGESIZE = "random.randint(20,20)" #BYTES y teniendo en cuenta net bandwidth nos da entre 20 y 60 MS

func_SERVICERESOURCES = "random.randint(1,1)" #MB de ram que consume el servicio, teniendo en cuenta noderesources y appgeneration tenemos que nos caben aprox 1 app por nodo o unos 10 servicios

func_APPDEADLINE="random.randint(1,1)" #MS

#myDeadlines = [487203.22, 487203.22,487203.22,474.51,302.05,831.04,793.26,1582.21,2214.64,374046.40,420476.14,2464.69,97999.14,2159.73,915.16,1659.97,1059.97,322898.56,1817.51,406034.73]

#pathGML ="topology/test_GLP.gml"


def appGeneration():
    
    #****************************************************************************************************
    #application generation
    #****************************************************************************************************
    
    numberOfServices=0
    apps = list()
    appsDeadlines = {}
    appsResources = list()
    appsSourceService = list()
    appsSourceMessage = list()
    appsTotalMIPS = list()
    mapService2App = list()
    mapServiceId2ServiceName = list()
    
    appJson = list()
    servicesResources = {}
    
    
    for i in range(TOTALNUMBEROFAPPS):
        print(f"CREANDDO APP :{i} ")
        
        myApp = {}
        APP = eval(func_APPGENERATION)
    
        mylabels = {}
    
        for n in range(0,len(APP.nodes)):
            mylabels[n]=str(n)
    
        edgeList_=list()
    
        for m in APP.edges:
            edgeList_.append(m)
        for m in edgeList_:
            APP.remove_edge(m[0],m[1])
            APP.add_edge(m[1],m[0])
    
    
    
        mapping=dict(zip(APP.nodes(),range(numberOfServices,numberOfServices+len(APP.nodes))))
        APP=nx.relabel_nodes(APP,mapping)
    
        numberOfServices = numberOfServices + len(APP.nodes)
        apps.append(APP)
        for j in APP.nodes:
            servicesResources[j]=eval(func_SERVICERESOURCES)
        appsResources.append(servicesResources)
    
        topologicorder_ = list(nx.topological_sort(APP))
        source = topologicorder_[0]

    
        appsSourceService.append(source)
    
        
        appsDeadlines[i]=eval(func_APPDEADLINE)
        #appsDeadlines[i] = myDeadlines[i]
        myApp['id']=i
        myApp['name']=str(i)
        myApp['HwReqs']=appsDeadlines[i]
        myApp['MaxReqs']= 200
        myApp['MaxLatency'] = 50
        
    
        myApp['module']=list()
    
        edgeNumber=0
        myApp['message']=list()
    
        myApp['transmission']=list()
    
        totalMIPS = 0
    
        for n in APP.nodes:
            mapService2App.append(str(i))
            mapServiceId2ServiceName.append(str(i)+'_'+str(n))
            myNode={}
            myNode['id']=n
            myNode['name']=str(i)+'_'+str(n)
            myNode['RAM']=servicesResources[n]
            myNode['type']='MODULE'
            if source==n:
                myEdge={}
                myEdge['id']=edgeNumber
                edgeNumber = edgeNumber +1
                myEdge['name']="M.USER.APP."+str(i)
                myEdge['s']= "None"
                myEdge['d']=str(i)+'_'+str(n)
                myEdge['instructions']=eval(func_SERVICEINSTR)
                totalMIPS = totalMIPS + myEdge['instructions']
                myEdge['bytes']=eval(func_SERVICEMESSAGESIZE)
                myApp['message'].append(myEdge)
                appsSourceMessage.append(myEdge)
                
                for o in APP.edges:
                    if o[0]==source:
                        myTransmission = {}
                        myTransmission['module']=str(i)+'_'+str(source)
                        myTransmission['message_in']="M.USER.APP."+str(i)
                        myTransmission['message_out']=str(i)+'_('+str(o[0])+"-"+str(o[1])+")"
                        myApp['transmission'].append(myTransmission)

            myApp['module'].append(myNode)
    
    
        for n in APP.edges:
            myEdge={}
            myEdge['id']=edgeNumber
            edgeNumber = edgeNumber +1
            myEdge['name']=str(i)+'_('+str(n[0])+"-"+str(n[1])+")"
            myEdge['s']=str(i)+'_'+str(n[0])
            myEdge['d']=str(i)+'_'+str(n[1])
            myEdge['instructions']=eval(func_SERVICEINSTR)
            totalMIPS = totalMIPS + myEdge['instructions']
            myEdge['bytes']=eval(func_SERVICEMESSAGESIZE)
            myApp['message'].append(myEdge)
            destNode = n[1]
            for o in APP.edges:
                if o[0]==destNode:
                    myTransmission = {}
                    myTransmission['module']=str(i)+'_'+str(n[1])
                    myTransmission['message_in']=str(i)+'_('+str(n[0])+"-"+str(n[1])+")"
                    myTransmission['message_out']=str(i)+'_('+str(o[0])+"-"+str(o[1])+")"
                    myApp['transmission'].append(myTransmission)
    
    
        for n in APP.nodes:
            outgoingEdges = False
            for m in APP.edges:
                if m[0]==n:
                    outgoingEdges = True
                    break
            if not outgoingEdges:
                for m in APP.edges:
                    if m[1]==n:
                        myTransmission = {}
                        myTransmission['module']=str(i)+'_'+str(n)
                        myTransmission['message_in']=str(i)+'_('+str(m[0])+"-"+str(m[1])+")"
                        myApp['transmission'].append(myTransmission)
    
    
        appsTotalMIPS.append(totalMIPS)
    
        appJson.append(myApp)
    return appJson


if __name__ == '__main__':
    
    appJson = appGeneration()
    with open("appDefinition.json","w") as f:
        f.write(json.dumps(appJson))
