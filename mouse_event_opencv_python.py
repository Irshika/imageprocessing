import numpy as np 
import cv2

#list out all the events in cv2 package
events = [ i for i in dir(cv2) if 'EVENT' in i]
#print(events)   

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ', ' + str(y)
        cv2.putText(img, strxy, (x, y), font, 1, (255,255,0), 2)
        cv2.imshow('Image', img)
        

img = np.zeros((512, 512 , 3),np.uint8)
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)
#arg 1 : window name
#arg 2 : callback function 

cv2.waitKey(0)
cv2.destroyAllWindows()