#morphological transformations are some simple operations based on the image shape
#mainly two things
    #1. original image
    #2. structuring elements (kernel)

#kernel - A Kernel tells us how to change the value of any given pixel by combining it with different amounts of the neighboring pixels.

import cv2
import numpy as np 
from matplotlib import pyplot as plt  

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

titles = ['image']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()