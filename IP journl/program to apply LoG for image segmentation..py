import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
Img_G= cv2.GaussianBlur(Img,(5,5),0)
Img_L= cv2.Laplacian(Img_G,cv2.CV_64F)
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Img_G,cmap='gray'),plt.title('Gaussian Image')
plt.axis('off')
plt.subplot(223),plt.imshow(Img_L,cmap='gray'),plt.title('LoG Image')
plt.axis('off')
plt.show()
