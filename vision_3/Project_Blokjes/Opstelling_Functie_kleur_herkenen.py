#%%
import cv2
import numpy as np

Middenpunt_Weergeven = 1

def Middenpunt_Bepalen(Contour):
    moments = cv2.moments(Contour[0])
    centroid_x = int(moments['m10'] / moments['m00'])
    centroid_y = int(moments['m01'] / moments['m00'])
    print("Centroid: (", centroid_x, ", ", centroid_y, ")")
    if Middenpunt_Weergeven:
          cv2.circle(img, (centroid_x, centroid_y), 5, (255, 255, 255), -1)
    return centroid_x, centroid_y

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')
# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_color_Wit = np.array([0, 0, 250])
upper_color_Wit = np.array([103, 56, 255])

lower_color_blauw = np.array([99, 199, 202])
upper_color_blauw = np.array([110, 232, 231])

lower_color_Rood = np.array([163, 155, 181])
upper_color_Rood = np.array([179, 213, 223])

lower_color_Paars = np.array([122, 121, 169])
upper_color_Paars = np.array([130, 173, 204])

lower_color_Oranje = np.array([0, 121, 157])
upper_color_Oranje = np.array([7, 159, 231])

lower_color_Groen = np.array([70, 190, 84])
upper_color_Groen = np.array([97, 255, 255])

lower_color_Geel = np.array([22, 241, 201])
upper_color_Geel = np.array([30, 255, 225])


# Create a mask that only includes pixels within the defined color range
mask_blauw = cv2.inRange(hsv, lower_color_blauw, upper_color_blauw)
mask_Wit = cv2.inRange(hsv,lower_color_Wit,upper_color_Wit)
mask_Rood = cv2.inRange(hsv,lower_color_Rood,upper_color_Rood)
mask_Paars = cv2.inRange(hsv,lower_color_Paars,upper_color_Paars)
mask_Oranje = cv2.inRange(hsv,lower_color_Oranje,upper_color_Oranje)
mask_Groen = cv2.inRange(hsv,lower_color_Groen,upper_color_Groen)
mask_Geel = cv2.inRange(hsv,lower_color_Geel,upper_color_Geel)


# Apply the mask to the original image
res_blauw = cv2.bitwise_and(img, img, mask=mask_blauw)
res_Wit = cv2.bitwise_and(img, img, mask=mask_Wit)
res_Rood = cv2.bitwise_and(img, img, mask=mask_Rood)
res_Paars = cv2.bitwise_and(img, img, mask=mask_Paars)
res_Oranje = cv2.bitwise_and(img, img, mask=mask_Oranje)
res_Groen = cv2.bitwise_and(img, img, mask=mask_Groen)
res_Geel = cv2.bitwise_and(img, img, mask=mask_Geel)


# Find the contours of the colored shapes in the image
contours_blauw, _ = cv2.findContours(mask_blauw, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Wit, _ = cv2.findContours(mask_Wit, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Rood, _ = cv2.findContours(mask_Rood, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Paars, _ = cv2.findContours(mask_Paars, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Oranje, _ = cv2.findContours(mask_Oranje, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Groen, _ = cv2.findContours(mask_Groen, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Geel, _ = cv2.findContours(mask_Geel, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw the contours onto the original image
cv2.drawContours(img, contours_blauw, -1, (0, 255, 0), 2)
cv2.drawContours(img, contours_Wit, -1, (0, 255, 200), 2)
cv2.drawContours(img, contours_Rood, -1, (0, 0, 255), 2)
cv2.drawContours(img, contours_Paars, -1, (110, 50, 60), 2)
cv2.drawContours(img, contours_Oranje, -1, (255, 50, 60), 2)
cv2.drawContours(img, contours_Groen, -1, (255, 200, 100), 2)
cv2.drawContours(img, contours_Geel, -1, (255, 200, 100), 2)

Middenpunt_Bepalen(contours_Geel)

# Show the image
cv2.imshow('mask_blauw', mask_blauw)
cv2.imshow('mask_wit', mask_Wit)
cv2.imshow('mask_rood', mask_Rood)
cv2.imshow('mask_Paars', mask_Paars)
cv2.imshow('mask_Oranje', mask_Oranje)
cv2.imshow('mask_Groen', mask_Groen)
cv2.imshow('mask_Geel', mask_Geel)

cv2.imshow('uitslag', img)
cv2.imwrite("uitslag.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %% kleur bepaling door bgr naar hsv
Blauw = 225
Groen = 104
Rood = 87
BGR_kleur = np.uint8([[[Blauw,Groen,Rood]]])
print(cv2.cvtColor(BGR_kleur, cv2.COLOR_BGR2HSV))
# %%

#%%
import cv2
import numpy as np

Middenpunt_Weergeven = 1

def Kleuren_Herken(Lower_Kleuren,Higher_Kleuren):
    Basis_Mask = cv2.inRange(Afbeelding_HSV, Lower_Kleuren, Higher_Kleuren)
    Basis_Res = cv2.bitwise_and(Afbeelding, Afbeelding, mask=Basis_Mask)
    Basis_contours, _ = cv2.findContours(Basis_Mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(Afbeelding, Basis_contours, -1, (0, 255, 0), 2)

    Middenpunt_Bepalen(Basis_contours)
    
    cv2.imshow('Mask_Kleur:', Basis_Mask)

    cv2.imshow('Uitslag', Afbeelding)
    cv2.imwrite("uitslag.png", Afbeelding)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def Middenpunt_Bepalen(Contour):
    moments = cv2.moments(Contour[0])
    Middenpunt_x = int(moments['m10'] / moments['m00'])
    Middenpunt_y = int(moments['m01'] / moments['m00'])
    print("Middenpunt: (", Middenpunt_x, ", ", Middenpunt_y, ")")
    if Middenpunt_Weergeven:
          cv2.circle(Afbeelding, (Middenpunt_x, Middenpunt_y), 5, (255, 255, 255), -1)
    return Middenpunt_x, Middenpunt_y

Afbeelding = cv2.imread('gekleurde_blokjes.jpg')
Afbeelding_HSV = cv2.cvtColor(Afbeelding, cv2.COLOR_BGR2HSV)

##Lower_Kleuren = np.array([0,0,0])
#Higher_Kleuren = np.array([0,0,0])
# %%
