import cv2
import numpy as np 

img = cv2.imread('messi5.jpg')

print(img.shape)            #returns a tuple of number of rows, columns, and channels
print(img.size)             #returns Total number of pixels is accessed
print(img.dtype)            #returns Image datatype is obtained
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

cv2.imshow('Image', img)

k = cv2.waitKey(0) & 0xFF
if k == 27 | ord('q'):
    cv2.destroyAllWindows() 


