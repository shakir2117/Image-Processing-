import cv2
import matplotlib.pyplot as plt
import numpy as np
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
m,n,p=Img.shape
r,g,b =cv2.split(Img)
Hh=np.array([[1,1,1],[1,-8,1],[1,1,1]])
r1=cv2.filter2D(r,-1,Hh)
g1=cv2.filter2D(g,-1,Hh)
b1=cv2.filter2D(b,-1,Hh)
Img_mer=cv2.merge([r1,g1,b1])
plt.figure()
plt.subplot(121),plt.imshow(Img),plt.title('Original Image')
plt.axis('off')
plt.subplot(122),plt.imshow(Img_mer),plt.title('Sharpen Color Image')
plt.axis('off')
plt.show()
