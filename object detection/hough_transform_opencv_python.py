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

# titles = ['Image 1', 'Image 2']
# images = [img1, img2]

# for i in range(2):
#     plt.subplot(1, 2, i+1), plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# plt.show() 

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#using hough transform we can express entire function (with x, y coordinates) in a single point (with m, c coordinates)