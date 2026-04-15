import cv2
import numpy as np
import time

# -----------------------------
# SETTINGS
# -----------------------------
EYE_CLOSED_FRAMES = 20
YAWN_FRAMES = 15


class DrowsinessDetector:
    def __init__(self):   # ✅ FIXED (__init__)
        cascades = cv2.data.haarcascades

        self.face_cascade = cv2.CascadeClassifier(cascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cascades + 'haarcascade_eye.xml')
        self.mouth_cascade = cv2.CascadeClassifier(cascades + 'haarcascade_smile.xml')

        self.eye_counter = 0
        self.yawn_counter = 0
        self.drowsy = False
        self.score = 0

        print("✅ System Initialized")

    def detect(self, gray):
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)

        results = []
        for (x, y, w, h) in faces:
            roi_top = gray[y:y + h//2, x:x + w]
            roi_bottom = gray[y + h//2:y + h, x:x + w]

            eyes = self.eye_cascade.detectMultiScale(roi_top, 1.1, 10)
            mouth = self.mouth_cascade.detectMultiScale(roi_bottom, 1.7, 20)

            results.append((x, y, w, h, eyes, mouth))

        return results

    def update(self, results):
        all_eyes = []
        all_mouths = []

        for r in results:
            all_eyes.extend(r[4])
            all_mouths.extend(r[5])

        # Eye logic
        if len(all_eyes) >= 2:
            self.eye_counter = 0
        elif len(all_eyes) == 1:
            self.eye_counter += 0.5
        else:
            self.eye_counter += 1

        # Drowsiness check
        if self.eye_counter >= EYE_CLOSED_FRAMES:
            self.drowsy = True
            self.score = min(100, self.score + 5)
        else:
            self.drowsy = False
            self.score = max(0, self.score - 1)

        # Yawn detection
        if len(all_mouths) > 0:
            self.yawn_counter += 1
        else:
            self.yawn_counter = max(0, self.yawn_counter - 1)

        yawning = False
        if self.yawn_counter >= YAWN_FRAMES:
            yawning = True
            self.yawn_counter = 0

        return self.drowsy, yawning, self.score

    def draw(self, frame, results, drowsy, yawning, score):
        for (x, y, w, h, eyes, mouth) in results:

            color = (0, 255, 0)
            if drowsy:
                color = (0, 0, 255)
            elif score > 50:
                color = (0, 165, 255)

            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (255, 255, 0), 1)

            for (mx, my, mw, mh) in mouth:
                cv2.rectangle(frame, (x+mx, y+h//2+my), (x+mx+mw, y+h//2+my+mh), (255, 0, 255), 1)

        # HUD
        cv2.putText(frame, f"Score: {score}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        status = "ALERT"
        if drowsy:
            status = "DROWSY"
        elif score > 50:
            status = "WARNING"

        cv2.putText(frame, f"Status: {status}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if drowsy or yawning:
            cv2.putText(frame, "WAKE UP!", (200, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        return frame


def main():
    print("🚗 Driver Drowsiness Detection Started")

    detector = DrowsinessDetector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not working. Try 1 instead of 0")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        results = detector.detect(gray)
        drowsy, yawning, score = detector.update(results)
        frame = detector.draw(frame, results, drowsy, yawning, score)

        cv2.imshow("Drowsiness Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Closed")


if __name__ == "__main__":   # ✅ FIXED
    main()