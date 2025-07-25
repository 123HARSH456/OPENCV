import cv2 as cv
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode= False, upperBody= False, smoothness= True, detectionConfidence= 0.5, trackingConfidence= 0.5):

        self.mode = mode
        self.upperBody = upperBody
        self.smoothness = smoothness
        self.detectionConfidence = detectionConfidence
        self.trackingConfidence = trackingConfidence


        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode, smooth_landmarks=self.smoothness, min_detection_confidence=self.detectionConfidence, min_tracking_confidence=self.trackingConfidence)


    def findPose(self, img, draw= True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img
    
    

    def findPosition(self, img, draw= True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)
        return lmList


    

def main():
    cap = cv.VideoCapture(0)
    pTime = 0


    detector = poseDetector()

    while True:
        success, img = cap.read()

        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        print(lmList)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (50,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

        cv.imshow('Img', img)

        cv.waitKey(1)


if __name__ == "__main__":
    main()