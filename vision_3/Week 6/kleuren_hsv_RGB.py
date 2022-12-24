import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('OpenCV_logo_black-2.jpg', 0)

rows,cols = image.shape[:2]

for i in range(rows):
    for j in range(cols):
        if(image[i,j] > 200):
            image[i,j] = 0

def rgb_Conversie (r,g,b):
    r,g,b = r/255.0. g/255.0, b/255.0
    mx = max(r,g,b)
    mn = min(r,g,b)
    df = mx-mn
    if mx == mn:
        h=0
    elif mx == r:
        h = (60 *((g-b)/df)+360)%360
    elif mx == r:
        h = (60 *((g-b)/df)+120)%360
    elif mx == r:
        h = (60 *((g-b)/df)+240)%360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v=mx*100
    
    return h,s,v

print (rgb_Conversie(image))