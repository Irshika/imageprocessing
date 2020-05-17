#canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
#the canny edge detection algorithm is composed of 5 steps
    #1 - Noise reduction
    #2 - Gradient calculation (find the intensity gradient of the image)
    #3 - Non-maximum suppression (to get rid off spherier response to edge detection)
    #4 - Double threshold (to determine the potential edges)
    #5 - Edge Tracking by Hysteresis

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

def nothing(x):
    print(x)

img = cv2.imread('messi5.jpg', 0)
cv2.namedWindow('image')

cv2.createTrackbar('TH1', 'image', 0, 255, nothing)
cv2.createTrackbar('TH2', 'image', 0, 255, nothing)

#if k = cv2.waitKey(1) & 0xFF

while(1):
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 

    TH1 = cv2.getTrackbarPos('TH1', 'image')
    TH2 = cv2.getTrackbarPos('TH2', 'image')

    canny = cv2.Canny(img, TH1, TH2)
    #arg 1 : source
    #arg 2 : threshold value 1 (for the histerisis procedure)
    #arg 3 : threshold value 2 (for the histerisis procedure)

    titles = ['image', 'canny']
    images = [img, canny]

    for i in range(2):
        plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

cv2.destroyAllWindows()
