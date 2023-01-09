#%%
import cv2
import numpy as np
from typing import Tuple

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_Copy = Afbeelding.copy()
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)
Afbeelding_Zwart_Wit = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2GRAY)


def Teken_Contours(Afbeelding_Doel):
    Afbeelding_Nummer = 0

    _, marge = cv2.threshold(Afbeelding_Doel, 100, 255, cv2.THRESH_BINARY)

    Contours, _ = cv2.findContours(marge, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    for Contouren in Contours:
        cv2.drawContours(Afbeelding_Doel, Contouren, -1, (0,255,0),3)

    Afbeelding_Nummer += 1
    cv2.imshow('Afbeelding'+ str(Afbeelding_Nummer),Afbeelding_Doel)

randen = cv2.Canny(Afbeelding_Zwart_Wit, 10, 200)

cv2.imshow('Zwart_Wit_Canny',randen)


Afbeelding_Blur_Filter = cv2.GaussianBlur(Afbeelding_Zwart_Wit,(5,5),0)

cv2.imshow('Zwart_Wit_Afbeelding_Blur_filter',Afbeelding_Blur_Filter)
cv2.imshow('Zwart_Wit_Afbeelding_Zwart_Wit',Afbeelding_Zwart_Wit)

Teken_Contours(Afbeelding_Blur_Filter)
Teken_Contours(Afbeelding_Zwart_Wit)

randen_Blur = cv2.Canny(Afbeelding_Blur_Filter, 50, 200)

cv2.imshow('Zwart_Wit_Canny_Blur',randen_Blur)

laplacian = cv2.Laplacian(Afbeelding_Blur_Filter,5,cv2.CV_64F)
filtered_image = cv2.convertScaleAbs(laplacian)
cv2.imshow('Zwart_Wit_filtered_image',filtered_image)


cv2.imshow('Zwart_Wit_Afbeelding_Contouren',Afbeelding_Copy)

cv2.waitKey(0)
cv2.destroyAllWindows()


 # %%
