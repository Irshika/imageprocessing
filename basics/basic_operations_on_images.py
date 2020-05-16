import cv2
import numpy as np 

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')


#------------------------- edit this for full functioning image handler ------------------------------------

# def click_event(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDOWN:

#         cv2.circle(img, (x, y), 3, (0,0,255), -1)
     
#         points.append((x, y))    
#         if len(points) >=2:
#             cv2.line(img, points[-1], points[-2], (255, 255, 255), 5)
#             print("X = %d", "Y = %d", x, y)
        
#         # cv2.imshow('Color picker', mycolorImage)

# #img = cv2.imread('.jpg')
# cv2.imshow('Image', img)

# points = []

# cv2.setMouseCallback('Image', click_event)

#----------------------------------- end ---------------------------------------------

print(img.shape)            #returns a tuple of number of rows, columns, and channels
print(img.size)             #returns Total number of pixels is accessed
print(img.dtype)            #returns Image datatype is obtained
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#resize images
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#for merging two or more images, they must be same size : Just add two images
#dst = cv2.add(img, img2)

#addWeighted : mentioning weights
dst = cv2.addWeighted(img, 0.2,img2, 0.8, 0)
    #arg1 : array element 1
    #arg2 : weight of the first array element
    #arg3 : array element 2
    #arg4 : weight of the secong array element
    #arg5 : scalar added 
    #arg 6: output array

    # dst = (source1 * alpha) + (source2 * beta) + gamma

cv2.imshow('Image', dst)

k = cv2.waitKey(0) & 0xFF
if k == 27 | ord('q'):
    cv2.destroyAllWindows() 


