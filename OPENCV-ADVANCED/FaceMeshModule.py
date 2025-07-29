import cv2 as cv
import mediapipe as mp
import time



class FaceMeshDetector():
    def __init__(self, mode=False, maxFaces=2, minDetectionConfidence=0.5, minTrackingConfidence=0.5):
        self.mode= mode
        self.maxFaces= maxFaces
        self.minDetectionConfidence = minDetectionConfidence
        self.minTrackingConfidence = minTrackingConfidence
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.mode, max_num_faces=self.maxFaces, min_detection_confidence=self.minDetectionConfidence, min_tracking_confidence=self.minTrackingConfidence)
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 1)


    def findFaceMesh(self, img, draw=True):
        


        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results =self.faceMesh.process(imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLandmarks in self.results.multi_face_landmarks:
                
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLandmarks, self.mpFaceMesh.FACEMESH_TESSELATION, self.drawSpecs, self.drawSpecs)
                face = []
               
                for id, landmark in enumerate(faceLandmarks.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(landmark.x*iw), int(landmark.y*ih)
                    #Heavy code (uncomment at your own risk)
                    #print(id, x, y)
                    face.append([x, y])
                faces.append(face)
        return img, faces
    


def main():
    cap = cv.VideoCapture(0)
    pTime = 0

    detector = FaceMeshDetector()


    while True:
        success, img = cap.read()

        img, faces = detector.findFaceMesh(img)

        if len(faces)!=0:
            print(len(faces))

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (50,50), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 3)

        cv.imshow('Img', img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()