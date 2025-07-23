import cv2 as cv

#READING IMAGES
img = cv.imread('photos/cat.jpg') #returns img as a matrix of pixels
cv.imshow('Cat', img) #displays the image as new window


#READING VIDEOS
capture = cv.VideoCapture(0) #0 = webcam, 1 = another camera, 2 = 2nd camera etc... put path if video not camera
#we use while loop to read frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) #keyboard binding function which waits for specific timing delay for key to be pressed (not imp)