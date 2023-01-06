#%%
#Code om de contouren te herkenen op basis van kleur. Geen vorm herkening.
#Code moet nog aangepast worden, op moment bij enkele kleuren een error dat er gedeeld wordt door 0, komt waarschijnlijk omdat er niet een perfect middenpunt is
import cv2
import numpy as np

Middenpunt_Weergeven = 1

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)

def Verkrijg_kleur_randwaardes(kleur): #Bieb voor alle kleuren, makkelijk en snel
    Kleuren_Bieb = {
        "Rood": (np.array([163, 155, 181]), np.array([179, 213, 223])),
        "Wit": (np.array([85, 9, 223]), np.array([121, 62, 255])),
        "Blauw":(np.array([90, 111, 196]), np.array([113, 233, 232])),
        "Paars":(np.array([122, 121, 169]), np.array([130, 173, 204])),
        "Oranje":(np.array([0, 121, 157]), np.array([7, 159, 231])),
        "Groen": (np.array([70, 190, 84]),np.array([97, 255, 255])),
        "Geel": (np.array([22, 241, 201]), np.array([30, 255, 225])),
    }
    return Kleuren_Bieb[kleur]

def Middenpunt_Bepalen(Contour): # Functie om te bepalen wat de middenpunten van alle objecten zijn en hier een stipje te zetten en de coordinaten te exporteren
    moments = cv2.moments(Contour[0])
    Middenpunt_x = int(moments['m10'] / moments['m00'])
    Middenpunt_y = int(moments['m01'] / moments['m00'])
    print("Middenpunt: (", Middenpunt_x, ", ", Middenpunt_y, ")")

    if Middenpunt_Weergeven:
          cv2.circle(Afbeelding, (Middenpunt_x, Middenpunt_y), 5, (0, 0, 0), -1)

    return Middenpunt_x, Middenpunt_y

def Kleuren_Herken(Kleur): #Hoofdfunctie om de kleuren te zoeken en de contours te tekenen
    Lower_Kleuren, Higher_Kleuren = Verkrijg_kleur_randwaardes(Kleur)

    Basis_Mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren)
    Basis_Res = cv2.bitwise_and(Afbeelding, Afbeelding, mask=Basis_Mask)
    Basis_contours, _ = cv2.findContours(Basis_Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(Afbeelding, Basis_contours, -1, (0, 255, 0), 2)

    Middenpunt_Bepalen(Basis_contours)

    cv2.imshow('Mask_Kleur:', Basis_Mask)
    cv2.imshow('Uitslag', Afbeelding)
    cv2.imwrite("uitslag.png", Afbeelding)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%


