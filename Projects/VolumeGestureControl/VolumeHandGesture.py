import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm
wCam, hCam = 1280, 720


cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


detector = htm.HandDetector()

while True:
    success, img = cap.read()

    img = detector.findHands(img)





    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (40, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)

    cv.imshow('img', img)
    cv.waitKey(1)