import cv2 as cv  # Importing OPenCV library as cv

# Reading Images

img = cv.imread('Learning/Photos/cat.jpg')  # Reading an image using imread

# OpenCV read images in BGR format
# But all the other will read in RGB format

cv.imshow("Cat", img)  # imshow will display read image

cv.waitKey(0)

# Reading Videos

# capture = cv.VideoCapture(0) # This will take live capture from camera

# 0 --> Camera 1
# 1 --> Camera 2

# This will take input as an existing video file
capture = cv.VideoCapture('Learning/Videos/dog.mp4')

# To display videos we will use while loop continously until we stop..

while True:
    ifTrue, frame = capture.read()

    cv.imshow('Video Dog', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):  # This breaks the video when we press q
        break

capture.release()  # Releases all the capturing videos
cv.destroyAllWindows()  # Destroy all the opened windows
