
#Een afbeeldign bestaat uit grijswaarde waarvan de laagste waarde 64 is en hoogste 255
#De helderheid van de afbeelding wordt verhoogt oor alle pixelwaarde met 1.5 te vermedigvuldigen
#%% Opdracht 18
import cv2
import numpy as np
import matplotlib.pyplot as plt
import typing

#inlezen afbeelding
Orginele_Afbeelding = cv2.imread('Daantje.jpg', cv2.IMREAD_GRAYSCALE)

#Herformateren van afbeelding zodat we het kunnen zien
Orginele_Afbeelding = cv2.resize(Orginele_Afbeelding,(307,408))

#afbeelding limiten zetten van min 64 en max 255
Bewerkte_Afbeelding = np.clip(Orginele_Afbeelding, 64, 255)

#Afbeelding maal 1.5
Bewerkte_Afbeelding_maal_1_5 = cv2.convertScaleAbs(Bewerkte_Afbeelding, alpha = 1.5)

#Afbeelding geedeeld door 1.5
Bewerkte_Afbeelding_gedeeld_door_1_5 = cv2.convertScaleAbs(Bewerkte_Afbeelding_maal_1_5, alpha = 1/1.5)

Histogram_Orginele_Afbeelding = cv2.calcHist([Orginele_Afbeelding],[0],None,[256],[0,256])
Histogram_Bewerkte_Afbeelding = cv2.calcHist([Bewerkte_Afbeelding],[0],None,[256],[0,256])
Histogram_Bewerkte_Afbeelding_maal_1_5 = cv2.calcHist([Bewerkte_Afbeelding_maal_1_5],[0],None,[256],[0,256])
Histogram_Bewerkte_Afbeelding_gedeeld_door_1_5 = cv2.calcHist([Bewerkte_Afbeelding_gedeeld_door_1_5],[0],None,[256],[0,256])



#Histogram maken voor alle afbeeldingen
fig, axs = plt.subplots(1,4)
axs[0].hist(Orginele_Afbeelding.ravel(),256,[0,256], color = 'red')
axs[0].set_title('Hist Orgineel')
axs[1].hist(Bewerkte_Afbeelding.ravel(),256,[0,256], color = 'blue')
axs[1].set_title('Hist Bewerkt')
axs[2].hist(Bewerkte_Afbeelding_maal_1_5.ravel(),256,[0,256], color = 'green')
axs[2].set_title('Hist *1.5 ')
axs[3].hist(Bewerkte_Afbeelding_gedeeld_door_1_5.ravel(),256,[0,256], color = 'orange')
axs[3].set_title('Hist *1.5 /1.5')


cv2.imshow('Orginele Afbeelding', Orginele_Afbeelding)
cv2.imshow('Bewerkte Afbeelding', Bewerkte_Afbeelding)
cv2.imshow('Bewerkte *1.5 Afbeelding', Bewerkte_Afbeelding_maal_1_5)
cv2.imshow('Bewerkte /1.5 Afbeelding', Bewerkte_Afbeelding_gedeeld_door_1_5)

cv2.waitKey(0)
cv2.destroyAllWindows()

Afbeeldingen = [Orginele_Afbeelding,Bewerkte_Afbeelding,Bewerkte_Afbeelding_maal_1_5,Bewerkte_Afbeelding_gedeeld_door_1_5]

for i, afbeelding in enumerate(Afbeeldingen):
    min_intensity = np.min(afbeelding)
    max_intensity = np.max(afbeelding)
    epsilon = 1e-5 # a small value
    dynamic_range = max_intensity / (min_intensity + epsilon)
    
    print('Dynamische bereik van de {} afbeelding is'.format(i), dynamic_range)
    print('Minimaal = ',min_intensity)
    print('Maximaal = ',max_intensity)
# %%
