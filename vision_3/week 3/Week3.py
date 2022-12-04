#%% Opgave 2
import numpy as np

import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder =0

for i in range(rows):
    for j in range(cols):
        if(image[i,j] > 127):
            helder +=1

helderpercentage = (helder / (rows*cols) )* 100 #print de helderheid van de afbeelding
print(image.shape) 

print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('Kroatie_out.jpg', image)
#%% Opgave 3a

import numpy as np

import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder =0

image = cv2.bitwise_not(image)

for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        #image[i,j] = 255 - k 
        
        if(image[i,j] > 127):
            helder +=1

helderpercentage = (helder / (rows*cols) )* 100

print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%% Opgave 3 b

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder = 0
drempelwaarde = int (input("Voor maximum waarde voor helderheid in: "))
for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        image[i,j] = drempelwaarde - k #(k // 32) * 32
        if(image[i,j] > 127):
            helder +=1

helderpercentage = (helder / (rows*cols) )* 100
print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%% Opgave 4 a

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder = 0
drempelwaarde = int (input("Voor maximum waarde voor helderheid in: "))
for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        image[i,j] = k + drempelwaarde #(k // 32) * 32
        if(image[i,j] > 127):
            helder +=1

helderpercentage = (helder / (rows*cols) )* 100
print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()




#%% Opgave 4 b

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder = 0
drempelwaarde = int (input("Voor maximum waarde voor helderheid in: "))
for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        image[i,j] = k * drempelwaarde #(k // 32) * 32
        if(image[i,j] > 255):
            helder +=1
            image[i,j] = 255

helderpercentage = (helder / (rows*cols) )* 100
print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()




#%% Opgave 4 c

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder = 0
drempelwaarde = int (input("Voor maximum waarde voor helderheid in: "))
for i in range(rows):
    for j in range(cols):
        k = image[i,j]
        image[i,j] = k * drempelwaarde #(k // 32) * 32
        if(image[i,j] > 255):
            helder +=1
            image[i,j] = 255

helderpercentage = (helder / (rows*cols) )* 100
print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)



cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()




#%% Opgave 5

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)
#mg = cv2.resize(image, (800, 600)) 

rows,cols = image.shape[:2]
helder = 0
#drempelwaarde = int (input("Voor maximum waarde voor helderheid in: "))
for i in range(rows):
    for j in range(cols):
        #k = image[i,j]
        #image[i,j] = k * drempelwaarde #(k // 32) * 32
        if(image[i,j] > 200):
            helder +=1
            image[i,j] = 200
        elif(image[i,j] < 30):
            image[i,j] = 30

helderpercentage = (helder / (rows*cols) )* 100
print(image.shape)  #print de helderheid van de afbeelding


print(np.average(image))
print(helderpercentage)


cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Kroatie_grijs_aangepast.jpg',image)




#%% Opgave 6

import numpy as np
import cv2

# Lees een foto in (grijswaarden)
image = cv2.imread('Kroatie_grijs.jpg', 0)

rows,cols = image.shape[:2]
#drempelwaarde = int (input("Voer drempelwaarde voor helderheid in: "))

aantal_Pixels_boven_grenswaarde = np.sum(image == 0 )

print ("Aantal Pixels boven Grenswaarde", aantal_Pixels_boven_grenswaarde)

for i in range(rows):
    for j in range(cols):
        if(image[i,j] > 200):
            image[i,j] = 0

Controle_aantal_Pixels_boven_grenswaarde = np.sum(image == 0 )
print ("Aantal Pixels boven Grenswaarde", Controle_aantal_Pixels_boven_grenswaarde)


cv2.imshow('plaatje',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Kroatie_grijs_aangepast.jpg',image)




# %%

