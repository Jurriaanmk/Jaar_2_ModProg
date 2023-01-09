# %%
import cv2
import numpy as np
from typing import Tuple


Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
for i in range(10):
    cv2.imshow(f'Plaatje{i}', Afbeelding)
cv2.waitKey(2000)
cv2.destroyAllWindows()
# %%
