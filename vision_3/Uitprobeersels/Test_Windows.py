#%%
import cv2
import numpy as np
from typing import Tuple

Afbeelding = cv2.imread('Bloemen.jpg')

 
cv2.namedWindow("Hervorm", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Hervorm", 600, 600)

cv2.imshow("Hervorm", Afbeelding)

cv2.waitKey()
cv2.destroyAllWindows()
# %%
