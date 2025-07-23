import cv2 as cv
import numpy as np

#create blank img with numpy
blank = np.zeros((500,500,3), dtype='uint8') #uint8 is for img type
blank2 = np.zeros((500,500,3), dtype='uint8')
blank3 = np.zeros((500,500,3), dtype='uint8')
blank4 = np.zeros((500,500,3), dtype='uint8')
blank5 = np.zeros((500,500,3), dtype='uint8')

# 1. Paint img a certain color
#range of color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green_Partially', blank)

#fully green
blank[:] = 0,255,0
cv.imshow('Green', blank)


# 2. Draw a Rectangle
cv.rectangle(blank2, (0,0), (250,250), (0,255,0), thickness = 2) #args = img name, point 1 , point 2, color , thickness , linetype
cv.imshow('Rectangle1', blank2)
# thickness = cv.FILL for filling the shape

#fill it
cv.rectangle(blank2, (0,0), (250,250), (0,255,0), thickness = cv.FILLED) # thickness = cv.FILLED or -1 for filling the shape
cv.imshow('Rectangle2', blank2)

#using calcs
cv.rectangle(blank2, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)
cv.imshow('Rectangle3', blank2)

# 3. Draw a Circle
cv.circle(blank3, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=2) #args = img name, center, radius, color, thickness, linetype
cv.imshow('Circle', blank3)

# 4. Draw a line
cv.line(blank4, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = 3) #args = img name, point 1, point 2, color, thickness, linetype
cv.imshow('Line',blank4)   

# 5. Text on image
cv.putText(blank5, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #args = img name, text, origin, fontface, scale, color, thickness
cv.imshow('Text', blank5)

cv.waitKey(0)