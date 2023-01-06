#%%
import cv2
import numpy as np

Afbeelding = cv2.imread('gekleurde_blokjes.jpg',0)
Voorbeeld_Geel_Blokje = cv2.imread('gekleurde_blokjes_geel.jpg',0)
h,w = Voorbeeld_Geel_Blokje.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    afbeelding2 = Afbeelding.copy()
    
    resultaat =  cv2.matchTemplate(afbeelding2, Voorbeeld_Geel_Blokje, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultaat)
    print(min_loc, max_loc)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        locatie = min_loc
    else:
        locatie = max_loc
    
    bodem_rechts = (locatie[0]+w,locatie[1]+h)
    cv2.rectangle(afbeelding2,locatie,bodem_rechts,255,5)
    
    cv2.imshow('Match', afbeelding2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# %%
import cv2
import numpy as np

# Load the image and template
image = cv2.imread("gekleurde_blokjes.jpg")
template = cv2.imread("gekleurde_blokjes_geel.jpg")

# Perform template matching
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Extract the region where the template is located
x, y = max_loc
w, h, _ = template.shape
cropped_image = image[y:y+h, x:x+w]

# Perform edge detection on the cropped image
edges = cv2.Canny(cropped_image, 100, 200)

# Draw the edges on the original image
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Show the final image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
