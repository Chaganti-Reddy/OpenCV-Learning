# Rescale videos will be good for lower resolution cameras

import cv2 as cv


def Rescale(frame, scale=0.75):
    """Function to rescale the given video/Image to a particule dimensions.
       This works for Images, Videos, Live Videos.
    """

    width, height = int(frame.shape[1]*scale), int(frame.shape[0]*scale)
    # Frame.shape is a tuple of (height, width)

    dimensions = (width, height)

    # Built-In resize() function in CV
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def Change_Res(video, width, height):
    """Function to change Resolution of an Image/Video.
       This works only for Live Videos.
    """

    # 3 stands for the property of width in capture.set method
    video.set(3, width)
    video.set(4, height)


# Now read the videos

capture = cv.VideoCapture('Learning/Videos/dog.mp4')

while True:
    ifTrue, frame = capture.read()

    frame_resized = Rescale(frame)  # Let's take default scale value
    frame_resized1 = Rescale(
        frame, scale=0.2)  # Let's take scale value = 20%

    cv.imshow('Video', frame)
    cv.imshow('Video Reshaped', frame_resized)
    cv.imshow('Video Reshaped Small', frame_resized1)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break


# capture.release()
# cv.destroyAllWindows()

# Read the images

# Same as videos we can reshape images

img = cv.imread('Learning/Photos/cat_large.jpg')
img_reshaped = Rescale(img, scale=0.2)
cv.imshow("Image", img)
cv.imshow("Reshaped Image", img_reshaped)
cv.waitKey(0)
cv.destroyAllWindows()
