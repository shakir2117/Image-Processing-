import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
img_col=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
H1=np.ones((5,5),np.float32)/25
m,n,p=img_col.shape
r,g,b=cv2.split(img_col)
r1=cv2.filter2D(r,-1,H1)
g1=cv2.filter2D(g,-1,H1)
b1=cv2.filter2D(b,-1,H1)
Img_merg=cv2.merge([r1,g1,b1])
plt.figure(),
plt.subplot(121),plt.imshow(img_col),plt.title('Original image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_merg),plt.title('Smooth Color image')
plt.axis('off')
plt.show()
