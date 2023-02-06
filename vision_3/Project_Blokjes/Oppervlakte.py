#%%
import cv2
import numpy as np
from typing import Tuple

oppervlakte_Print = 1


Kleuren_Bieb = {  # Bieb voor alle kleuren van de blokjes plus het aantal keer dat ze voorkomen
    "rood": {
        "Waardes": (np.array([163, 155, 181]), np.array([179, 213, 223])),
        "Oppervlakte": 26230,
        "Voorgekomen": 0
    },
    "wit": {
        "Waardes": (np.array([85, 9, 223]), np.array([121, 62, 255])),
        "Oppervlakte": 13145,
        "Voorgekomen": 0
    },
    "blauw": {
        "Waardes": (np.array([90, 111, 196]), np.array([113, 233, 232])),
        "Oppervlakte": 11439,
        "Voorgekomen": 0
    },
    "paars": {
        "Waardes": (np.array([122, 121, 169]), np.array([130, 173, 204])),
        "Oppervlakte": 24737,
        "Voorgekomen": 0
    },
    "oranje": {
        "Waardes": (np.array([0, 121, 157]), np.array([7, 159, 231])),
        "Oppervlakte": 49865,
        "Voorgekomen": 0
    },
    "groen": {
        "Waardes": (np.array([70, 190, 84]), np.array([97, 255, 255])),
        "Oppervlakte": 47559,
        "Voorgekomen": 0
    },
    "geel": {
        "Waardes": (np.array([22, 241, 201]), np.array([30, 255, 225])),
        "Oppervlakte": 23826,
        "Voorgekomen": 0
    },
}

def Verkrijg_Kleur_Randwaardes(kleur: str) -> Tuple[np.ndarray, np.ndarray]:
    """Functie om alle kleuren in de bieb te ophalen"""
    return Kleuren_Bieb[kleur]["Waardes"]

def Verkrijg_Kleur_Randwaardes(kleur: str) -> Tuple[np.ndarray, np.ndarray]:
    """Functie om alle kleuren in de bieb te ophalen"""
    return Kleuren_Bieb[kleur]["Waardes"]

def Afbeelding_Inladen(Afbeelding):
    Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)
    Afbeelding2 = Afbeelding.copy()
    Afbeelding2_HSV = cv2.cvtColor(Afbeelding2, cv2.COLOR_BGR2HSV)

    return Afbeelding, Afbeelding_HSV, Afbeelding2, Afbeelding2_HSV


def Kleuren_Herkennen(Kleur):
    Lower_Kleuren, Higher_Kleuren = Verkrijg_Kleur_Randwaardes(Kleur)  # Haal de eigenschappen van de kleuren op en stop ze in de juiste waarde

    # Maak een filter masker waar enkel de geselecteerde kleur in te zien is.
    Basis_Mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren)
    Basis_Res = cv2.bitwise_and(Afbeelding, Afbeelding, mask=Basis_Mask)
    Basis_contours, _ = cv2.findContours(Basis_Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(Basis_contours) != 0:  # Maak een blauwe contour om alle gevonden contouren
        cv2.drawContours(Afbeelding, Basis_contours, -1, (255, 0, 0), 3)

        # Vind de grootste contour in alle gevonden contouren
        Max_Grootte = max(Basis_contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(Max_Grootte)

        # Teken een vierkant rond het grootste contour in Groen
        cv2.rectangle(Afbeelding, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Zoek de contouren in alle contouren
        areas = [cv2.contourArea(Max_Grootte)for Max_Grootte in Basis_contours]
        # Selecteerd de grootste contour uit alle contouren
        Grootst_Oppervlakte = max(areas)
        Max_Index = np.argmax(areas)
        
        Vierkant = cv2.minAreaRect(Max_Grootte)
        
        if oppervlakte_Print:
            print('Oppervlakte = ', Grootst_Oppervlakte)
        
    return Basis_Mask

# %%
Video = cv2.VideoCapture(0)


Wachttijd_Tussen_Frame = 500   #Instelbare wachttijd tussen het maken van een nieuw frame, op moment in ms

while (True):
    _, huidig_Frame = Video.read()
    cv2.imshow('Live Video', huidig_Frame)

    #Druk op de spatiebalk om een frame te nemen
    if cv2.waitKey(Wachttijd_Tussen_Frame) & 0xFF == 32:
        
        #Optionele while loop, loopt het max aantal lussen door door met een wachttijd om zeker te zijn van object detectie.
            #x x_, huidig_Frame = Video.read()
            cv2.imshow('Live Video', huidig_Frame)
            Afbeelding, Afbeelding_HSV, Afbeelding2, Afbeelding2_HSV = Afbeelding_Inladen(huidig_Frame)
            
            for Kleuren_Keys in Kleuren_Bieb.keys():
                Basis_Masker = Kleuren_Herkennen(Kleuren_Keys)
                cv2.imshow(f'Mask_Kleur{Kleuren_Keys}', Basis_Masker)

            #De Q/q toets zorgt dat de while loop verlaten wordt en weer de live feed weergeven wordt.
    if cv2.waitKey(Wachttijd_Tussen_Frame) & 0xFF == ord('q'):
        cv2.destroyAllWindows()



    #De X toets sluit de video af
    if cv2.waitKey(Wachttijd_Tussen_Frame) & 0xFF == ord('x'):

        Video.release()
        cv2.destroyAllWindows()
        break

# %%
