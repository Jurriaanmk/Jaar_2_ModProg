<<<<<<< Updated upstream
#schrink en grow is randen detectie en de randen te laten omvloeien naar de buren

import numpy as np
import cv2 

afbeelding = cv2.imread('Bolletjes.jpg',0)

rijnen, kolommen =afbeelding[:2]

for i in range(rijnen):
    for j in range(kolommen):
        if(afbeelding[i,j])
=======
#%%
from PIL import Image, ImageDraw

# Open the image and convert it to RGB
image = Image.open('Bolletjes.jpg').convert('RGB')

# Get the width and height of the image
width, height = image.size

# Create a blank image with the same size
result = Image.new('RGB', (width, height))

# Get the pixels of the image
pixels = image.load()

# Iterate over the pixels
for x in range(width):
    for y in range(height):
        # Get the pixel at (x, y)
        r, g, b = pixels[x, y]

        # Check if the pixel is pink (255, 192, 203)
        if r == 255 and g == 192 and b == 203:
            # Shrink or grow the pixel depending on its position
            if x < width / 2 and y < height / 2:
                # Shrink the pixel
                r //= 2
                g //= 2
                b //= 2
            else:
                # Grow the pixel
                r *= 2
                g *= 2
                b *= 2

        # Set the pixel in the result image
        result.putpixel((x, y), (r, g, b))

# Save the result image
result.save('result.jpg')
# %%
>>>>>>> Stashed changes
