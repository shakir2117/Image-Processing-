import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0)
m,n=Img.shape
N_img=np.zeros((m,n))
T=int(input('Enter the threshold value'))
for x in range(0,m):
 for y in range(0,n):
    if Img[x,y]>=T:
     N_img[x,y]=255
 else:
    N_img[x,y]=0
plt.figure(),
plt.subplot(121),plt.imshow(Img),plt.title('Original Gray Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img),plt.title('Threshold Image')
plt.axis('off')
plt.show()
