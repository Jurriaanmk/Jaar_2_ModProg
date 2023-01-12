#Maak een afbeelding waarin vanaf rood tot paars van bovenaf naar beneden wordt weergeven
#Methode HSV de Hue vanaf 127-255 naar 0-126

#%%
import cv2
import numpy as np

Hoogte = 700
Breedte = 200

# Maak een afbeelding met de maten van Breedte en Hoogte
Afbeelding = np.zeros((Hoogte, Breedte, 3), dtype=np.uint8) 

for x in range(Breedte):
    for y in range(Hoogte):
        # Zet de H (Hue) op basis van de hoogte
        hue = int((180 * y)/Hoogte)
        # Overige kanalen op 255 zetten (max saturatie, max value)
        sat = 255
        val = 255
        # Terug naar het RGB (BGR) spectrum
        b, g, r = cv2.cvtColor(np.uint8([[[hue, sat, val]]]), cv2.COLOR_HSV2BGR)[0][0]
        Afbeelding[y,x] = [b,g,r]

# Save the Afbeelding to a file
cv2.imwrite("Kleuren_Spectrum.jpg",Afbeelding)
cv2.imshow('Kleuren Spectrum', Afbeelding)

cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
