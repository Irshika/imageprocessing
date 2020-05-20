#background substraction is a technique for generating the foreground mask (binary image containing the pixels belonging to the moving object of a scene, when capture with a static camera)
#
import cv2
import numpy as np 
#for example
# img = cv2.imread('backsub.png')
# cv2.imshow('Example', img)

cap = cv2.VideoCapture('../data/vtest.avi')

#create a background object (fgbg - forground object)
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)         #gaussiann mixture based background and forground segmentation algorithm
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)

#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG() 
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() 
    #if "AttributeError: module 'cv2.cv2' has no attribute 'bgsegm' error occurs, install contrib dependency for python opencv
    #pip install opencv-contrib-python

#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))           #if uses createBackgroundSubstractorGMG()

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)               # (fgmask - forground mask object)
    #to remove the noises we need to do morphological operarions
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)          #if uses createBackgroundSubstractorGMG()

    cv2.imshow('rrame', frame)
    cv2.imshow('forground mask frame', fgmask)    

    k = cv2.waitKey(30)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()