import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/woman.jpg')
cv.imshow('img', img)

plt.imshow(img) #originally bgr img
plt.show() #will be in rgb so inversed

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#we cant convert grayscale to hsv directly, so converting to bgr is very important

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsvtobgr', hsv_bgr)

#LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_HSV2BGR)
cv.imshow('labtobgr', lab_bgr)

cv.waitKey(0)