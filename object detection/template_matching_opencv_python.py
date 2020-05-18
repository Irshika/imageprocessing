#template matching is the method of searching and finding the location of a template image inside a larger image
import cv2
import numpy as np 

img = cv2.imread('messi5.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()