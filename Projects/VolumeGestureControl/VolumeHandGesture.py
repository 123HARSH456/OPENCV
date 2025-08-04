import cv2 as cv
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
wCam, hCam = 1280, 720


cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0


detector = htm.handDetector(detectionConfidence=0.7)


#pycaw code


#Get the default audio playback device (speakers)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

#Get the volume range in decibels (e.g., -65.25 to 0.0)
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400


while True:
    success, img = cap.read()

    if not success:
        print("Failed to grab frame, skipping...")
        continue

    img = detector.findHands(img)

    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2


        cv.circle(img,(x1, y1), 15, (255,0,255), cv.FILLED)
        cv.circle(img,(x2, y2), 15, (255,0,255), cv.FILLED)
        cv.line(img, (x1, y1), (x2, y2), (255,0,255), 3)
        cv.circle(img,(cx, cy), 15, (255,0,255), cv.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)
        #max  = 250, min = 35
        #volume range -65 to 0
        #so we interpolate
        vol = np.interp(length, [35, 250], [minVol, maxVol])    
        volBar = np.interp(length, [35, 250], [400, 150]) 
        print(vol)
        #change master volume
        volume.SetMasterVolumeLevel(vol, None)




        if length < 35:
            cv.circle(img,(cx, cy), 15, (0,255,0), cv.FILLED)
        

        # #volume bar
        cv.rectangle(img, (50, 150), (85, 400), (0,255,0), 3)
        cv.rectangle(img, (50, int(volBar)), (85, 400), (0,255,0), cv.FILLED)



    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (40, 70), cv.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)

    cv.imshow('img', img)
    cv.waitKey(1)