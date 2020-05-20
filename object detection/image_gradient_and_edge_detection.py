#an image gradient is a directional change in the intensity or color in an image 
#we use image gradient inside the image to find the edges of the image
    #laplacian - calculates the laplacian derivatives
    #soble - joit gaussian and deferentiation

import cv2
import numpy as np 
from matplotlib import pyplot as plt  

# img = cv2.imread('../data/messi5.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

img = cv2.imread('../data/messi5.jpg', cv2.IMREAD_GRAYSCALE)       #same procedure from line 10 to 12
#img = cv2.imread('../data/sudoku.png', cv2.IMREAD_GRAYSCALE)

#Laplacian method
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
        #arg 1 : source
        #arg 2 : data type
        #arg 3 : kernel size
    #CV_64F - just a data type (64 bit float, with supports for the negative numbers)
lap = np.uint8(np.absolute(lap))

#sobel gradient representation (sobelx and sobely)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    #arg 1 : source
    #arg 2 : data type
    #arg 3 : dx - order of derivative x ( 1 means we are focusing on x direction)
    #arg 4 : dy - order of derivative y 
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    #arg 4 : dy  ( 1 means we are focusing on y direction)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#combining sobelX and sobelY
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

#canny edge detector
canny = cv2.Canny(img, 100, 200)        #this method removes more noise

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show() 