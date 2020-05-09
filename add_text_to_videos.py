import cv2
import datetime

capture = cv2.VideoCapture(0)

# print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))            #associate number of WIDTH = 3
# print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))           #associate number of HEIGHT = 4

# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# #capture.set(3, 1208)           #same as above

# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# #capture.set(4, 720)            #same as above

# print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# #print(capture.get(3))              #same as above

# print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #print(capture.get(4))              #same as above

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height: ' + str(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, date_time,(10, 50), font, 1, (0,255,255), 2, cv2.LINE_AA )
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()