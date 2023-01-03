#%%
#schrink en grow is randen detectie en de randen te laten omvloeien naar de buren
import cv2
import numpy as np

# read in image
image = cv2.imread('Bolletjes.jpg')

# get number of rows and columns in image
rows, cols = image.shape[:2]

# iterate over rows and columns in image
for row in range(rows):
    for col in range(cols):
        pixel = image[row, col]
        
        # check if pixel is pink
        if pixel[0] > 200 and pixel[1] < 50 and pixel[2] > 200:
            # get neighboring pixels
            neighbors = [image[row-1, col], image[row+1, col], image[row, col-1], image[row, col+1]]

            # calculate average value of neighbors
            mean_value = np.mean(neighbors, axis=0).astype(np.uint8)

            # set pixel value in image to average value of neighbors
            image[row, col] = mean_value
        
        # display image
        cv2.imshow('Shrunken Circle', image)
        cv2.waitKey(1)

# close window
cv2.destroyAllWindows()

# %%

import cv2
import numpy as np

# read in image
image = cv2.imread('Bolletjes.jpg')
# get number of rows and columns in image
rows, cols = image.shape[:2]

PINK_MIN_R = 190
PINK_MAX_G = 100
PINK_MIN_B = 190


# iterate over rows and columns in image
for row in range(rows):
    for col in range(cols):
        pixel = image[row, col]
        
        # check if pixel is adjacent to a pink pixel
        pink = pixel[0] > PINK_MIN_B and pixel[1] < PINK_MAX_G and pixel[2] > PINK_MIN_R
        left = col > 0 and image[row, col-1][0] > PINK_MIN_B and image[row, col-1][1] < PINK_MAX_G and image[row, col-1][2] > PINK_MIN_R
        right = col < cols-1 and image[row, col+1][0] > PINK_MIN_B and image[row, col+1][1] < PINK_MAX_G and image[row, col+1][2] > PINK_MIN_R
        top = row > 0 and image[row-1, col][0] > PINK_MIN_B and image[row-1, col][1] < PINK_MAX_G and image[row-1, col][2] > PINK_MIN_R
        bottom = row < rows-1 and image[row+1, col][0] > PINK_MIN_B and image[row+1, col][1] < PINK_MAX_G and image[row+1, col][2] > PINK_MIN_R
        if pink or left or right or top or bottom:
            # get neighboring pixels
            neighbors = [image[row-1, col], image[row+1, col], image[row, col-1], image[row, col+1]]
            
            # calculate average value of neighbors
            mean_value = np.mean(neighbors, axis=0).astype(np.uint8)
            
            # set pixel value in image to average value of neighbors
            image[row, col] = mean_value
            
            # display image
            
cv2.imshow('Shrunken Circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
