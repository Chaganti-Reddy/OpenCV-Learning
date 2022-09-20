# Let's see different Trandformations of images
import numpy as np
import cv2 as cv

img = cv.imread('Learning/Photos/park.jpg')
cv.imshow("Park", img)

# Let's Translate the Image (Lets change the axis of images)


def translate(img, x, y):
    """Function to Translate the Images."""

    # If x < 0 --> Shifting to Left
    # If y < 0 --> Shifting to Up
    # If x > 0 --> Shifting to Right
    # If y > 0 --> Shifting to Down
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # Translation Matrix
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

translated1 = translate(img, -100, -100)
cv.imshow("Translated 1", translated1)

# Rotation of an Image


def rotate(img, angle, rotPoint=None):
    """Function to rotate an Image."""

    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated1 = rotate(rotated, -45)
cv.imshow("Rotated 1", rotated1)

# Flipping the Image
flip_vert = cv.flip(img, 0)
cv.imshow("Flip Vert", flip_vert)
# 0 --> Flip Vertically
# 1 --> Flip Horizontally
# -1 --> Flip both sides
flip_hori = cv.flip(img, 1)
cv.imshow("Flip Hori", flip_hori)

flip_both = cv.flip(img, -1)
cv.imshow("Flip Both", flip_both)

cv.waitKey(0)
