#template matching is the method of searching and finding the location of a template image inside a larger image
import cv2
import numpy as np 

img = cv2.imread('../data/messi5.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('../data/messi_face.jpg', 0)

w, h = template.shape[::-1]         #(-1) getting column value and row value in reverse order


res = cv2.matchTemplate(img_gray, template, cv2.TM_CCORR_NORMED)
#print(res)         #by observing this we need to find brightest value
threshold = 0.99        #increase the threshold value to find out actual brightest point (this will find out when loc has only one element en each arrays it will returns)
loc = np.where(res >= threshold)
print(loc)
#then declare a rectangel with same size as template width and height

#iterate in case of there are more than one matching area
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)


cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()