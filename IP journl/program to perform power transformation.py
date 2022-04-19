import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0)
m,n=Img.shape
C=float(input('Enter the vlue of constant : '))
gamma=float(input('Enter Gamma value : '))
Nimg=np.zeros((m,n),dtype=Img.dtype)
for i in range(0,m):
    for j in range(0,n):
        Nimg[i,j]=C*(Img[i,j]**gamma)
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Nimg,cmap='gray'),plt.title('Power Transformed Image')
plt.axis('off')
plt.show()
