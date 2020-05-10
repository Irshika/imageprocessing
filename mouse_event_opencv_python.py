import numpy as np 
import cv2

#list out all the events in cv2 package
events = [ i for i in dir(cv2) if 'EVENT' in i]
print(events)   
