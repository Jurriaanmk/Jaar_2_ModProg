#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:27:21 2022

@author: rufus
"""

from math import sqrt, pi
from time import sleep
from robot import Robot

#%% a
robot1 = Robot([2.0, 1.0, 5.0])
robot2 = Robot([4.0, 5.1, 9.2])



#%% b en c
# zie robot.py


#%% d


#%% e
number_of_robots = 100
robot_list = []
for i in range(number_of_robots):
    pose_i = ... # determine initial pose of i-th robot
    robot_i = Robot(pose_i) # create i-th robot object
    robot_list.append(robot_i) # add i-th robot to the list
    
robot_list = []
for i in range(10):
    for j in range (10):
        pose = [i, j, 0.]
        robot_object = Robot(pose)
        robot_list.append(robot_object)
#%% f


#%% g


#%% h
    
    
#%% i
# voorbeeld code is geplaatst in comments
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots() # maak figuur met een as axis object
#plt.show()               # toon de figuur op het scherm

#num = 10
#for i in range(num):
#    ax.cla()                  # wis het assenstelsel zodat evt vorige visualisatie verdwijnt
#   ... beweeg robot en vraag de lijsten met x, y positie and xdir, ydir richting op
#    ax.quiver(x,y,xdir,ydir)  # maak de vector plot voor alle robots in de lijst 
#    ax.axis([-20,20,-20,20])  # zet grootte van het assenstelsel vast, zodat beeld niet verspringt
#    fig.canvas.draw()         # geef commando om beeld te tekenen (plt.draw() mag ook)
#    plt.pause(0.5)            # nodig voor matplotlib, sleep alleen blijkt niet voldoende
#    sleep(0.5)                # wacht even, zodat je het beeld beter kunt zien

#%% j


 