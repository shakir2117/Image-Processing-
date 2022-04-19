import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
img=cv2.imread('C:/Users/Sahil/Downloads/rice.png',0)
pre_v=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
pre_h=np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
sob_v=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
sob_h=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img_vp=cv2.filter2D(img,-1,pre_v)
img_hp=cv2.filter2D(img,-1,pre_h)
img_vs=cv2.filter2D(img,-1,sob_v)
img_hs=cv2.filter2D(img,-1,sob_h)
plt.figure(),
plt.subplot(321),plt.imshow(img,cmap="gray"),plt.title('Original image')
plt.axis('off')
plt.subplot(322),plt.imshow(img_vs,cmap="gray"),plt.title('Sobel Vertical image')
plt.axis('off')
plt.subplot(323),plt.imshow(img_hs,cmap="gray"),plt.title('Sobel Horizontal image')
plt.axis('off')
plt.subplot(324),plt.imshow(img_vp,cmap="gray"),plt.title('Prewitt Vertical image')
plt.axis('off')
plt.subplot(325),plt.imshow(img_hp,cmap="gray"),plt.title('Prewitt Horizontal image')
plt.axis('off')
plt.show()
