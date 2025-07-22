import cv2 as cv

img = cv.imread('photos/woman.jpg')
cv.imshow('img', img)

#Averaging
#we define a kernel window which will compute middle pixel intensity based on surrounding pixels
average = cv.blur(img, (3,3)) #higher the kernel size more the blur
cv.imshow('avg', average)

#Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian_blur', gaussian_blur)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#Bilateral Blur
#retains edges as well
bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)