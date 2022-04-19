import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
m,n,p=Img.shape
N_img=np.zeros((m,n,p))
for i in range(0,m):
 for j in range(0,n):
    for k in range(0,p):
        N_img[i,j,k]=1-Img[i,j,k]
plt.figure()
plt.subplot(121),plt.imshow(Img),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img),plt.title('CMYK Image')
plt.axis('off')
plt.show()