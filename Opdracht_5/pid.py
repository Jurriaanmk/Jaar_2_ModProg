#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:11:00 2020

@author: rufus
"""

class PID:
    """PID controller class."""
    def __init__(self,Kp,Ki,Kd,h,ep=0,eip=0):
        """Kp,Ki,Kd: proportional, integral and derivative gain
           h: sampling time
           ep: previous error signal e(k-1)
           eip: previous integral error signal e_int(k-1)
        """
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.h = h
        self.ep = ep
        self.eip = eip
        
    def __str__(self):
        """Returns the string printed by print(controller)."""
        return f"PID controller object with:\n\tKp={self.Kp}, Ki={self.Ki}, Kd={self.Kd}, h={self.h}, ep={self.ep}, eip={self.eip}."
    
    def run(self,e):
        """Computes control signal u and updates past error and integral."""
        self.eip += self.h * e  # update integral
        derivative = (e - self.ep) / self.h
        u = self.Kp * e + self.Ki * self.eip + self.Kd * derivative
        self.ep = e # update previous error, for next run
        return u


C_pid = PID(10,2,0.1,0.01)
C_pi  = PID(10,2,0,0.01)

print(C_pid)

