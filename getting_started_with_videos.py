import cv2

#capture = cv2.VideoCapture('myfile.avi')      # read from file
capture = cv2.VideoCapture(0)        # index of the camera. by default either 0 or -1

while(True):
    ret, frame = capture.read()                # ret - is there video is available(True or false will be saved)
                                               # frame - frame will be saved / capture the frame

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
capture.release()
cv2.destroyAllWindows()