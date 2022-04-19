import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
H1=(1/9)*np.ones((3,3))
H2=(1/25)*np.ones((5,5))
H3=(1/49)*np.ones((7,7))
Nimg1=cv2.filter2D(Img,-1,H1)
Nimg2=cv2.filter2D(Img,-1,H2)
Nimg3=cv2.filter2D(Img,-1,H3)
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Nimg1,cmap='gray'),plt.title('3x3 low pass filtered Image')
plt.axis('off')
plt.subplot(223),plt.imshow(Nimg2,cmap='gray'),plt.title('5x5 low pass filtered Image')
plt.axis('off')
plt.subplot(224),plt.imshow(Nimg3,cmap='gray'),plt.title('7x7 low pass filtered Image')
plt.axis('off')
plt.show()
