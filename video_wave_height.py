#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 13:45:30 2019

@author: juliareis
"""
# code based on link:
# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

wave_height = pd.read_csv((path + "waveHeight.csv"),header=None) 

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 201), ylim=(0, 8))
line, = ax.plot([], [], lw=3)

ax.set_title('Wave Height', fontsize=15)
ax.set_xlabel('Waypoint Segments', fontsize=15)


def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(1, 201, 201)
    y = wave_height.iloc[:,i]
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('wave_height.gif', writer='imagemagick') 


### Wind

fig = plt.figure()
ax = plt.axes(xlim=(0, 201), ylim=(0, 20))
line, = ax.plot([], [], lw=3)

ax.set_title('Wind Speed', fontsize=15)
ax.set_xlabel('Waypoint Segments', fontsize=15)


def init():
    line.set_data([], [])
    return line,
def animate(i):
    #x = np.linspace(0, 4, 1000)
    x = np.linspace(1, 201, 201)
    #y = np.sin(2 * np.pi * (x - 0.01 * i))
    y = speed_wind.iloc[:,i]
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('wind_speed.gif', writer='imagemagick') 