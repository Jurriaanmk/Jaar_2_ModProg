#%% Opgave 2 bepaal afgeleide 1 afbeelding op basis van de Disney.jpg

import numpy as np
import cv2 

Afbeelding_Disney = cv2.imread('Disney.jpg', 0)
Afbeelding_Disney = cv2.cvtColor(Afbeelding_Disney, cv2.COLOR_BGR2GRAY)
Afbeelding_Disney_Mediaan = cv2.medianBlur(Afbeelding_Disney,0.5)


rows, colloms = Afbeelding_Disney_Mediaan[:2]
Afbeelding_Disney_Diff_x = numpy.diff(rows)
Afbeelding_Disney_Diff_y = numpy.diff(colloms)
Afbeelding_Disney_Diff = Afbeelding_Disney_Diff_y/Afbeelding_Disney_Diff_x

#%%

for i in range(rows):
    for j in range(colloms):
        
        



