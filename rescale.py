import cv2 as cv
img = cv.imread('photos/cat.jpg')
cv.imshow('Cat', img)

#works for images videos and webcams
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #frame.shape[1] = width
    height = int(frame.shape[0] * scale) #frame.shape[0] = height
    dimensions = (width,height) #tuple

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#works for only reading live video
def changeRes(width, height):
    capture.set(3, width) #3 stands for width
    capture.set(4, height) #4 stands for height


capture = cv.VideoCapture('photos/vid.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    #resized using function
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video_rescaled', frame_resized)



    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0) 