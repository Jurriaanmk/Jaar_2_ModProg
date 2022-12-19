#%%
import cv2
import numpy as np

# Read the image file
img = cv2.imread('Cheshire.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the number of pixels to change to black
num_pixels = gray.size * 0.01

# Generate a list of random indices
indices = np.random.choice(gray.size, int(num_pixels), replace=False)

# Change the pixels at the random indices to black
for i in indices:
    gray[i//gray.shape[1], i%gray.shape[1]] = 0

# Save the modified image
cv2.imwrite('Cheshire_modified_image.jpg', gray)
#%%

