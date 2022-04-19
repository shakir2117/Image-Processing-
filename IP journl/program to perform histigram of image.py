import cv2
import matplotlib.pyplot as plt
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(222),plt.hist(Img.flatten(),256,[0,256],color='r'),plt.title('Histogram Image')
plt.axis('on')
plt.show()
