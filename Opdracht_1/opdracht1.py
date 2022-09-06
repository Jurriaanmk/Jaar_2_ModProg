
#%%
#Opgave 1A, tijds omzetting 
#def Tijdsomzetting():
#voer de tijd in bij uren, minuten en seconden.
from cmath import pi
import math
from multiprocessing import reduction
from tokenize import triple_quoted
from xml.etree.ElementInclude import include


Tijd_Invoer_Uren = 74
Tijd_Invoer_Minuten = 23
Tijd_Invoer_Seconden = 12

Tijd_Totaal_Seconden = Tijd_Invoer_Uren*3600 + Tijd_Invoer_Minuten*60 + Tijd_Invoer_Seconden

Tijd_Uitvoer = Tijd_Totaal_Seconden
print (Tijd_Uitvoer)


#    if __name__ == "__Tijdsomzetting__":
#        Tijdsomzetting()

##%%
# Opgave 1A verbeterd
def tijd_Omzetting(Uren,Minuten,Seconden):
    return (Uren*3600) + (Minuten*60) + Seconden

# #%%
#Opgave 1B
def tijd_Omzetting_Inverse(Invoer_Seconden):
    Minuten, Seconden = divmod( Invoer_Seconden, 60)
    Uren, Minuten = divmod(Minuten, 60)

    return (Uren, Minuten, Seconden)

## %%
#Opgave 1C
#Testen uitgevoerd, werken naar behoren.

##%%
#Opgave 2A
pi = 3.14
def rad2degrees (x):
    x= (x/(2*pi))*360
    return(x)

def deg2rad (x):
    x = (x/360)*(2*pi)
    return (x)

## %%
#Opgave 2B
#Toerental naar Hz

def RPM2Hz (x):
    """"Rekent van RPM naar Hz"""
    x= 1/(x/60)
    return(x)

def Hz2RPM (x):
    """"Rekent van Hz naar RPM"""
    x=1/x*60
    return (x)
## %%
#Opgave 3, 
import operator as op
def FalseOrTrue (x,y):
    z= op.and_(x,y)
    return(z)


def print_waarheidstabel_And():
    print('False, False: ', op.and_(False,False))
    print('False, True: ', op.and_(False,True))
    print('True, False: ', op.and_(True,False))
    print('True, True: ', op.and_(True,True))

## %%
#opgave 3B

def print_waarheidstabel_Or():
    print('False, False: ', op.or_(False,False))
    print('False, True: ', op.or_(False,True))
    print('True, False: ', op.or_(True,False))
    print('True, True: ', op.or_(True,True))
    return()

def print_waarheidstabel_Xor():
    print('False, False: ', op.xor(False,False))
    print('False, True: ', op.xor(False,True))
    print('True, False: ', op.xor(True,False))
    print('True, True: ', op.xor(True,True))
    return()

def print_waarheidstabel(operator):
    print('False, False: ', operator(False,False))
    print('False, True: ', operator(False,True))
    print('True, False: ', operator(True,False))
    print('True, True: ', operator(True,True))
    return()

print_waarheidstabel(op.xor)
##%%
def return_waarheidstabel(operator):
    ff = [False, False, operator(False,False)]
    ft = [False, True, operator(False,True)]
    tf = [True, False, operator(True,False)]
    tt = [True, True, operator(True,True)]
    return [ff, ft, tf, tt]

print(return_waarheidstabel(op.xor))