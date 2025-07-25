    for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)