import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
kernel = np.ones((5,5),np.uint8)
Img_E= cv2.erode(Img,kernel)
Img_D= cv2.dilate(Img,kernel)
Img_Op=cv2.dilate(Img_E,kernel)
Img_Cl=cv2.erode(Img_E,kernel)
Img_Top=Img-Img_Op
Img_Bott=Img_Cl-Img
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Img_Top,cmap='gray'),plt.title('Top Hat Image')
plt.axis('off')
plt.subplot(223),plt.imshow(Img_Bott,cmap='gray'),plt.title('Bottom Hat Image')
plt.axis('off')
plt.show()
