import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
kernel = np.ones((5,5),np.uint8)
Img_E=cv2.erode(Img,kernel)
Img_D=cv2.dilate(Img,kernel)
Img_Grad=Img_D-Img_E
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_Grad,cmap='gray'),plt.title('Morphological Gradient Image')
plt.axis('off')
plt.show()
