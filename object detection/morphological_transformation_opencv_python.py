#morphological transformations are some simple operations based on the image shape
#mainly two things
    #1. original image
    #2. structuring elements (kernel)

#kernel - A Kernel tells us how to change the value of any given pixel by combining it with different amounts of the neighboring pixels.
#basically we perform the morphological transformations on the binary images, therefore we introduce mask using thresholdings.
#if we are using a binary image there's no need to add a mask, just do the morphological transformation without using mask


import cv2
import numpy as np 
from matplotlib import pyplot as plt  

img = cv2.imread('../data/smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)           #bigger the rectangle, better the kernel result. but it affects the object size (increases)

dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)          #opening = erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)         #closing = dilation followed by erosion
morph_gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel, iterations=1)
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel, iterations=1)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morphological gradient', 'top hat']
images = [img, mask, dilation, erosion, opening, closing, morph_gradient, top_hat]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()