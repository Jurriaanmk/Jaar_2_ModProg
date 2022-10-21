#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:27:21 2022

@author: Jurriaan Katsman, made by Rufus Fraanje
"""

from math import sqrt, pi
from time import sleep
from robot import Robot
from time import sleep

#%% a
robot1 = Robot([2.0, 1.0, 5.0])
robot2 = Robot([4.0, 5.1, 9.2])



#%% b en c
# zie robot.py


#%% d


#%% e
robot_list = []
#def initRobots_list(Bots):
Bots = 4

for x in range(Bots):
    for y in range(Bots):
        pose = [x,y,0.0]
        robot = Robot(pose)
        robot_list.append(robot)
for i, robot in enumerate(robot_list):
    print(f'Robot Locatie {i} = ', robot.get_location())

#%% f
def Move_all(Afstand, Richting):
    for item in range(len(robot_list)):
        robot = robot_list[item]
        robot.move(Afstand, Richting)
        robot = Robot(pose)
        return

#%% g

def get_x():
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_list = []
    for robots in robot_list:
        x_list.append(robots.get_x())
    print("X_list",x_list)   
    return x_list

def get_y():
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    y_list = []
    for robot in robot_list:
        y_list.append(robot.get_y())
        print("Y_list",y_list)
        
    return y_list

def get_x_dir(robot_list):
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_dir_list = []
    for robot in robot_list:
        x_dir_list.append(robot.get_xdir())
        print("x_dir_list",x_dir_list)
        
    return x_dir_list
#%% h
#def move_for_time(robot_list, tijds_invoer):
 #   for tijds_invoer:
        
    
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


 