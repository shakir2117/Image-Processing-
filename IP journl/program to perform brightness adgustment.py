import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif')
Img_Gray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
m,n=Img_Gray.shape
print(Img_Gray.shape)
k=int(input('Enter the brightness factor'))
N_img=np.zeros((m,n),dtype=Img.dtype)
for x in range(0,m):
    for y in range(0,n):
        N_img[x,y]=Img_Gray[x,y]+k
        if N_img[x,y]>=255:
            N_img[x,y]=255
plt.figure()
plt.subplot(121),plt.imshow(Img_Gray,cmap='gray'),plt.title('Original Gray Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img,cmap='gray'),plt.title('Bright Image')
plt.axis('off')
plt.show()