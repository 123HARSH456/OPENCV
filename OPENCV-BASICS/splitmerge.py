import cv2 as cv
import numpy as np
img = cv.imread('photos/woman.jpg')
cv.imshow('img', img)

#split
#they show pixel intensity
#areas darker have lesser intensity
b,g,r = cv.split(img)

#grayscale images basically
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

#grayscale images have shape of 1
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge
#we get back the merged image
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

#show actual color channel instead for grayscale img, we have to reconstruct the img
#we create a blank img using numpy
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blueC', blue)
cv.imshow('greenC', green)
cv.imshow('redC', red)


cv.waitKey(0)