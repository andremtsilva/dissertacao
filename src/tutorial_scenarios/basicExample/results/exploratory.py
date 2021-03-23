#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:49:15 2020

@author: amts
"""

import pandas as pd
# import os

# os.getcwd()

s_trace = 'sim_trace.csv'
s_t_link = 'sim_trace_link.csv'

df_s_trace = pd.read_csv(s_trace)
df_s_t_link = pd.read_csv(s_t_link)



"""
dtmp = df[df["module.src"]=="None"].groupby(['app','TOPO.src'])['id'].apply(list)

for g in dtmp.keys():
    print(g)
"""  
        
