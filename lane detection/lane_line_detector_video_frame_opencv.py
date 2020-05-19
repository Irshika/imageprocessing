#steps -
    #1 - read image, find and define the roi
    #2 - image masking
    #3 - apply hough line transform
    #  
import matplotlib.pylab as plt 
import cv2
import numpy as np 

#function to mask every other things other than our roi
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)          
    #channel_count = img.shape[2]        #get number of color channels
    #match_mask_color = (255,) * channel_count            #create a match color as the same as channel_count
    match_mask_color = 255            #line 8, 9 removed because when we apply the canny edge detector to image before finding the roi, therefore no need of color channel count
    cv2.fillPoly(mask, vertices, match_mask_color)            #polygon 
    masked_image = cv2.bitwise_and(img, mask)            #return the image only where the mask pixels matches
    return masked_image

#draw line function
def draw_lines(img, lines):
    img = np.copy(img)          #copy image
    blank_image = np.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)            #create a blanked image with same size as original image
    #then loop aroun the line vector and draw lines
    #we need to draw lines in the blank image and merge with the original image
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)            #merge original image with blank image()
    return img


# image = cv2.imread('road.png')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def process(image):
    #define the region of interest (roi)
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
        (0, height), 
        (width/2 , height-height/4),
        (width, height)
    ]

    #find out the edges
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 200)

    image_after_masking = region_of_interest(canny_image,
                                            np.array([region_of_interest_vertices], np.int32),)


    #apply hough line transform
    lines = cv2.HoughLinesP(image_after_masking, 
                            rho=2, 
                            theta= np.pi/180, 
                            threshold=120, 
                            lines=np.array([]), 
                            minLineLength=5, 
                            maxLineGap=100)

    #then define a function to draw lines 
    if lines is None:
        image_with_lines = image
    else:
        image_with_lines = draw_lines(image, lines)
    return image_with_lines

capture = cv2.VideoCapture('clip1.mp4')

#check whether the video is available or not
while(capture.isOpened()):
    ret, frame = capture.read()
    #frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)             #if needed
    frame = process(frame)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


