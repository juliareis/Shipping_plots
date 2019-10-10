#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:08:14 2019

@author: juliareis
"""
### Plot Optimized RPM v Environmental Variables

# load data
cd Results
opt_RL = pd.read_csv('Opt_RPM_RL_Oct2.csv', header = None)

# Simulate environmental variables at each waypoint, based on:
# optimized RPM, start time (bg) and waypoint location (wp_bg)
(env) = f_run(opt_RL, bg, wp_bg) 
env_RL = env

# Plot Settings
plt.rcParams.update({'font.size': 16})
plt.style.use('seaborn-ticks')

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85, bottom = 0.2)
ax.set_xlabel('Current') 
ax.set_ylabel('RPM')
ax.plot(env_RL[:,0],opt_RL,'b.')
plt.savefig('RPM_v_Current_RL.jpg')

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85, bottom = 0.2)
ax.set_xlabel('Wind Speed') 
ax.set_ylabel('RPM')
ax.plot(env_RL[:,1],opt_RL,'b.')
plt.savefig('RPM_v_Wind_RL.jpg')

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85, bottom = 0.2)
ax.set_xlabel('Wave Height') 
ax.set_ylabel('RPM')
ax.plot(env_RL[:,2],opt_RL,'b.')
plt.savefig('RPM_v_WaveHeight_RL.jpg')
