#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:49:15 2020

@author: amts
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, date_range
from matplotlib.ticker import FormatStrFormatter

from yafs.stats import Stats


# for size in [100,1000,10000,100000,1000000]:


s_trace = 'sim_trace.csv'
s_t_link = 'sim_trace_link.csv'

df = pd.read_csv(s_trace)
df_link = pd.read_csv(s_t_link)



"""
dtmp = df[df["module.src"]=="None"].groupby(['app','TOPO.src'])['id'].apply(list)

for g in dtmp.keys():
    print(g)
"""  
        
m = Stats(defaultPath="sim_trace")


m.compute_times_df()
    
# print ("\tNetwork bytes transmitted:")
# print (f"\t\t{m.bytes_transmitted():.1f}")

# m.df_link.head(15) # from Stats class
time_loops = [["M.USER.APP.0", "M.USER.APP.1", "M.USER.APP.2",
               "M.USER.APP.3"]]



m.showResults2(10000, time_loops=None)

print(f'total messages = {m.count_messages()}')

# Latency from m.compute_times()
# print(m.df['time_latency'])


x = m.df['id']
y = m.df['time_latency']


# Latency behaviour along simulation
fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='event simulation', ylabel='time_latency',
       title='Latency along simulation')

fig.savefig("test.png")
plt.show()


print ("\t- Network saturation -")
print()

print ("\t\tAverage waiting messages : "
       f"{m.average_messages_not_transmitted()}")
print()

print ("\t\tPeak of waiting messages :"
       f"{m.peak_messages_not_transmitted()}")
print()

print(f"\t\tShow Loops: {m.showLoops(time_loops)}")

print()
print (f"\t\tTOTAL messages not transmitted:" 
       f" {m.messages_not_transmitted()}")
print()

# print(m.get_df_modules())

