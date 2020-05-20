#uses of histograms -
    #can tell you whether or not the image has been properly exposed
    #identify the lighting conditions
    #can used to make adjestments

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../data/lena.jpg', 0)
#img = np.zeros((200, 200), np.uint8)
#cv2.rectangle(img, (0, 100), (200, 200), (255, 255, 255), -1)
#cv2.rectangle(img, (0, 50), (100, 100), (127, 127, 127), -1)

#b, g, r = cv2.split(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# cv2.imshow('img', img)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.xlabel('Intensity level')
# plt.ylabel('Total number of pixels')
    #arg1 : source
    #arg2 : maximum number of pixel values
    #arg3 : range
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()