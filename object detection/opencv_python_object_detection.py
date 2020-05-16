import cv2
import numpy as np 

def nothing(x):
    pass

#cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread('smarties.png')

    #convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_b = np.array([110, 50, 50])       #lower limit for hsv blue color
    upper_b = np.array([130, 255, 255])     #upper limit for hsv blue color 

    #treshold the image and get only the blue color
    mask = cv2.inRange(hsv, lower_b, upper_b)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
