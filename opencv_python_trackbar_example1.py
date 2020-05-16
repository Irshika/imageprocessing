import cv2
import numpy as np 

#callback function when runnes createTrackbar()
def nothing(x):
    print(x)

img = np.zeros((300, 512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

# while(1):
#     cv2.imshow('image', img)
#     k = cv2.waitKey(0) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()

k = cv2.waitKey(0) & 0xFF
if k == 27 |ord('q'):
    cv2.destroyAllWindows()