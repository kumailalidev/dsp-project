"""
main.py

This program will recognize student faces and mark attendance
"""

# Import necessary packages
import cv2
from scripts import attendance

# Creating face recognizer using Local Binary Patterns Histogram (LBPH)
recognizer = cv2.face.LBPHFaceRecognizer.create()

# Loading trained model
recognizer.read("media/trainer/trainer.yml")

# Using haarcascade
cascadePath = "media/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# font for displaying seat number/
font = cv2.FONT_HERSHEY_SIMPLEX


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Setting camera parameters
cam.set(3, 640)  # set video width
cam.set(4, 360)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    _, img = cam.read()

    # Converting image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting faces from grayscale image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    # Drawing rectangle and adding labels based on recognized face
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        seat_number, confidence = recognizer.predict(gray[y : y + h, x : x + w])
        # print(f"EH{seat_number}, Confidence:{round(confidence)}%")

        # Checking confidence level and mark attendance of student
        if confidence >= 40 and confidence < 100:
            confidence = "{0}%".format(round(confidence))
            seat_number = "EH" + str(seat_number)

            # Mark attendance
            attendance.mark_attendance(seat_number)

        else:
            seat_number = "UNKNOWN STUDENT"
            confidence = "{0}%".format(round(confidence))

        cv2.putText(img, str(seat_number), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow("Attendance System", img)

    # Press 'ESC' for exiting video
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break

print("\n[INFO] EXITING PROGRAM. PLEASE WAIT")
cam.release()
cv2.destroyAllWindows()
