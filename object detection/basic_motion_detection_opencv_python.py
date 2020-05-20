import cv2
import numpy as np 

capture = cv2.VideoCapture('../data/vtest.avi')

ret, frame1 = capture.read()
ret, frame2 = capture.read()

while capture.isOpened():
    diff = cv2.absdiff(frame1, frame2)                           #absdiff() - finds the difference between frame1 and frame2
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)                       #then convert this difference to grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0)                           #blur the diff
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)                #find the threshold
    dilated = cv2.dilate(thresh, None, iterations=3)                       #dialate the thresholding image to fill in all the holes (this will helps us to find the better contours)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)              #find the contours
    
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)            #draw contours
    
    #draw rectangles replacing contours
    for contour in contours:
        (x, y, width, height) = cv2.boundingRect(contour)
        #we need to tell the program to not draw rectangles for small areas which are less than the area that we have given
        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+width, y+height), (0, 255, 0), 2)
        cv2.putText(frame1, "Status : {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    
    cv2.imshow('feed', frame1)

    frame1 = frame2            #assign the value inside frame2 to frame1

    ret, frame2 = capture.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
capture.release()