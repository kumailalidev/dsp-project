"""
model_generator.py

This program will train face recognition model based on the students face dataset and generate a model 'trainer.yml.
"""

# Import necessary packages
import cv2
import numpy as np
from PIL import Image
import os

# Path for the students face image database
path = "media/dataset"

# Creating face recognizer using Local Binary Patterns Histogram (LBPH)
recognizer = cv2.face.LBPHFaceRecognizer.create()

# Using Haar cascade classifier for face features detection
detector = cv2.CascadeClassifier(
    "media/haarcascades/haarcascade_frontalface_default.xml"
)


def get_images_and_labels(path):
    """
    Functions to get images from dataset and labeling data (such as seat number)
    """
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    seat_numbers = []

    for image_path in image_paths:
        PIL_img = Image.open(image_path).convert("L")  # convert it to grayscale
        img_numpy = np.array(PIL_img, "uint8")
        seat_number = int(os.path.split(image_path)[1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for x, y, w, h in faces:
            face_samples.append(img_numpy[y : y + h, x : x + w])
            seat_numbers.append(seat_number)

    return face_samples, seat_numbers


print(
    "\n[INFO] TRAINING FACES: Please wait, model is training based on provided image dataset. It will take some time ..."
)

faces, seat_numbers = get_images_and_labels(path)
recognizer.train(faces, np.array(seat_numbers))

# Save the model into trainer/trainer.yml
recognizer.save("media/trainer/trainer.yml")

# Print the number of faces trained and suspend program
print(
    "\n[INFO] {0} UNIQUE FACES TRAINED. EXITING PROGRAM".format(
        len(np.unique(seat_numbers))
    )
)
