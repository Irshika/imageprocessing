#detecting circles using hough circle transform
    # (x - x_center)^2 + (y - y_center)^2 = r^2
    # (x_center, y_center) is the center of the circle, and r is the radius of the circle
import cv2
import numpy as np

#img = cv2.imread('../data/smarties.png') 
img = cv2.imread('../data/shapes.jpg')
output = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, ksize=5)

#hough circle method
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    #arg 1: source - 8bit, single channel, grayscale input image
    #arg 2: method - detection method, see HoughModes.
    #arg 3: dp - Inverse ratio of the accumulator resolution to the image resolution
    #arg 4: minDist - Minimum distance between the centers of detected circles
    #arg 5: param1 - First method-specific parameter. in case of HOUGH_GRADIENT, it is the higher threshold of the two passed to the canny edge detector (the lower one is twice smaller)
    #arg 6: param2 - Second method-specific parameter. in case of HOUGH_GRADIENT, it is the accumulator threshold of for the circle centers at the detection stage.
    #arg 7: minRadius - Minimum circle radius
    #arg 8: maxRadius - Maximum circle radius, if <=0, uses the maximum image dimension. if <0, returns centers without finding the radius.

detectec_circles = np.uint16(np.around(circles))
for (x, y, r) in detectec_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)          #draw the center
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)

cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()