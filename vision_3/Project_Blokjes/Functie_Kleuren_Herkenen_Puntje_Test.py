#%%
#Code om de contouren te herkenen op basis van kleur. Geen vorm herkening.
#Code moet nog aangepast worden, op moment bij enkele kleuren een error dat er gedeeld wordt door 0, komt waarschijnlijk omdat er niet een perfect middenpunt is
import cv2
import numpy as np

Middenpunt_Weergeven = 1

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)
Afbeelding2 = Afbeelding.copy()
Afbeelding2_HSV = cv2.cvtColor(Afbeelding2, cv2.COLOR_BGR2HSV)

Kleuren_Bieb = {    #Bieb voor alle kleuren
        "Rood": (np.array([163, 155, 181]), np.array([179, 213, 223])),
        "Wit": (np.array([85, 9, 223]), np.array([121, 62, 255])),
        "Blauw":(np.array([90, 111, 196]), np.array([113, 233, 232])),
        "Paars":(np.array([122, 121, 169]), np.array([130, 173, 204])),
        "Oranje":(np.array([0, 121, 157]), np.array([7, 159, 231])),
        "Groen": (np.array([70, 190, 84]),np.array([97, 255, 255])),
        "Geel": (np.array([22, 241, 201]), np.array([30, 255, 225])),
    }

def Verkrijg_kleur_randwaardes(kleur): #functie om alle kleuren optehalen
    return Kleuren_Bieb[kleur]

def Middenpunt_Bepalen(Contour,index): # Functie om te bepalen wat de middenpunten van alle objecten zijn en hier een stipje te zetten en de coordinaten te exporteren
    moments = cv2.moments(Contour[index])
    Middenpunt_x = int(moments['m10'] / moments['m00'])
    Middenpunt_y = int(moments['m01'] / moments['m00'])
    print("Middenpunt: (", Middenpunt_x, ", ", Middenpunt_y, ")")

    if Middenpunt_Weergeven:
          cv2.circle(Afbeelding, (Middenpunt_x, Middenpunt_y), 5, (0, 0, 0), -1)

    return Middenpunt_x, Middenpunt_y

def Kleuren_Herken(Kleur): #Hoofdfunctie om de kleuren te zoeken en de contours te tekenen
    Lower_Kleuren, Higher_Kleuren = Verkrijg_kleur_randwaardes(Kleur) # Haal de eigenschappen van de kleuren op en stop ze in de juiste waarde

    Basis_Mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren) #Maak een filter masker waar enkel de geselecteerde kleur in te zien is.
    Basis_Res = cv2.bitwise_and(Afbeelding, Afbeelding, mask=Basis_Mask)
    Basis_contours, _ = cv2.findContours(Basis_Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    if len(Basis_contours) != 0: #Maak een blauwe contour om alle gevonden contouren
        cv2.drawContours(Afbeelding, Basis_contours, -1, (255, 0, 0), 3)

        #Vind de grootste contour in alle gevonden contouren
        c = max(Basis_contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

        #Teken een vierkant rond het grootste contour in Groen
        cv2.rectangle(Afbeelding,(x,y),(x+w,y+h),(0,255,0),2)

        areas = [cv2.contourArea(c) for c in Basis_contours] #Zoek de contouren in alle contouren
        max_index = np.argmax(areas) #Selecteerd de grootste contour uit alle contouren

        cv2.drawContours(Afbeelding, Basis_contours,max_index, (0, 0, 0), 2) #Teken een contour in Zwart rond de grootste contour

        Middenpunt_Bepalen(Basis_contours,max_index)

    cv2.imshow('Mask_Kleur:', Basis_Mask)
    cv2.imshow('Uitslag', Afbeelding)
    cv2.imwrite("uitslag.png", Afbeelding)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%