import os
import numpy as np
import cv2 as cv

people = []
DIR = r'Learning/Faces/train'

for i in os.listdir(r'Learning/Faces/train'):
    people.append(i)  # Reading all the folders into a list

haar_cascade = cv.CascadeClassifier(
    'Learning/Face-Detect-Built-In/haar_face.xml')  # Reading cascade file

features = []
labels = []


def create_train():
    """Function to train our mini model."""

    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path, image)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

print("Training Done ------------------->")

features = np.array(features, dtype=object)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train recognizer on features list & Labels list

face_recognizer.train(features, labels)

face_recognizer.save('Face_trained_model.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
