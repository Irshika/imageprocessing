import cv2

capture = cv2.VideoCapture(0)        # index of the camera. by default either 0 or -1
#capture = cv2.VideoCapture('clip1.mp4')      # read from file

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))           # second arg is the 4cc code (4-bit code which is used to specify the video codecs)
                                               # source http://fourcc.org/codecs.php
#print(capture.isOpened())                    # checking isOpened() working or not
while(capture.isOpened()):             # check the video is open or not
    ret, frame = capture.read()                # ret - is there video is available(True or false will be saved)
                                               # frame - frame will be saved / capture the frame

    if ret == True:
        # getting the props
        # Video capture props source : https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        print(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        # print(capture.get(cv2.CAP_PROP_FPS))            
        # print(capture.get(cv2.CAP_PROP_FRAME_COUNT))

        out.write(frame)


        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)      # convert to grayscale
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord ('q'):
            break
    else:
        break

capture.release()                   # releasing the capture
out.release()
cv2.destroyAllWindows()
