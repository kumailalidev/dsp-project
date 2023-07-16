"""
dataset_generator.py

This file will generate dataset of students using camera
"""

# Import necessary packages
import cv2

# Define video capture object with cam variable
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Setting camera parameters
camera.set(3, 640)  # set video width
camera.set(4, 360)  # set video height

# Define cascadeClassifier function with haarcascade_frontalface_default.xml file
face_detector = cv2.CascadeClassifier(
    "media/haarcascades/haarcascade_frontalface_default.xml"
)

# Enter student seat no.
face_id = input(
    "\nPLEASE ENTER STUDENT SEAT NUMBER OF FORMAT EHXXXXXXX. [ENTER DIGITS ONLY, SKIP 'EH']: "
)
print("\nInitializing face capture process. please face the camera...")

# Initialize individual sampling face count
count = 0
while True:
    _, img = camera.read()

    # Converting image into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Extracting faces from the grayscale image
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around detected faces with green color
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        count += 1

        # Save the captured image in datasets folder
        cv2.imwrite(
            "media/dataset/STUDENT." + str(face_id) + "." + str(count) + ".jpg",
            gray[y : y + h, x : x + w],
        )
        print(f"PLEASE WAIT: {count}")
        cv2.imshow("Dataset Generator", img)

    # Press 'ESC' for exiting video
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
    # Take 50 face sample and stop video
    elif count >= 50:
        break

print("\n [INFO] EXITING PROGRAM. PLEASE WAIT...")
camera.release()
cv2.destroyAllWindows()
