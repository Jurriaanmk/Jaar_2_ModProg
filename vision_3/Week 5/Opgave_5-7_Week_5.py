#schrink en grow is randen detectie en de randen te laten omvloeien naar de buren

import numpy as np
import cv2 

afbeelding = cv2.imread('Bolletjes.jpg',0)

rijnen, kolommen =afbeelding[:2]

for i in range(rijnen):
    for j in range(kolommen):
        if(afbeelding[i,j])