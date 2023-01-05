#%%
import cv2
import numpy as np

# Load the image
img = cv2.imread('gekleurde_blokjes.jpg')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of colors to detect
lower_color = np.array([100, 50, 50])
upper_color = np.array([140, 255, 255])

# Create a mask that only includes pixels within the defined color range
mask = cv2.inRange(hsv, lower_color, upper_color)

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
