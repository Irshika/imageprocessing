import cv2
import numpy as np 

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (250,0), (500, 250), (255, 255, 255), -1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

k = cv2.waitKey(0) & 0xFF
if k == 27 |ord('q'):
    cv2.destroyAllWindows()