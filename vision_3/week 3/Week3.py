#%%
import numpy as np

import cv2

# Lees een foto in (grijswaarden)
img = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(img, (800, 600)) 

rows,cols = img.shape[:2]
helder =0

for i in range(rows):
    for j in range(cols):
        k = img[i,j]
        img[i,j] = 255 - (k // 32) * 32
        if(img[i,j] > 127):
            helder +=1

helderpercentage = (helder / (rows*cols) )* 100
print(i+1, j+1)
print(np.average(img))
print(helderpercentage)



cv2.imshow('plaatje',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('Kroatie_out.jpg', img)
#%%