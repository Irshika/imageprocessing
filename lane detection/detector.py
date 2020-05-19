import matplotlib.pylab as plt 
import cv2
import numpy as np 

image = cv2.imread('road.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#define the region of interest (roi)
print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height), 
    (width/2 , height/2),
    (width, height)
]

#function to mask every other things other than our roi
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)          
    channel_count = img.shape[2]        #get number of color channels
    match_mask_color = (255,) * channel_count            #create a match color as the same as channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)            #polygon 
    masked_image = cv2.bitwise_and(img, mask)            #return the image only where the mask pixels matches
    return masked_image

image_after_masking = region_of_interest(image, 
                        np.array([region_of_interest_vertices], np.int32))


plt.imshow(image_after_masking)
plt.show()
