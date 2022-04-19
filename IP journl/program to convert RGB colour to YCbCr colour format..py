import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
m,n,p=Img.shape
YCBCR=np.zeros((m,n,p),dtype=Img.dtype)
for i in range(0,m):
    for j in range (0,n):
        YCBCR[i,j,0]=16+(65.481*Img[i,j,0]+128.553*Img[i,j,1]+24.966*Img[i,j,2])/255
        YCBCR[i,j,2]=128+(112.00*Img[i,j,0]-93.786*Img[i,j,1]-18.214*Img[i,j,2])/255
        YCBCR[i,j,0]=16+(65.481*Img[i,j,0]+128.553*Img[i,j,1]+24.966*Img[i,j,2])/255
plt.figure()
plt.subplot(121),plt.imshow(Img),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(YCBCR),plt.title('YCBCR Image')
plt.axis('off')
plt.show()
