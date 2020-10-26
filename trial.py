import cv2
import numpy as np
by=int(input('Size you want to inc'))
print(by)
img=cv2.imread('img.jpg')

[l,b,cs]=np.shape(img)
# print(l,b)
inc_img=np.zeros((l*by,b*by,cs),dtype=np.int16)
# print(np.shape(inc_img))
for i in range(0,l):
    for j in range(0,b):
        inc_img[(by*i):(by*(i+1)),(by*j):(by*(j+1)),:]=img[i,j,:]

inc_img=inc_img/255.0

cv2.imshow('gg',img)
cv2.imshow('gg_inc',inc_img)
cv2.waitKey(0)
cv2.destroyAllWindows()