import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/balloon.jpg',0)
Img1=cv2.resize(Img,(360,480))
Img2=cv2.resize(Img,(580,580))
Img3=cv2.resize(Img,(420,1280))
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Img1,cmap='gray'),plt.title('Sample 1 Image')
plt.axis('off')
plt.subplot(223),plt.imshow(Img2,cmap='gray'),plt.title('Sample 2 Image')
plt.axis('off')
plt.subplot(224),plt.imshow(Img3,cmap='gray'),plt.title('Sample 3 Image')
plt.axis('off')
plt.show()
