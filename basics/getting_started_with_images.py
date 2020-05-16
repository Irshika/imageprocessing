import cv2

#read images
#image source "https://github.com/opencv/opencv/samples/data"
img = cv2.imread('lena.jpg', 1)            # read image from local dir
                                                # In here as the second argument is the flag, it states how the image should be read.
                                                # 	1 loads a color image
                                                # 	2 loads image in grayscale mode
                                                # 	3 loads image as such including alpha channel

print(img)                     
cv2.imshow('Lena',img)                 # shows img in a window
k = cv2.waitKey(0) & 0xFF         # waitKey(5000) - picture will hold 5 sec and then disappeir
                                  # 0xFF is a mask to do the same as waitkey()

if k == 27:                               #27 states the escape button
    cv2.destroyAllWindows()                   # destroyes all the windows that we have created
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)                 # after running above command lena_copy.png was created
    cv2.destroyAllWindows() 
        






