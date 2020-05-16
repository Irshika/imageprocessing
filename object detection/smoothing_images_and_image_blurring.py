#for smoothing and blurring images Homogeneous filters used more often. (easy and fast)
#Homogeneous filter, gaussian filter, median filter, bilateral filter, etc
#Homogeneous filter is the most simple filter, each output pixel is the mean of its kernel neighbors
#in image processing, a kernel convolution matrix, or mask is small matrix. it is used for blurring, sharpening, embossing, edge detection, and more

import cv2
import numpy as np 
from matplotlib import pyplot as plt  

img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)          #because matplotlib reads as RGB

kernel = np.ones((5, 5), np.float32)/ (5*5)             #kernel = ones(width, height) / (width * height)        #IMPORTANT
dst = cv2.filter2D(img, -1,kernel)

#As in one-dimensional signals, images also can be filtered with various low-pass filters(LPF, high-pass filters(HPF), etc
#LPF helps in removing noises, blurring the images.
#HPF helps in finding edges in the images.

blur = cv2.blur(img, (5,5))

#Gaussian filter is nothing but using different-weight-kernel, in both x and y directions
#pixels in the middle of the kernel has the higher weight, then the weight decreses with distance form the neighborhood center
#so the pixels located in the side have smaller weight, pixels located in the center has the higher weight

gblur = cv2.GaussianBlur(img, (5, 5), 0)

#Median filter is something that replace each pixel's value with the median of its neighboring pixels. This method is great when dealing with "salt and pepper noise"

median = cv2.medianBlur(img, 5)

#Homogeneos filter, gaussian filter and median filter will blur the images and smoothen the edges

#sometime we need to sharpening the edges

#bilateral filter is very usefull on noise removal while keeping edges sharp

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)
    #arg 1: source
    #arg 2: diameter of each pixel
    #arg 3: sigmaColor -> the filter sigma in the color space
    #arg 4: filter sigma in the coordinates space



titles = ['image', '2D Convolution', 'blur', 'Gaussian blur', 'median filter', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()