import cv2 as cv
import numpy as np
img = cv.imread('photos/woman.jpg')
cv.imshow('Woman', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# canny = cv.Canny(img, (125,175))
# cv.imshow('Canny', canny)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) #contours is a list of all coordinates

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours draw', blank)


cv.waitKey(0)