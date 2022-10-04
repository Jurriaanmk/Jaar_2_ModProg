#%% method
class Time():
    def __init__(self, uren, minuten, seconden):
        self.uren = uren
        self.minuten = minuten
        self.seconden = seconden 
        
    def time_to_int_method(self):
        return (self.uren*60+self.minuten)*60+self.seconden
        
def time_to_int(Time):
    return (Time.uren*60+Time.minuten)*60+Time.seconden

t = Time(12, 25, 00)

#%%
class Vector():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        
x = Vector(1,0,0)

#%%
from calendar import c
import numpy as np
x = np.array([1,0,0])
y = np.array([0,1,0])

a = 2*x +3*y

x_c = x.reshape((len(x),1))
y_c = y.reshape((len(y),1))
a_c = a.reshape((len(a),1))

x_r =x_c.T
y_r = y_c.T
a_r = a_c.T

A = np.array([
    [1.,1,0],
    [2.,-1,0],
    [0,0,1]
])

#%%

import numpy as np
import matplotlib.pyplot as plt

def fun(a,b,c,x):
    return a*x**2 + b*x + c

u = np.linspace(0,10,100)
a = 3
b = 6
c = 14
y = fun(a,b,c,u)

#%%