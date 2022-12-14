#%% Opgave 1 

import numpy as np
import cv2 
from scipy import signal
import matplotlib.pyplot as plt


Afbeelding_Disney = cv2.imread('Disney.jpg')
gray = cv2.cvtColor(Afbeelding_Disney, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[-1,0,1],
                     [-2,0,2],
                     [-1,0,1]])

derivative = signal.convolve2d(gray, kernel_x, boundary='symm', mode='same')

gradient = np.sqrt(derivative**2)

gradient = gradient / np.max(gradient)
threshold = 0.5
edge_map = (gradient > threshold).astype(np.uint8) * 255

low_threshold = 50
high_threshold = 150
edge_map = cv2.Canny(gray, low_threshold, high_threshold)

kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])


laplacian = signal.convolve2d(gray, kernel, boundary='symm', mode='same')

threshold = 50
edge_map = (laplacian > threshold).astype(np.uint8) * 255


fig, axs = plt.subplots(2, 2)

# Display the original image
axs[0, 0].imshow(Afbeelding_Disney)
axs[0, 0].set_title('Original Image')

# Display the derivative
axs[0, 1].imshow(derivative, cmap='gray')
axs[0, 1].set_title('Derivative')

# Display the gradient magnitude
axs[1, 0].imshow(gradient, cmap='gray')
axs[1, 0].set_title('Gradient Magnitude')

# Display the edge map
axs[1, 1].imshow(edge_map, cmap='gray')
axs[1, 1].set_title('Edge Map')

# Show the figure
plt.show()

#%% 4
import cv2
import numpy as np

# Read image
img = cv2.imread("Disney.jpg", cv2.IMREAD_GRAYSCALE)

# Prewitt operator kernels
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Apply convolution using the kernels
prewitt_x_image = cv2.filter2D(img, -1, prewitt_x)
prewitt_y_image = cv2.filter2D(img, -1, prewitt_y)

# Add the two images to get the final result
prewitt_image = cv2.addWeighted(prewitt_x_image, 0.5, prewitt_y_image, 0.5, 0)

# Show and save the image
cv2.imshow("Prewitt Image", prewitt_image)
cv2.imwrite("prewitt_image.jpg", prewitt_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# %% Opgave 6-7

import cv2
import numpy as np

afbeelding = cv2.imread('Bolletjes_Grijs.jpg',0)

kernel = np.ones((5,5), np.uint8)

afbeelding_Dilatie = cv2.dilate(afbeelding, kernel, iterations =1)

cv2.imshow('input', afbeelding)
cv2.imshow('dilatie', afbeelding_Dilatie)

cv2.waitKey(0)
cv2.destroyAllWindows()




# %%
