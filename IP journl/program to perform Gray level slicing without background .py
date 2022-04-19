import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
m,n=Img.shape
a=int(input('Enter the first threshold value:'))
b=int(input('Enter the second threshold value:'))
N_img=np.zeros((m,n))
for x in range(0,m):
 for y in range(0,n):
    if Img[x,y]>=a and Img[x,y]<=b:
        N_img[x,y]=255
    else:
        N_img[x,y]=0
plt.figure(),
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Gray image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img,cmap='gray'),plt.title('Gray Image without Background')
plt.axis('off')
plt.show()
