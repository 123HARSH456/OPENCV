import cv2 as cv
import mediapipe as mp
import time

class FaceDetector():
    def __init__(self, minDetectionConfidence=0.5):

        self.minDetectionConfidence = minDetectionConfidence

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionConfidence) 

    def findFaces(self, img, draw=True):

        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)

        boundingBoxes = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                boundingBoxClass = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                boundingBox = int(boundingBoxClass.xmin * iw), int(boundingBoxClass.ymin * ih), int(boundingBoxClass.width * iw), int(boundingBoxClass.height * ih)

                boundingBoxes.append([boundingBox, detection.score])
                if draw:
                    self.fancyDraw(img, boundingBox)
                    cv.putText(img, str(int(detection.score[0]*100))+"%", (boundingBox[0], boundingBox[1] -20), cv.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)
        return img, boundingBoxes

    def fancyDraw(self, img, boundingBox, l=30, thickness = 7):
        x, y, w, h = boundingBox
        x1, y1 = x+w, y+h
        cv.rectangle(img, boundingBox, (255,0,0), 2)
        cv.line(img, (x, y), (x+l, y), (0,0,255), thickness)
        cv.line(img, (x, y), (x, y+l), (0,0,255), thickness)
        cv.line(img, (x1, y), (x1-l, y), (0,0,255), thickness)
        cv.line(img, (x1, y), (x1, y+l), (0,0,255), thickness)
        cv.line(img, (x, y1), (x+l, y1), (0,0,255), thickness)
        cv.line(img, (x, y1), (x, y1-l), (0,0,255), thickness)
        cv.line(img, (x1, y1), (x1-l, y1), (0,0,255), thickness)
        cv.line(img, (x1, y1), (x1, y1-l), (0,0,255), thickness)
        return img
    

def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    while True:
        success, img = cap.read()

        img, bboxs = detector.findFaces(img)


        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)


        cv.imshow("image", img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()