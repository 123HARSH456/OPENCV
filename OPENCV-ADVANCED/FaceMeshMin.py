import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh()
#parameters:
#   static mode false default
#   no of faces default 1
#   detection confidence default 0.5
#   tracking confidence default 0.5


drawSpecs = mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)


while True:
    success, img = cap.read()

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results =faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLandmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLandmarks, mpFaceMesh.FACEMESH_TESSELATION, drawSpecs, drawSpecs)

            #To display position of a point (Takes lot of resources as it prints position of 468 points)
            # for id, landmark in enumerate(faceLandmarks.landmark):
            #     ih, iw, ic = img.shape
            #     x, y = int(landmark.x*iw), int(landmark.y*ih)
            #     print(id, x, y)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (50,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

    cv.imshow('Img', img)
    cv.waitKey(1)
