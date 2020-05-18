#probabilistic hough line transform is a extended version on hough line transform

#------------------------ !Enhance the functionality later ----------------------------------

import cv2
import numpy as np 

# img = cv2.imread('sudoku.png')
# img = cv2.imread('road1.jpg')
# img = cv2.imread('road2.jpg')
# img = cv2.imread('road3.jpg')
img = cv2.imread('road4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
 
cv2.imshow('edges', edges)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    #arg 1: source
    #arg 2: rho - Distance resolution of the accumulator in pixels
    #arg 3: theta - Angle resolution of the accumulator in radians
    #arg 4: Threshold - Accumulator threshold parameter. Only those lines are returned that get enough votes (>threshold)
    #arg 5: minLineLength - Minimum length of line. Line segments shorter than this are rejected
    #arg 6: maxLineGap - Maximum allowed gap between line segments to treat them as a single line

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image', img)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
