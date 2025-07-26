import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            boundingBoxClass = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            boundingBox = int(boundingBoxClass.xmin * iw), int(boundingBoxClass.ymin * ih), int(boundingBoxClass.width * iw), int(boundingBoxClass.height * ih)

            cv.rectangle(img, boundingBox, (255,0,0), 2)

            cv.putText(img, str(int(detection.score[0]*100))+"%", (boundingBox[0], boundingBox[1] -20), cv.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)




    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)


    cv.imshow("image", img)
    cv.waitKey(1)