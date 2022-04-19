import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
m,n=Img.shape
N_img=np.zeros((m,n,3),dtype=Img.dtype)
for i in range(0,m):
    for j in range(0,n):
        if Img[i,j]>=0 and Img[i,j]<=100:
            N_img[i,j,0]=255
            N_img[i,j,1]=0
            N_img[i,j,2]=0
        elif Img[i,j]>100 and Img[i,j]<=200:
            N_img[i,j,0]=0
            N_img[i,j,1]=255
            N_img[i,j,2]=0
        else:
            N_img[i,j,0]=0
            N_img[i,j,1]=0
            N_img[i,j,2]=255
plt.figure()
plt.subplot(121),plt.imshow(Img ,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img),plt.title(' Psedo color Image')
plt.axis('off')
plt.show()