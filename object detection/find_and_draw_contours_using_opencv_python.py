#contours can be explained as curve joining all continous points along the path which are having the same color or density
#most used in object detection and object recognition

import cv2
import numpy as np 

img = cv2.imread('../data/opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)        #find the threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)        #find the contours
#contours is a python list of all the contours in the image. each individual contours ia a numpy array of (x,y) coordinates of boundary points of the object
#hierarchy is the optional output vector which is containing the information about image topology
print("Number of contours : " + str(len(contours)))
print(contours[0])          #each contours index contains the x and y coordinates of each contour

#now we can draw this contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    #arg 1: source
    #arg 2: contours array
    #arg 3: contour index (-1 means draw all the contours)
    #arg 4: color
    #arg 5: thickness

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()