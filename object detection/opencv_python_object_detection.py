import cv2
import numpy as np 

def nothing(x):
    pass

cv2.namedWindow("Tracking")

while True:
    frame = cv2.imread('smarties.png')

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
