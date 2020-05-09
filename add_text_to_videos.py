import cv2

capture = cv2.VideoCapture(0)

print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))            #associate number of WIDTH = 3
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))           #associate number of HEIGHT = 4

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)
#capture.set(3, 1208)           #same as above
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#capture.set(4, 720)            #same as above

print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(capture.get(3))              #same as above
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#print(capture.get(4))              #same as above

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()