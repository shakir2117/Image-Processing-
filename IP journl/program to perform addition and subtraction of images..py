import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
img1=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/black.jpg')
img2=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
img2=cv2.resize(img2,(400,400))
img1=cv2.resize(img1,(400,400))
print(img1.shape)
print(img2.shape)
img3=img1+img2
img4=img1-img2
plt.figure()
plt.subplot(221),plt.imshow(img1),plt.title('Original image 1')
plt.axis('off')
plt.subplot(222),plt.imshow(img2),plt.title('Original image 2')
plt.axis('off')
plt.subplot(223),plt.imshow(img3),plt.title('addition of 2 img')
plt.axis('off')
plt.subplot(224),plt.imshow(img4),plt.title('substraction of 2 img')
plt.axis('off')
plt.show()
