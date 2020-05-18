import cv2 
import numpy as np 

img = cv2.imread('messi5.jpg')
print(img.shape)

img_crop = img[90:135, 220:260]

cv2.imshow('Image', img)
cv2.imshow('messi face', img_crop)
           
k = cv2.waitKey(0) & 0xFF                                           
if k == 27:                               
    cv2.destroyAllWindows()                   
elif k == ord('s'):
    cv2.imwrite('messi_face.jpg', img_crop)               
    cv2.destroyAllWindows() 
        