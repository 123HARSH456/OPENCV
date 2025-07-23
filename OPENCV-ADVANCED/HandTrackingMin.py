import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0); #capture webcam

mpHands = mp.solutions.hands
hands = mpHands.Hands()
#parameters: 
    # static mode -> keep detecting again again default false
    # max hands -> default 2
    # detection confidence -> default 50%
    # tracking confidence -> default 50%

#used to draw 21 points on hands
mpDraw = mp.solutions.drawing_utils

#for fps calculation
pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    #first convert img to rgb from bgr
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    #hands object will process our rgb img into result object
    results = hands.process(imgRGB)

    #to detect if multiple hands detected or not
    print(results.multi_hand_landmarks)

    #we need to extract multiple hands if present
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #get id and landmark from the info
            for id, lm in enumerate(handLms.landmark):
                #this provides us with the ratio of the img x y z coordinates so we need to multiply the number with width and height to extract pixel values
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)


                #making index finger stand out 
                if id == 8:
                    cv.circle(img, (cx, cy), 15, (255,0,255), cv.FILLED)


            #method provided by mediapipe to draw these points (21 points on hands)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS) #draw on original img and use HAND_CONNECTIONS to draw the lines

    #for fps calculation
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #display fps on screen
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX, 3, (255,255,0), 3)

    #display
    cv.imshow("Image", img)
    cv.waitKey(1)