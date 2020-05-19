import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('face-demographics-walking.mp4')

while (cap.isOpened()):
    _ , img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)            
    #faces = cv2.CascadeClassifier.detectMultiScale(gray, 1.1, 4)            #detect the faces inside the image
        #faces - Vector of rectangles where each rectangle contains the detected object, the rectangles may be partially outside the original image 
        #arg 1: Image - Matrix of the type CV_8U containing an image where objects are detected.
        #arg 1: ScaleFactor - Parameter specifying how much the image size is reduced at each image scale.
        #arg 1: minNeighbors - Parameter specifying how many neighbors each candidate rectangle should have to retain it.

    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x,y), (x+width, y+height), (0, 255, 0), 3)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()