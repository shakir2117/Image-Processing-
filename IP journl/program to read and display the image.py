import cv2
import matplotlib.pyplot as plt
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
Img_RGB=cv2.cvtColor(Img,cv2.COLOR_BGR2RGB)
Img_Gray=cv2.cvtColor(Img,cv2.COLOR_BGR2GRAY)
plt.figure(),
plt.subplot(221),plt.imshow(Img),plt.title('BGR Image')
plt.axis('off')
plt.subplot(222),plt.imshow(Img_RGB),plt.title('RGB Image')
plt.axis('off')
plt.subplot(223),plt.imshow(Img_Gray),plt.title('GRAY Image')
plt.axis('off')
plt.show()