import cv2

capture = cv2.VideoCapture('clip1.mp4')      # read from file
#capture = cv2.VideoCapture(0)        # index of the camera. by default either 0 or -1
#print(capture.isOpened())                    # checking isOpened() working or not
while(capture.isOpened()):             # check the video is open or not
    ret, frame = capture.read()                # ret - is there video is available(True or false will be saved)
                                               # frame - frame will be saved / capture the frame

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)      # convert to grayscale
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
capture.release()                   # releasing the capture
cv2.destroyAllWindows()