#image blending is a application of pyramids

#Image blending technique
    #1 - Load the two images
    #2 - Find the gaussian pyramids for the images
    #3 - From gaussian pyramids, find their laplacian pyramids
    #4 - Now join the left half of image 1 and right half of image 2 in each levels of laplacian pyramids
    #5 - Finally from this join image pyramids, reconstruct the original image

import cv2
import numpy as np 

#1 - loading two images
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:,  :256], orange[:, 256:]))
#we need to blend these two images, so we use image pyramid techniques

#2.1 - generate gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#2.2 - generate gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#3.1 - laplacian pyramid for apple
apple_copy = gp_apple[5]
#v2.imshow('upper level gaus pyramid for apple', apple_copy)
lap_apple = [apple_copy]

for i in range(5, 0, -1):
    gp_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gp_extended)
    lap_apple.append(laplacian)

#3.2 - laplacian pyramid for orange
orange_copy = gp_orange[5]
#cv2.imshow('upper level gaus pyramid for orange', orange_copy)
lap_orange = [orange_copy]

for i in range(5, 0, -1):
    gp_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gp_extended)
    lap_orange.append(laplacian)

#4 - join images 
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lap_apple, lap_orange):
    n += 1
    cols, rows, channels = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    

#5 - Reconstruction of the image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)
cv2.imshow('apple_orange', apple_orange)
# cv2.imshow('apple', apple)
# cv2.imshow('orange', orange)

cv2.waitKey(0)
cv2.destroyAllWindows()