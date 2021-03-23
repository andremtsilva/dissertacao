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
        


# m.df_link.head(15) # from Stats class
time_loops = [["M.USER.APP.0", "M.USER.APP.1", "M.USER.APP.2",
               "M.USER.APP.3", "M.USER.APP.4", "M.USER.APP.5", 
               "M.USER.APP.6", "M.USER.APP.7", "M.USER.APP.8",
               "M.USER.APP.9"]]





### Finally, you can analyse the results:
print ("-"*20)
print ("Results:")
print ("-" * 20)

m = Stats(defaultPath="sim_trace") #Same name of the results
m.compute_times_df()
m.showResults2(1000, time_loops=time_loops)
print ("\t- Network saturation -")
print (f"\t\tAverage waiting messages : {m.average_messages_not_transmitted()}")
print (f"\t\tPeak of waiting messages : {m.peak_messages_not_transmitted()}")
print (f"\t\tTOTAL messages not transmitted: {m.messages_not_transmitted()}") 

print ("\n\t- Stats of each service deployed -")
print (m.get_df_modules())
print (m.get_df_service_utilization("2_8",1000))
print (m.get_df_service_utilization("6_29",1000))


print ("\n\t- Stats of each DEVICE -")
  #TODO
print(f'total messages = {m.count_messages()}')
# Latency from m.compute_times()
# print(m.df['time_latency'])

TODO
# group id simulation specific rows (df)
# latency metrics
# hop count from analize_results MCDA work

"""
x = m.df['id']
y = m.df['time_latency']


# Latency behaviour along simulation
fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='event simulation', ylabel='time_latency',
       title='Latency along simulation')

#fig.savefig("test.png")
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
"""