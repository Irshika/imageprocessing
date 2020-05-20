#background substraction is a technique for generating the foreground mask (binary image containing the pixels belonging to the moving object of a scene, when capture with a static camera)
#
import cv2
import numpy as np 
#for example
# img = cv2.imread('backsub.png')
# cv2.imshow('Example', img)

cap = cv2.VideoCapture('../data/vtest.avi')

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    cv2.imshow('Frame', frame)

    k = cv2.waitKey(30)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()