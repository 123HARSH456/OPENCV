import cv2 as cv
import numpy as np
img = cv.imread('photos/woman.jpg')

cv.imshow('Woman', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) #translational matrix
    dimensions = (img.shape[1], img.shape[0]) #tuple of width and height
    return cv.warpAffine(img, transMat, dimensions)

# if negative x=> shift left
# if negative y => shift up
# if positive x => shift right
# if positive y => shift down

# Translate
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotate
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
        rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)

        return cv.warpAffine(img, rotMat, dimensions)
    
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)
# negative value to rotate clockwise

# Resizing
resized = cv.resize(img, (1000,1000), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) #flip code : 0 => vertically, 1 => horizontaly, -1 => flip both vertically and horizontally
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)