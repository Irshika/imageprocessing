import cv2
import numpy as np 

def nothing(x):
    pass

capture = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)       #LH -> Lower Hue
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)       #LH -> Lower Saturation
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)       #LH -> Lower Value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)       #LH -> Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)       #LH -> Upper Saturation
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)       #LH -> Upper Value

while True:
    #frame = cv2.imread('smarties.png')
    _, frame = capture.read()

    #convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("LH", "Tracking")
    lower_s = cv2.getTrackbarPos("LS", "Tracking")
    lower_v = cv2.getTrackbarPos("LV", "Tracking")

    Upper_h = cv2.getTrackbarPos("UH", "Tracking")
    Upper_s = cv2.getTrackbarPos("US", "Tracking")
    Upper_v = cv2.getTrackbarPos("UV", "Tracking")

    lower_b = np.array([lower_h, lower_s, lower_v])       #lower limit for hsv blue color
    upper_b = np.array([Upper_h, Upper_s, Upper_v])     #upper limit for hsv blue color 

    #treshold the image and get only the blue color
    mask = cv2.inRange(hsv, lower_b, upper_b)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
