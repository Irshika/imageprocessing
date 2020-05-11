import numpy as np 
import cv2

#list out all the events in cv2 package
events = [ i for i in dir(cv2) if 'EVENT' in i]
#print(events)   

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
            #arg 1: source
            #arg 2: x and y coordinates
            #arg 3: radius
            #arg 4: color
            #arg 5: thickness
        points.append((x, y))    
        if len(points) >=2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
        cv2.imshow('Image', img)


# Showing the color channels
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y, x, 0]
    #         #arg 1 : y coordinate
    #         #arg 2 : x coordinate
    #         #arg 3 : channel
    #     green = img[y, x, 1]
    #     red = img[y, x, 2]

    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
    #     cv2.putText(img, strBGR, (x, y), font, 0.5, (255,255,0), 2)
    #     cv2.imshow('Image', img)
        

#img = cv2.imread('lena.jpg', 1)
img = np.zeros((512, 512 , 3),np.uint8)
cv2.imshow('Image', img)

points = []

cv2.setMouseCallback('Image', click_event)
#arg 1 : window name
#arg 2 : callback function 


k = cv2.waitKey(0) & 0xFF         
if k == 27 | k == ord('q'):                               
    cv2.destroyAllWindows()                   
