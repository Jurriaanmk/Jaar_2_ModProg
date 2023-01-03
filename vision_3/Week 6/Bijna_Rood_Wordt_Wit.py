#%%
import cv2
import numpy as np

# Lees een foto in (grijswaarden)
image = cv2.imread('gekleurde_blokjes.jpg')

lower_bound = np.array([0, 0, 150])
upper_bound = np.array([100, 100, 255])



mask = cv2.inRange(image, lower_bound, upper_bound)

filterd_image = cv2.bitwise_and(image, image, mask=mask)

white_image = np.full(image.shape, 255, dtype=np.uint8)

masked_white_image = cv2.bitwise_and(white_image, white_image, mask=mask)

modified_image = cv2.add(image, masked_white_image)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

contour_image = np.zeros(image.shape, dtype=np.uint8) #maak afbeelding zwart en voeg hierover de contoeren toe
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', contour_image)



cv2.imshow('Contours_2', image)
cv2.imshow('Filtered Image', filterd_image)
cv2.imshow('Modified Image', modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()




# %%


