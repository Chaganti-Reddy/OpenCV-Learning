import numpy as np
import cv2 as cv
import os

people = []

for i in os.listdir(r'Learning/Faces/train'):
    people.append(i)  # Reading all the folders into a list

haar_cascade = cv.CascadeClassifier(
    'Learning/Face-Detect-Built-In/haar_face.xml')  # Reading cascade file

features = np.load(
    'Learning/Face-Detect-Built-In/features.npy', allow_pickle=True)
labels = np.load('Learning/Face-Detect-Built-In/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Learning/Face-Detect-Built-In/Face_trained_model.yml')

img = cv.imread('Learning/Faces/val/ben_afflek/2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

# Detect the faces in the images
faces_rect = haar_cascade.detectMultiScale(
    gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (5, 30),
               cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img,  (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

img = cv.resize(img, (400, 600))

cv.imshow("Detected Image", img)

cv.waitKey(0)


# This model is not that accurate but it has high confidence.
# But we can optimize it to more and more
