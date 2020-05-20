#corners are the region in the image, with large variation in intensity in all the direction
import cv2
import numpy as np 

#using Shi Tomasi corner detector
#it gives better result compared to Harris. Also we can find top end corners (in case of we dont want to find all the corners in the image)
img = cv2.imread('pic1.png')
img = cv2.resize(img, (512, 512))           #if needed

cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
    #arg 1: input image 
    #arg 2: maxCorners - maximum number of corners to return (is more corners found than we asked for, then the strongest corners will returns)
    #arg 3: qualityLevel - minimul expected quality of the image corner
    #arg 4: minDistance - minimum possible eucleadian distance between the returned corners

corners = np.int0(corners)          #convert all the corners to int values

for i in corners:
    x, y = i.ravel()

    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)


cv2.imshow('Shi Tomasi', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()