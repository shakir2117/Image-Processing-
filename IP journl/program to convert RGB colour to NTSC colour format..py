import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
m,n,p=Img.shape
YIQ=np.zeros((m,n,p),dtype=Img.dtype)
for i in range(0,m):
 for j in range(0,n):
    YIQ[i,j,0]=0.299*Img[i,j,0]+0.587*Img[i,j,1]+0.114*Img[i,j,2]
    YIQ[i,j,1]=0.596*Img[i,j,0]-0.274*Img[i,j,1]-0.322*Img[i,j,2]
    YIQ[i,j,2]=0.211*Img[i,j,0]-0.523*Img[i,j,1]+0.312*Img[i,j,2]
plt.figure()
plt.subplot(121),plt.imshow(Img),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(YIQ),plt.title('NTSC Image')
plt.axis('off')
plt.show()