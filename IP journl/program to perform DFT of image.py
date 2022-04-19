import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/cameraman.tif',0)
f=np.fft.fft2(Img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift))
f_ishift=np.fft.ifftshift(fshift)
img_back=np.fft.ifft2(f_ishift)
img_back=np.abs(img_back)
plt.figure(),
plt.subplot(231),plt.imshow(Img,cmap='gray'),plt.title('Original Image')
plt.axis('off')
plt.subplot(232),plt.imshow(np.abs(f),cmap='gray'),plt.title('FFT Image')
plt.axis('off')
plt.subplot(233),plt.imshow(np.abs(fshift),cmap='gray'),plt.title('Shifted FFT Image')
plt.axis('off')
plt.subplot(234),plt.imshow(magnitude_spectrum,cmap='gray'),plt.title('Magnitude FFT Image')
plt.axis('off')
plt.subplot(235),plt.imshow(img_back,cmap='gray'),plt.title('Inverse FFT Image')
plt.axis('off')
plt.show()
