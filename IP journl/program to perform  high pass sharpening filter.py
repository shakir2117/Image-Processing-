import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0)
Hh=np.array([[1,1,1],[1,-8,1],[1,1,1]])
dst=cv2.filter2D(Img,-1,Hh)
plt.figure()
plt.subplot(121),plt.imshow(Img,cmap='gray'),plt.title('Original Gray Image')
plt.axis('off')
plt.subplot(122),plt.imshow(dst,cmap='gray'),plt.title('Sharpening Image')
plt.axis('off')
plt.show()
