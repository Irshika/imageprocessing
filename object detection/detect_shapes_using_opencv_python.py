import cv2
import numpy as np 

img = cv2.imread('../data/shapes.jpg')            #read image
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)          #convert to grayscale
_, thresh = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY)            #find threshold
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)            #find contours

#iterate through all the contours
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)           #approxPloyDP() - approximates polygonal curves with a specific position
        #arg 1: contour
        #arg 2: epsilion - approximation accuracy   |    arclength() - calculates contour parameter or a curve length
        #arg 3: opened or closed
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)            #draw contour
    #print out the shape
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 7       #aligning the text position

    #based on the number of polygonal curves we can approximate which shape it can be          
    if len(approx) == 3:
        cv2.putText(img, "Trangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1 , y1, width, heigth = cv2.boundingRect(approx)
        aspect_ratio = float(width)/heigth
        if aspect_ratio <=1.05 and aspect_ratio >= 0.95:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()