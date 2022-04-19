import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
kernel = np.ones((5,5),np.uint8)
D_img= cv2.dilate(Img,kernel)
E_img=cv2.erode(Img,kernel)
O_img=cv2.dilate(E_img,kernel)
C_img=cv2.erode(D_img,kernel)
plt.figure()
plt.subplot(321),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(322),plt.imshow(D_img,cmap='gray'),plt.title('Dilation Image')
plt.axis('off')
plt.subplot(323),plt.imshow(E_img,cmap='gray'),plt.title('Erosion Image')
plt.axis('off')
plt.subplot(324),plt.imshow(O_img,cmap='gray'),plt.title('Opening Image')
plt.axis('off')
plt.subplot(325),plt.imshow(C_img,cmap='gray'),plt.title('Closing Image')
plt.axis('off')
plt.show()