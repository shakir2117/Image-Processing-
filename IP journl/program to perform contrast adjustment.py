import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif')
Im=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
m,n=Im.shape
k=float(input('Enter Contrast factor: '))
Nim=np.zeros((m,n),dtype=Img.dtype)
for row in range(0,m):
    for col in range(0,n):
        Nim[row,col]=Im[row,col]*k
        if Nim[row,col]>=255:
            Nim[row,col]=255
plt.figure()
plt.subplot(221),plt.imshow(Im,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Nim,cmap='gray'),plt.title('Image after Contrast Adjustment')
plt.axis('off')
plt.show()