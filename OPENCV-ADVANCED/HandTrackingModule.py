import cv2 as cv
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionConfidence=0.5, trackingConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionConfidence = detectionConfidence
        self.trackingConfidence = trackingConfidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectionConfidence, min_tracking_confidence=self.trackingConfidence)
        #parameters: 
            # static mode -> keep detecting again again default false
            # max hands -> default 2
            # detection confidence -> default 50%
            # tracking confidence -> default 50%

        #used to draw 21 points on hands
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
            #first convert img to rgb from bgr
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        #hands object will process our rgb img into result object
        self.results = self.hands.process(imgRGB)

        #to detect if multiple hands detected or not
        # print(results.multi_hand_landmarks)

        #we need to extract multiple hands if present
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                

                if draw:
                    #method provided by mediapipe to draw these points (21 points on hands)
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) #draw on original img and use HAND_CONNECTIONS to draw the lines
        return img            
    def findPosition(self, img, handNo=0, draw=True):
            lmList = []
            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks  [handNo]



                # #get id and landmark from the info
                for id, lm in enumerate(myHand.landmark):
                # #this provides us with the ratio of the img x y z coordinates so we need to multiply the number with width and height to extract pixel values
                # print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(id, cx, cy)
                    lmList.append([id, cx, cy])

                    # #making index finger stand out 
                    if draw:
                        cv.circle(img, (cx, cy), 15, (255,0,255), cv.FILLED)
            return lmList



#reusable code 
def main():
    cap = cv.VideoCapture(0); #capture webcam
    #for fps calculation
    pTime = 0
    cTime = 0

    detector = handDetector()



    while True:
        success, img = cap.read()   
        img = detector.findHands(img)

        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[8])

        #for fps calculation
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        #display fps on screen
        cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_COMPLEX, 3, (255,255,0), 3)

        #display
        cv.imshow("Image", img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()