#%%
import cv2
import numpy as np
from typing import Tuple

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)


Lower_Kleuren,Higher_Kleuren = np.array([122, 121, 169]), np.array([130, 173, 204])

Basis_Mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren)
Basis_Res = cv2.bitwise_and(Afbeelding, Afbeelding, mask=Basis_Mask)
Basis_contours, _ = cv2.findContours(Basis_Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

Max_Grootte = max(Basis_contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(Max_Grootte)

# Teken een vierkant rond het grootste contour in Groen
cv2.rectangle(Afbeelding, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Zoek de contouren in alle contouren
areas = [cv2.contourArea(Max_Grootte)for Max_Grootte in Basis_contours]
# Selecteerd de grootste contour uit alle contouren
Grootst_Oppervlakte = max(areas)
Max_Index = np.argmax(areas)

#Zoek hoek van object geef dit in tekst op scherm + in variable in dict
Vierkant = cv2.minAreaRect(Max_Grootte)
((VierkantX, VierkantY),(Breedte,Hoogte),Hoek) = Vierkant
Doos = cv2.boxPoints(Vierkant)
Doos = np.intp(Doos)

print(Hoek)

cv2.drawContours(image=Afbeelding, contours=[Doos], contourIdx=-1, color=(0,255,255), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow('Mask_Kleur:', Basis_Mask)
cv2.imshow('Uitslag', Afbeelding)
cv2.imwrite("uitslag.png", Afbeelding)
cv2.waitKey()
cv2.destroyAllWindows()
# %%
