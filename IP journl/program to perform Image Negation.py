import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0)
m,n=Img.shape
N_img=np.zeros((m,n))
for x in range(0,m):
 for y in range(0,n):
    N_img[x,y]=255-Img[x,y]
plt.figure(),
plt.subplot(121),plt.imshow(Img),plt.title('Original Gray Image')
plt.axis('off')
plt.subplot(122),plt.imshow(N_img),plt.title('Negation Image')
plt.axis('off')
plt.show()