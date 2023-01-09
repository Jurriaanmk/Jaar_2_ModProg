#%%
import numpy as np
import cv2

# Read an image
image = cv2.imread('gekleurde_blokjes.jpg', cv2.IMREAD_COLOR)
image_cv2 = cv2.imread('gekleurde_blokjes.jpg')


def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df / mx
    v = mx
    return h, s, v


rows, cols = image.shape[:2]
image_hsv = np.empty_like(image)

for i in range(rows):
    for j in range(cols):
        b, g, r = image[i, j]
        h, s, v = rgb_to_hsv(b, g, r)
        image_hsv[i, j] = [h, s, v]


image_cv2_hsv = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2HSV)

cv2.imshow('Manual Conversion', image_hsv)
cv2.imshow('CV2 Conversion', image_cv2_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
