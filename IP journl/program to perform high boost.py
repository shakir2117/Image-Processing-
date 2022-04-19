import cv2
import matplotlib.pyplot as plt
import numpy as np 
Img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/nature.jpg',0) 
M,N=Img.shape 
D=np.zeros((M,N)) 
H=np.zeros((M,N)) 
A=1.5 
Do=int(input("Enter the cut-off frequency: "))
for x in range(0,M):
    for y in range(0,N): 
        D[x,y]=((x-(M/2))**2+(y-(N/2))**2)**0.5
for x in range(0,M):
    for y in range(0,N):
        if D[x,y]<= Do:
            H[x,y]=0
        else: 
            H[x,y]=1 
Hb=(A-1)+H 
f=np.fft.fft2(Img)
fshift=np.fft.fftshift(f) 
O_img=fshift*Hb
mag_s=20*np.log(np.abs(fshift))
f_ishift=np.fft.ifftshift(O_img)
img_back=np.fft.ifft2(f_ishift)
img_back=np.abs(img_back) 
plt.figure()
plt.subplot(221),plt.imshow(Img,cmap="gray"),plt.title('Original image')
plt.axis('off')
plt.subplot(222),plt.imshow(Hb,cmap="gray"),plt.title('High Boost mask')
plt.subplot(223),plt.imshow(img_back,cmap="gray"),plt.title('High Boost Filtered image')
plt.subplot(224),plt.imshow(mag_s,cmap="gray"),plt.title('FFT Image')
plt.show()
