# %%
import cv2
import numpy as np

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)

cv2.imshow('Orginele Afbeelding', Afbeelding)
cv2.imshow('Orginele HSV', Afbeelding_HSV)

Lower_Kleuren = np.array([163, 155, 181])
Higher_Kleuren = np.array([179, 213, 223])


mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren)

Filter_Afbeelding = cv2.bitwise_and(Afbeelding, Afbeelding, mask=mask)

Wit_Afbeelding = np.full(Afbeelding.shape, 255, dtype=np.uint8)

masked_Wit_Afbeelding = cv2.bitwise_and(Wit_Afbeelding, Wit_Afbeelding, mask=mask)

Aangepaste_Afbeelding = cv2.add(Afbeelding, masked_Wit_Afbeelding)

contouren, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(Afbeelding, contouren, -1, (0, 255, 0), 3)

# maak afbeelding zwart en voeg hierover de contoeren toe
contouren_Afbeelding = np.zeros(Afbeelding.shape, dtype=np.uint8)
cv2.drawContours(contouren_Afbeelding, contouren, -1, (0, 255, 0), 3)


cv2.imshow('mask',mask)
cv2.imshow('Afbeelding Met Contour', Afbeelding)
cv2.imshow('Contouren', contouren_Afbeelding)
cv2.imshow('Filter Afbeelding', Filter_Afbeelding)
cv2.imshow('Aangepaste Afbeelding', Aangepaste_Afbeelding)

cv2.waitKey(0)
cv2.destroyAllWindows()


# %%
