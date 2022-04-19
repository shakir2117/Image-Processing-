import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
m,n,p=Img.shape
r,g,b =cv2.split(Img)
pln =np.zeros((m,n),dtype=Img.dtype)
Red=cv2.merge([r,pln,pln])
Green=cv2.merge([pln,g,pln])
Blue=cv2.merge([pln,pln,b])
plt.figure()
plt.subplot(221),plt.imshow(Img),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Red),plt.title('Red Channel')
plt.axis('off')
plt.subplot(223),plt.imshow(Green),plt.title('Green Channel')
plt.axis('off')
plt.subplot(224),plt.imshow(Blue),plt.title('Blue Channel')
plt.axis('off')
plt.show()
