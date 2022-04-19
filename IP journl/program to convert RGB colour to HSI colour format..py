import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
img=cv2.imread('C:/Users/sahil/OneDrive - 834sys/Documents/Python Scripts/apple1.jpg')
img_col=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
row,col,p=img_col.shape
hsi_img = img_col.copy()
R,G,B= cv2.split(img_col)
[R,G,B] = [ i/255.0 for i in ([R,G,B])]
H = np.zeros((row, col))
I = (R + G + B) / 3.0
S = np.zeros((row,col))
for i in range(row):
    den = np.sqrt((R[i]-G[i])**2+(R[i]-B[i])*(G[i]-B[i]))
    thetha = np.arccos(0.5*(R[i]-B[i]+R[i]-G[i])/den)
    h = np.zeros(col)
    h[B[i]<=G[i]] = thetha[B[i]<=G[i]]
    h[G[i]<B[i]] = 2*np.pi-thetha[G[i]<B[i]]
    h[den == 0] = 0
    H[i] = h/(2*np.pi)
for i in range(row):
    min = []
    for j in range(col):
        arr = [B[i][j],G[i][j],R[i][j]]
        min.append(np.min(arr))
    min = np.array(min)
    S[i] = 1 - min*3/(R[i]+B[i]+G[i])
    S[i][R[i]+B[i]+G[i] == 0] = 0
hsi_img[:,:,0] = H*255
hsi_img[:,:,1] = S*255
hsi_img[:,:,2] = I*255
plt.figure(),
plt.subplot(121),plt.imshow(img_col),plt.title('Original Color image')
plt.axis('off')
plt.subplot(122),plt.imshow(hsi_img),plt.title('HSI image')
plt.axis('off')
plt.show()