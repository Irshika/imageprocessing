#Hough Transform basics
#the hough transform is a popular technique to detect any shape, if we can represent that shape in a mathematical form. it can detect the shape even if it is broken or distorted a little bit.
#A line in the image space can be expressed with two variables.
    #for example :
        #in the cartesian coordinate system - y = mx + c
        #in the polar coordinate system - xcos(theta) + ysin(theta) = r
#uncomment line 8 to 27 to get an insight,
# import cv2
# from matplotlib import pyplot as plt

# img1 = cv2.imread('hough_transformation1.jpg', -1)
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# img2 = cv2.imread('hough_transformation2.png')
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# img3 = cv2.imread('hough_transformation3.jpg')
# img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

# img4 = cv2.imread('polar_coordinates1.jpg')
# img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

# img5 = cv2.imread('polar_coordinates2.jpg')
# img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)

# img6 = cv2.imread('polar_coordinates3.jpg')
# img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)

# titles = ['Cartesian Coordinates', 'Polar Coordinates', 'Example 1 (Cartesian)', 'Example 2 (cartesian)', 'Example 3 (with one x,y coordinates/polar)', 'Example 4 (with multiple x,y coordinates/polar)']
# images = [img2, img4, img2, img3, img5, img6]

# for i in range(6):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.show() 

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#using hough transform we can express entire function (with x, y coordinates) in a single point (with m, c coordinates), vise-versa
#hough transform represents a line in form of a point in mc space(hough space)

#hough transformation algorithm
    #1 - Edge detection. eg: using the canny edge detector
    #2 - Mapping of edge points to the hough space and storage in an accumulator.
    #3 - Interpretation of the accumulator to yield lines of infinite length. the interpretation is done by thresholding and possibly other constraints.
    #4 - Conversion of infinite lines to finite lines.

#opencv implements two types of hough line transform methods
    #1 - The Standard Hough Transform (HoughLines method)
    #2 - The Probabilistic Hough Line (Transform HoughLinesP method)