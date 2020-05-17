#using image pyramids we works with images with different resolution
#using image pyramids we just create the images of different resolution and we search for the object
#pyramid, or pyramid representation is a type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling.
#there are two types of image pyramids
    #1 - Gaussian pyramid
            #1 - pyrDown (gives lower resolution)
            #2 - pyrUp (gives higher resolution)
    #2 - Laplacian pyramid
        #nothing but repeated blurring and subsampling of an image

import cv2
import numpy as np 

img = cv2.imread('lena.jpg')

# #gaussian pyramids
# #pyrDown() - gives 1/4 resolution of the source
# lower_res1 = cv2.pyrDown(img)  
# lower_res2 = cv2.pyrDown(lower_res1)

# #pyrUp() - gives 4* resolution of the source
# higher_res1 = cv2.pyrUp(lower_res2)

# #cv2.imshow("Original image", img)
# cv2.imshow("pyrDown 1 image", lower_res1)

# #cv2.imshow("pyrDown 2 image", lower_res2)
# cv2.imshow("pyrup 1 image", higher_res1)

# #After lowers the resolution with pyrDown image will loss some details, so if we again increases by the pyrUp, we will not get the same image as before. 
#     #compare pyrDown 1 image with pyrup 1 image

#create a pyramid of multiple resolution
layer = img.copy()
gaussian_pyr = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyr.append(layer)
    # cv2.imshow(str(i), layer)


#laplacian pyramids are formed on the gaussian pyramids
#no exclusive function for creating laplacian pyramids
#A level in laplacian pyramid is formed by the difference between that level in gaussian pyramid and expanded version of its upper level in gaussian pyramid

layer = gaussian_pyr[5]     #gets last image of gaussian pyramid
cv2.imshow('upper level Gaussian Pyramid', layer)
laplacian_pyr = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gaussian_pyr[i])          #extending the level of gaussian pyramid
    laplacian = cv2.subtract(gaussian_pyr[i-1], gaussian_extended)         #creating laplacian pyramid
    cv2.imshow(str(i), laplacian)       #its like a edge detector

#use of laplacian and gaussian pyramids,
    #helps us to blend the images and reconstruction of the images

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()