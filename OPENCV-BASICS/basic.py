import cv2 as cv

img = cv.imread('photos/woman.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #to blur more increase the 2nd param num, should be odd always
cv.imshow('Blur', blur)

# Edge Cascade
cany = cv.Canny(img, 125, 175)
cv.imshow('Canny', cany)

# Dilating the img
dilated = cv.dilate(cany, (3,3), iterations = 1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_AREA) #ignores aspect ratio so interpolation is important (linear is faster cubic is slower but better)
cv.imshow('Resized', resized)

# Cropping
#images are array so we can slice em
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)