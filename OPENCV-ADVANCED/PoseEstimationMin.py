import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose() 
#parameterss:
#   static mode: default false
#   upper body only: default false
#   smooth landmarks: default true
#   detection confidence: default 0.5
#   tracking confidence: default 0.5


cTime = 0
pTime = 0
cap = cv.VideoCapture(0)


while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)



        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)






    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (50,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    cv.imshow('Img', img)

    cv.waitKey(1)

