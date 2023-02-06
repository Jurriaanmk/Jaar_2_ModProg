#%%
import cv2
# Lees een foto in (grijswaarden)
img = cv2.imread('Kroatie_grijs.jpg', 0)
opzoektabel = [0,1,1,1,2,3,3,4,6,7,8,9,11,12,13,15]
rows,cols = img.shape[:2]
for i in range(rows):
    for j in range(cols):
        oud = img[i,j] // 16
        nieuw = opzoektabel[oud]
        img[i,j] = nieuw * 16
cv2.imshow('plaatje',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
