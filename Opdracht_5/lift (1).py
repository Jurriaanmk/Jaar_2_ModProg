#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:39:22 2020

@author: rufus
"""

from time import sleep  # sleep functie is nodig om te kunnen wachten

class Lift():
    """Class voor Lift type objecten, waarmee gedrag van een lift gesimuleerd kan worden."""
    
    def __init__(self, verdieping_min, verdieping_max, tijd_deur, tijd_verdieping):
        if verdieping_min > 0:
            raise RuntimeError('verdieping_min moet 0 of kleiner zijn.')
        self.verdieping_min  = verdieping_min
        self.verdieping_max  = verdieping_max
        self.tijd_deur       = tijd_deur
        self.tijd_verdieping = tijd_verdieping
        self.positie         = 0     # starten altijd op verdieping 0
        self.deur_open       = False  # false is dicht, true is open

    def __str__(self):
        return f"Lift object, huidige positie is {self.positie}, deur_open = {self.deur_open}."

    def printPositie(self):
        print("Huidige positie: ",self.positie)

    def printDeur(self):
        if self.deur_open:
            print("Deur is open")
        else:
            print("Deur is dicht")

    def openDeur(self):
        if not self.deur_open: # deur is dicht
            sleep(self.tijd_deur) # tijd nodig om deur dicht te doen
            self.deur_open = True
        self.printDeur()
    
    def sluitDeur(self):
        if self.deur_open:  # deur is open
            sleep(self.tijd_deur) # tijd nodig om deur open te doen
            self.deur_open = False
        self.printDeur()
        
    def gaNaar(self,verdieping):
        if (verdieping<self.verdieping_min) | (verdieping>self.verdieping_max):
            raise RuntimeError("verdieping valt buiten toegestane grens.")
            
        if self.positie == verdieping:
            self.printPositie()
            self.openDeur()
        else:
            self.sluitDeur()
            if self.positie < verdieping: # omhoog
                for stap in range(self.positie,verdieping):
                    sleep(self.tijd_verdieping) # tijd nodig voor 1 omhoog
                    self.positie += 1
                    self.printPositie()
            else: # omlaag
                for stap in range(self.positie,verdieping,-1):
                    sleep(self.tijd_verdieping) # tijd nodig voor 1 omlaag
                    self.positie -= 1
                    self.printPositie()
            self.openDeur()

            
