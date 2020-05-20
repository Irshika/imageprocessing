#corners are the region in the image, with large variation in intensity in all the direction
import cv2
import numpy as np 

#for more details - (https://aishack.in/tutorials/harris-corner-detector/)

#steps -

    #1 : determine which windows produce very large variations in intensity when moved in both x and y directions.
# img1 = cv2.imread('harris1.png')
# cv2.imshow('Step 1', img1)
    
    #2 : with each such window found, a score "R" is computed 
# img2 = cv2.imread('harris2.png')
# cv2.imshow('Step 2', img2)
        #lambda1, lambda2 are the eigen values of M

    #3 : after applying a threshold to this score, important corners are selected & marked
# img3 = cv2.imread('harris3.png')
# cv2.imshow('Step 3', img3)

            #1 - |R| is small, which happens when lambda1 and lambda2 are small, the refion is flat
            #2 - R < 0, which happens when lambda1 >> lambda2 or vice versa, the region is edge.
            #3 - R is large, which happens when lambda1 and lambda2 are large and lambda1 ~ lambda2, the refion is a corner

# we check original intensity with shifted intensity, the difference of those will be calculated. "this difference for a corner is VERY LAEGE"
#           thats how we detect corners 

#using harris corner detector
img = cv2.imread('pic1.png')
#img = cv2.imread('chessboard.png')
img = cv2.resize(img, (512, 512))           #if needed

cv2.imshow('Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)         #because cornerHarris() takes gray as float32, so we have to do the conversion
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    #arg 1: input image - it should be grayscale and float32 type
    #arg 2: blockSize - it is the size of neighbourhood considered for corner detection
    #arg 3: ksize - aperture parameter of Sobel derivative used
    #arg 4: k - harris detector free parameter in the equation

dst = cv2.dilate(dst, None)         #to get the better result we need to dilate

img[dst > 0.01 * dst.max()] = [0, 0, 255]           #returning to original image with optimal threshold value.

cv2.imshow('Harris', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()