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







# %%
