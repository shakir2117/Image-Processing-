import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
Img_canny= cv2.Canny(Img,100,200)
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_canny,cmap='gray'),plt.title('Canny Edge Image')
plt.axis('off')
plt.show()
