import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img = cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
kernel = np.ones((5,5),np.uint8)
Img_E= cv2.erode(Img,kernel,iterations=1)
Img_Boun=Img-Img_E
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_Boun,cmap='gray'),plt.title('Boundary Image')
plt.axis('off')
plt.show()