# %%
# Code om de contouren te herkenen op basis van kleur. Geen vorm herkening.
# Om te gebruiken, voer afbeelding in bij Afbeelding, draai programma, type in console Kleuren_Herkenen("Kleur"). Type in Kleur de kleur uit de bibiloteek die je wilt.
# Dit print het aantal x voorgekomen en middenpunt van deze kleur.
import cv2
import numpy as np
from typing import Tuple

Middenpunt_Print = 0
"""1 = aan, 0 = uit. Print in de console de middenpunt waarde, kan gebruikt worden voor het exporteren van de middenpunten van de blokjes"""

Oppervlakte_Marge = 0.2
"""Een marge factor om te kijken of een oppervlakte in het bereik van de bieb versie ligt"""
oppervlakte_Print = 1

#Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
#Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)
#Afbeelding2 = Afbeelding.copy()
#Afbeelding2_HSV = cv2.cvtColor(Afbeelding2, cv2.COLOR_BGR2HSV)

def Afbeelding_Inladen(Afbeelding):
    Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)
    Afbeelding2 = Afbeelding.copy()
    Afbeelding2_HSV = cv2.cvtColor(Afbeelding2, cv2.COLOR_BGR2HSV)

    return Afbeelding, Afbeelding_HSV, Afbeelding2, Afbeelding2_HSV

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


def Verkrijg_Aantal_Keer_Kleur_Voorgekomen(kleur: str) -> int:
    """Functie om aantal keer dat een kleur voorgekomen is op te vragen"""
    return Kleuren_Bieb[kleur]["Voorgekomen"]


def Verkrijg_Kleur_Randwaardes(kleur: str) -> Tuple[np.ndarray, np.ndarray]:
    """Functie om alle kleuren in de bieb te ophalen"""
    return Kleuren_Bieb[kleur]["Waardes"]


def Verkrijg_Kleur_Oppervlakte(kleur: str) -> int:
    """Functie om de ingestelde oppervalkte van een kleur te ophalen"""
    return Kleuren_Bieb[kleur]["Oppervlakte"]


def Middenpunt_Bepalen(Contour, index: int) -> Tuple[int, int]:
    """Functie om te bepalen wat de middenpunten van alle objecten zijn en hier een stipje te zetten en de coordinaten te exporteren"""
    moments = cv2.moments(Contour[index])
    #Check of er een middenpunt berekend kan worden
    if moments['m00'] == 0:
        return 0,0

    Middenpunt_x = int(moments['m10'] / moments['m00'] + 1e-5)
    Middenpunt_y = int(moments['m01'] / moments['m00'] + 1e-5)
    cv2.circle(Afbeelding, (Middenpunt_x, Middenpunt_y), 5, (0, 0, 0), -1)

    if Middenpunt_Print:
        print("Middenpunt: (", Middenpunt_x, ", ", Middenpunt_y, ")")

    return Middenpunt_x, Middenpunt_y


def Oppervlakte_Check(Kleur: str, Huidig_Oppervlakte) -> bool:
    """Functie om te controlleren of een oppervalkte inderdaad hetzelfde oppervalkte is als gemeten, geeft een Bool, 1 of 0, terug"""
    Opgeslagen_Oppervlakte = Verkrijg_Kleur_Oppervlakte(Kleur)

    return Opgeslagen_Oppervlakte * (1 - Oppervlakte_Marge) <= Huidig_Oppervlakte <= Opgeslagen_Oppervlakte * (1 + Oppervlakte_Marge)

def Coordinaten_Doorgeven(InputCoordinaat_X, InputCoordinaat_Y):
    #Vastgestelde aantal pixels naar cm
    Resolutie_Foto = 200 #1cm
    Resolutie_DeltaRobot = 125 #aantal stappen naar cm
    
    #offset 0 punt
    offset_X_As = 15 #cm
    offset_Y_As = 10 #cm
    
    #Formule om de output te berekenen (Input / resolutie_foto + as_Offset ) * Resolutie_DeltaRobot
    Output_Coordinaat_X = (InputCoordinaat_X / Resolutie_Foto + offset_X_As) * Resolutie_DeltaRobot
    Output_Coordinaat_Y = (InputCoordinaat_Y / Resolutie_Foto + offset_Y_As) * Resolutie_DeltaRobot
    
    if Middenpunt_Print:
        print('X:', Output_Coordinaat_X)
        print('Y:',Output_Coordinaat_Y)
    
    return Output_Coordinaat_X, Output_Coordinaat_Y

def Kleuren_Herkennen(Kleur):
    """Hoofdfunctie om de kleuren te zoeken en de contours te tekenen"""
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
        
        if oppervlakte_Print:
            print(f'Oppervlakte {Kleur} = ', Grootst_Oppervlakte)
        
        Vierkant = cv2.minAreaRect(Max_Grootte)
        ((VierkantX, VierkantY),(Breedte,Hoogte), Hoek) = Vierkant
        Doos = cv2.boxPoints(Vierkant)
        Doos = np.intp(Doos)

        if Middenpunt_Print:
            print(Hoek)

        cv2.drawContours(image=Afbeelding, contours=[Doos], contourIdx=-1, color=(0,255,255), thickness=3, lineType=cv2.LINE_4)

        if Oppervlakte_Check(Kleur, Grootst_Oppervlakte):
            Kleuren_Bieb[Kleur]["Voorgekomen"] += 1
            

        if Middenpunt_Print:
            print("Aantal keer voorgekomen: ", Verkrijg_Aantal_Keer_Kleur_Voorgekomen(Kleur))

        # Teken een contour in Zwart rond de grootste contour
        cv2.drawContours(Afbeelding, Basis_contours, Max_Index, (0, 0, 0), 2)
        Coordinaat_X, Coordinaat_Y = Middenpunt_Bepalen(Basis_contours, Max_Index)
        Output_X, Output_Y = Coordinaten_Doorgeven(Coordinaat_X, Coordinaat_Y)

    else:
        Output_X = 0
        Output_Y = 0
        Hoek = 0

    return Basis_Mask, Afbeelding, Output_X, Output_Y, Hoek

# %%
#video Capture functie
Video = cv2.VideoCapture(0)
Aantal_Cyclussen = 0
Max_Aantal_Cyclussen = 1   #De instelbare waarde voor hoevaak de camera aan moet gaan en gaat zoeken
Wachttijd_Tussen_Frame = 5000   #Instelbare wachttijd tussen het maken van een nieuw frame, op moment in ms

while (True):
    _, huidig_Frame = Video.read()
    cv2.imshow('Live Video', huidig_Frame)

    #Druk op de spatiebalk om een frame te nemen
    if cv2.waitKey(1) & 0xFF == 32:
        
        #Optionele while loop, loopt het max aantal lussen door door met een wachttijd om zeker te zijn van object detectie.
        while (Aantal_Cyclussen < Max_Aantal_Cyclussen):
            _, huidig_Frame = Video.read()
            cv2.imshow('Live Video', huidig_Frame)
            Afbeelding, Afbeelding_HSV, Afbeelding2, Afbeelding2_HSV = Afbeelding_Inladen(huidig_Frame)

            for Kleuren_Keys in Kleuren_Bieb.keys():
                if Middenpunt_Print:
                    print(Kleuren_Keys)
                Basis_Masker, Uitslag, Ouput_X,Output_Y, Hoek = Kleuren_Herkennen(Kleuren_Keys)

                cv2.imshow(f'Mask_Kleur{Kleuren_Keys}', Basis_Masker)
                cv2.imshow(f'Uitslag_Kleur{Kleuren_Keys}', Uitslag)

            cv2.imshow(f'Einduitslag{Aantal_Cyclussen}', Uitslag)
            
            #De Q/q toets zorgt dat de while loop verlaten wordt en weer de live feed weergeven wordt.
            if cv2.waitKey(Wachttijd_Tussen_Frame) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            Aantal_Cyclussen += 1
        else:
            Aantal_Cyclussen = 0
            cv2.destroyAllWindows()

    #De X toets sluit de video af
    if cv2.waitKey(1) & 0xFF == ord('x'):

        Video.release()
        cv2.destroyAllWindows()
        break

# %%