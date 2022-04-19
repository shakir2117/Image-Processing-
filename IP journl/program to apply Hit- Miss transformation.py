import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
kernel = np.ones((5,5),np.uint8)
Img_hit=cv2.morphologyEx(Img, cv2.MORPH_HITMISS, kernel)
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_hit,cmap='gray'),plt.title('Hit Miss Image')
plt.axis('off')
plt.show()
