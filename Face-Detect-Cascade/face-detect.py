# In this we will use built-in haarcascade file to detect faces in an image
import cv2 as cv

img = cv.imread('Learning/Photos/group 1.jpg')
cv.imshow("Group of 5", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Lady", gray)

haar_cascade = cv.CascadeClassifier(
    'Learning/Face-Detect/haar_face.xml')  # Reading cascade file

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)  # Getting the coordinates of face from the images
# Changing the minNeighbors wil;l incerase the effectivity

print(f'No.of Face = {len(faces_rect)}')  # Printing no.of faces in image

for (x, y, w, h) in faces_rect:
    # Drawing rectangle over the face
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow("Detected Faces", img)

cv.waitKey(0)
