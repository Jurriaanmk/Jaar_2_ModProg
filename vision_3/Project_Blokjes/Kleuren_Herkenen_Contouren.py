#%% Detectie blauw
import cv2
import numpy as np

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')
# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_color_Wit = np.array([0, 0, 250])
upper_color_Wit = np.array([101, 56, 255])


# Define the range of colors to detect
lower_color_blue = np.array([100, 0, 0])
upper_color_blue = np.array([109, 217, 255])

# Create a mask that only includes pixels within the defined color range
mask_blauw = cv2.inRange(hsv, lower_color_blue, upper_color_blue)
mask_Wit = cv2.inRange(hsv,lower_color_Wit,upper_color_Wit)

# Apply the mask to the original image
res_blauw = cv2.bitwise_and(img, img, mask=mask_blauw)
res_Wit = cv2.bitwise_and(img, img, mask=mask_Wit)

# Find the contours of the colored shapes in the image
contours_blauw, _ = cv2.findContours(mask_blauw, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours_Wit, _ = cv2.findContours(mask_Wit, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw the contours onto the original image
cv2.drawContours(img, contours_blauw, -1, (0, 255, 0), 2)
cv2.drawContours(img, contours_Wit, -1, (0, 255, 0), 2)


# Show the image
#cv2.imshow('mask_blauw', mask_blauw)
cv2.imshow('mask_wit', mask_Wit)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%

import cv2
import numpy as np


rgb_blauw_laag = np.uint8([[[190,101,28 ]]])
rgb_blauw_Hoog = np.uint8([[[255,115,38 ]]])

rgb_Wit_laag = np.uint8([[[250,230,195 ]]])
rgb_Wit_Hoog = np.uint8([[[255,255,255 ]]])

hsv_blauw_laag = cv2.cvtColor(rgb_blauw_laag,cv2.COLOR_BGR2HSV)
hsv_blauw_Hoog = cv2.cvtColor(rgb_blauw_Hoog,cv2.COLOR_BGR2HSV)

hsv_Wit_laag = cv2.cvtColor(rgb_Wit_laag,cv2.COLOR_BGR2HSV)
hsv_Wit_Hoog = cv2.cvtColor(rgb_Wit_Hoog,cv2.COLOR_BGR2HSV)

print(hsv_blauw_laag)
print(hsv_blauw_Hoog)

print(hsv_Wit_laag)
print(hsv_Wit_Hoog)




#%%
import cv2
import numpy as np

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of colors to detect
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

# Create a mask that only includes pixels within the defined color range
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to the original image
res = cv2.bitwise_and(img, img, mask=mask)

# Find the contours of the colored shapes in the image
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw the contours onto the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2
import numpy as np

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of colors to detect
lower_purple = np.array([160, 50, 50])
upper_purple = np.array([190, 255, 255])

# Create a mask that only includes pixels within the defined color range
mask = cv2.inRange(hsv, lower_purple, upper_purple)

# Apply the mask to the original image
res = cv2.bitwise_and(img, img, mask=mask)

# Find the contours of the colored shapes in the image
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Iterate through the contours
for contour in contours:
    # Approximate the contour as a polygonal curve
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Check if the contour has four vertices
    if len(approx) == 4:
        # Check if the contour is convex
        if cv2.isContourConvex(approx):
            # Draw the contour onto the original image
            cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %%
import cv2
import numpy as np

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')


# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Convert the RGB values to the HSV color space
rgb = np.uint8([[[85, 64, 184]]])
hsv_color = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
hue = hsv_color[0][0][0]

# Define the range of colors to detect
lower_purple = np.array([hue-10, 50, 50])
upper_purple = np.array([hue+10, 255, 255])


# Create a mask that only includes pixels within the defined color range
mask = cv2.inRange(hsv, lower_purple, upper_purple)

# Apply the mask to the original image
res = cv2.bitwise_and(img, img, mask=mask)

# Find the contours of the colored shapes in the image
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw the contours onto the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %%
import cv2

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Detect the edges in the image
edges = cv2.Canny(blur, 50, 150)

# Find the contours of the shapes in the image
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Iterate through the contours
for contour in contours:
    # Approximate the contour as a polygonal curve
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Check if the contour has four vertices
    if len(approx) == 4:
        # Check if the contour is convex
        if cv2.isContourConvex(approx):
            # Draw the contour onto the original image
            cv2.drawContours(img, [approx], -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2
import numpy as np

# Load the image
image = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce high frequency noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw them on the original image
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2
import numpy as np

# Load the image
image = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur the image to reduce high frequency noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

cv2.imshow('Non-blurred_image ', blurred_image)


# Perform Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)

# Iterate through the contours and draw them on the original image
for contour in contours:
    # Check if the contour is a square
    if not cv2.isContourConvex(contour):
        # Draw the contour on the image
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Non-Perfect Squares', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2

img = cv2.imread("gekleurde_blokjes.jpg") # Read image

# Setting parameter values
t_lower = 50 # Lower Threshold
t_upper = 150 # Upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img, t_lower, t_upper)

cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%%
import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('gekleurde_blokjes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use the Canny function to detect edges in the image
edges = cv2.Canny(gray, 10, 150)

# Find the contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw them on the image
for contour in contours:
    if len(contour) == 4:
        # This is a square, so draw it in yellow
        cv2.drawContours(image, [contour], 0, (0, 255, 255), 2)
    elif len(contour) == 3:
        # This is a triangle, so draw it in red
        cv2.drawContours(image, [contour], 0, (0, 0, 255), 2)
    elif len(contour) > 10:
        # This is some other shape, so draw it in green
        cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('gekleurde_blokjes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use thresholding to create a binary image
threshold, binary_image = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Find the contours in the image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and approximate them with polygons
for contour in contours:
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # Check the number of points in the approximated polygon
    if len(approx) == 4:
        # This is a square, so draw it in yellow
        cv2.drawContours(image, [approx], 0, (0, 255, 255), 2)
    elif len(approx) == 3:
        # This is a triangle, so draw it in red
        cv2.drawContours(image, [approx], 0, (0, 0, 255), 2)
    elif len(approx) > 10:
        # This is a larger shape, so draw it in green
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)

# Show the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
import cv2
import numpy as np
image_obj = cv2.imread('gekleurde_blokjes.jpg')

gray = cv2.cvtColor(image_obj, cv2.COLOR_BGR2GRAY)

kernel = np.ones((4, 4), np.uint8)
dilation = cv2.dilate(gray, kernel, iterations=1)

blur = cv2.GaussianBlur(dilation, (5, 5), 0)


thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

# Now finding Contours         ###################
contours, _ = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
coordinates = []
for cnt in contours:
        # [point_x, point_y, width, height] = cv2.boundingRect(cnt)
    approx = cv2.approxPolyDP(
        cnt, 0.07 * cv2.arcLength(cnt, True), True)
    if len(approx) == 3:
        coordinates.append([cnt])
        cv2.drawContours(image_obj, [cnt], 0, (0, 0, 255), 3)

#cv2.imwrite("result.png", image_obj)
cv2.imshow('Image', image_obj)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
