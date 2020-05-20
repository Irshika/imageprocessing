# #object tracking is the process of locating a moving object over time.
# #camShift - continously adoptive meanShirt
# #camShift applies meanShift first, and the once the meanShift converges it update the size of the windows
# #also it calculates the orientation of the best fitting eclipse to it

# import cv2
# import numpy as np 

# cap = cv2.VideoCapture('../data/vtest.avi')
# #Step 1 - take first frame of the video
# ret, frame = cap.read()             #first frame



# #--------------- finding the initial location of a object ---------------------------
# # print(frame.shape)

# # frame = cv2.rectangle(frame, (490, 150), (540, 240), (0, 255, 0), 2)
# # cv2.imshow('frame', frame)

# # if cv2.waitKey(0) & 0xFF == 27:
# #     cv2.destroyAllWindows()
# #--------------------------------- END ----------------------------------------------



# #Step 2 - setup initial location of window
# x, y , width, height = 490, 150, 60, 90 
# track_window = (x, y, width, height)


# #Step 3 - set up the ROI for tracking
# #this steps finally gives the histogram back-projected image
# roi = frame[y:y+height, x:x+width]
# hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))         #why inRange() ?  because histogram only hue is considerd as hsv, also to avoid false values due to low light or low light value
# roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)         #normalize the hist


# #Step 4 - set up the termination criteria, either 10 iteration or move by atleast 1 pt
# term_criteria = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)
# cv2.imshow('roi', roi)
# while(1):
#     ret, frame = cap.read()
#     if ret == True:
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)         #calculating the back-projection
#         ret, track_window = cv2.CamShift(dst, track_window, term_criteria)            #apply the mean shift to get the new location
#         #print(ret)         #return x, y (width, height, rotation)

# #So in camShift we can also rotate our rectangle acording to our object size

#         #Draw it on image
#         pts = cv2.boxPoints(ret)            #draw rectangle which can rotate
#         print(pts)          #in order to use pts we need to convert it to int
#         pts = np.int0(pts)
#         final_image = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

#         #we cannot use the rectangle() function to draw rotating rectangle
#         # x, y, w, h = track_window
#         # final_image = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
#         cv2.imshow('dst', dst)
#         cv2.imshow('final', final_image)
        
#         if cv2.waitKey(30) & 0xFF == 27:
#             break
#     else:
#         break
