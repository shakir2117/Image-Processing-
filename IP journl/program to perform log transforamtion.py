import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0)
m,n=Img.shape
C=float(input('Enter the constant : '))
N_img=np.zeros((m,n))
for x in range(0,m):
    for y in range(0,n):
        N_img[x,y]=C*math.log(1+Img[x,y])
plt.figure(),
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Gray Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img,cmap='gray'),plt.title('Log Image')
plt.axis('off')
plt.show()
