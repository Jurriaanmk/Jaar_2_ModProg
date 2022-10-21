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
    for i, robot in enumerate(robot_list):
        print(f'Robot Locatie {i} = ', robot.get_location())
    return

#%% g
def get_pose():
    """get_pose(robot_list) geeft een lijst met de positie van de
robots in robot_list"""
    pose_list = []
    for robot in robot_list:
        pose_list.append(robot.get_xdir())
    for i, robot in enumerate(robot_list):
        print(f'Robot pose_list {i} = ', robot.get_pose())
        
    return 

def get_x():
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_list = []
    for robots in robot_list:
        x_list.append(robots.get_x())
    for i, robot in enumerate(robot_list):
        print(f'Robot X {i} = ', robot.get_x())
    return 

def get_y():
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    y_list = []
    for robot in robot_list:
        y_list.append(robot.get_y())
    for i, robot in enumerate(robot_list):
        print(f'Robot Y {i} = ', robot.get_y())
        
    return 

def get_x_dir():
    """get_x(robot_list) geeft een lijst met de x-coordinaat van de
robots in robot_list"""
    x_dir_list = []
    for robot in robot_list:
        x_dir_list.append(robot.get_xdir())
    for i, robot in enumerate(robot_list):
        print(f'Robot x_dir {i} = ', robot.get_xdir())
        
    return 

def get_y_dir():
    """get_x(robot_list) geeft een lijst met de y-coordinaat van de
robots in robot_list"""
    y_dir_list = []
    for robot in robot_list:
        y_dir_list.append(robot.get_ydir())
    for i, robot in enumerate(robot_list):
        print(f'Robot y_dir {i} = ', robot.get_ydir())
        
    return 
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


 