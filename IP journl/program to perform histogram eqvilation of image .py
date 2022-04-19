import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
Img_equ= cv2.equalizeHist(Img)
plt.figure(),
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.hist(Img.flatten(),256,[0,256],color='r'),plt.title('Original Image Histogram')
plt.subplot(223),plt.imshow(Img_equ,cmap='gray'),plt.title('Histogram Equalized Image')
plt.axis('off')
plt.subplot(224),plt.hist(Img_equ.flatten(),256,[0,256],color='r'),plt.title('Histogram of Histogram Equalized Image')
plt.show()
