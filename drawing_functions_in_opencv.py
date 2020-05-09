import numpy as np 
import cv2

img = cv2.imread('lena.jpg',1)

# modify to the img
#img = cv2.line(img, (100, 100), (400, 100), (135,156,30), 5)       #arg 1 : the source
                                                            #arg 2, 3 : the starting coordinates, ending cordinates
                                                            #arg 4 : the color (BGR)
                                                            # arg 5 : thickness
#img = cv2.arrowedLine(img, (100, 100), (400, 100), (135,156,30), 5)

img = cv2.rectangle(img,(384,0), (510,128), (0,0,255), 5 )
#arg 1 : source
#arg 2 : Left upper coordinates
#arg 3 : Right bottom coordinates
#arg 4 : Color
#arg 5 : Thickness ** if -1 - fills the rectangle

img = cv2.circle(img, (447, 63), 63, (255,0,0), 5)
#arg 1 : Source
#arg 2 : Centre
#arg 3 : radius
#arg 4 : Color
#arg 5 : Thickness

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'Lena', (10, 500), font, 4, (135,156,30), 10,cv2.LINE_AA )
#arg 1 : Source
#arg 2 : Text
#arg 3 : Starting point
#arg 4 : Font
#arg 5 : Font size
#arg 6 : Color
#arg 7 : Thickness
#arg 8 : Line types

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()