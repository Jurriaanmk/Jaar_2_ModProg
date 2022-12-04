#%%
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:27:21 2022

@author: Jurriaan Katsman, made by Rufus Fraanje
"""

from distutils.file_util import move_file
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
Bots = 10

for x in range(10):
    for y in range(10):
        pose = [x,y,0]
        robot = Robot(pose)
        robot_list.append(robot)
# for i, robot in enumerate(robot_list):
#     print(f'Robot Locatie {i} = ', robot.get_location())

#%% f
def Move_all(Afstand, Richting):
    for item in robot_list:
        robot = robot_list[item]
        Robot.move(Afstand, Richting)
       
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot Locatie {i} = ', robot.get_location())
    return

#%% g
def get_pose():
    """get_pose(robot_list) geeft een lijst met de positie van de
robots in robot_list"""
    pose_list = []
    for robot in robot_list:
        pose_list.append(Robot.get_xdir(robot))
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot pose_list {i} = ', robot.get_pose())
        
    return pose_list

def get_x(robot_list):
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_list = []
    for robot in robot_list:
        x_list.append(Robot.get_x(robot))
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot X {i} = ', robot.get_x())
    return x_list

def get_y(robot_list):
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    y_list = []
    for robot in robot_list:
        y_list.append(Robot.get_y(robot))
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot Y {i} = ', robot.get_y())
        
    return y_list

def get_x_dir(robot_list):
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_dir_list = []
    for robot in robot_list:
        x_dir_list.append(Robot.get_xdir(robot))
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot x_dir {i} = ', robot.get_xdir())
        
    return x_dir_list

def get_y_dir(robot_list):
    """get_x(robot_list) geeft een lijst met de y-coordinaat van de
robots in robot_list"""
    y_dir_list = []
    for robot in robot_list:
        y_dir_list.append(Robot.get_ydir(robot))
    # for i, robot in enumerate(robot_list):
    #     print(f'Robot y_dir {i} = ', robot.get_ydir())
        
    return y_dir_list
#%% h
def move_for_time(tijds_invoer):
    for i in range(tijds_invoer):
        sleep(1)
        Move_all(i,i*pi)
        
        for i, robot in enumerate(robot_list):
            print(f'Robot pose_list {i} = ', robot.get_pose())
    return
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
from time import sleep
from robot import Robot
from math import pi
import math as mt
import matplotlib.pyplot as plt
import numpy as np

while(1):
    num = 10
    for i in range(num):
        Robot.move(robot_list, 0.5, (pi/10))

        
        ax = plt.subplot()

        x = get_x(robot_list)
        y = get_y(robot_list)
        xdir = get_x_dir(robot_list)
        ydir = get_y_dir(robot_list)
        q = ax.quiver(x,y,xdir,ydir)  # maak de vector plot voor alle robots in de lijst
        ax.quiverkey(q, X=0.1, Y=1.1, U=0.7, label='Robot position', labelpos='E')

        plt.xlim([-5, 12.5])
        plt.ylim([-5, 16])
        plt.grid()
        
        avgX = round(np.mean(get_x(robot_list)))
        avgY = round(np.mean(get_y(robot_list)))

        text = 'Average: (' + str(avgX) + ', ' + str(avgY) + ')'
        
        ax.text( 0, 15, text, verticalalignment = 'top')
        plt.pause(0.025)
        plt.clf()
    
    

# %%

 