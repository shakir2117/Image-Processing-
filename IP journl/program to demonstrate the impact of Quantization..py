import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image
import PIL
Img=Image.open('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg')
Img1=Img.quantize(1)
Img2=Img.quantize(2)
Img3=Img.quantize(4)
Img4=Img.quantize(8)
plt.figure()
plt.subplot(231),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(232),plt.imshow(Img1,cmap='gray'),plt.title('1 Quantized Image')
plt.axis('off')
plt.subplot(233),plt.imshow(Img2,cmap='gray'),plt.title('2 Quantized Image')
plt.axis('off')
plt.subplot(234),plt.imshow(Img3,cmap='gray'),plt.title('4 Quantized Image')
plt.axis('off')
plt.subplot(235),plt.imshow(Img4,cmap='gray'),plt.title('8 Quantized Image')
plt.axis('off')
plt.show()
