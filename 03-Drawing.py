import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')  # Here uint8 is dtype of images
cv.imshow("Blank", blank)

# Let us create with different colors
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Red", blank)

# Let's Create a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow("Rectangle", blank)

# Let's draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          40, (255, 0, 0), thickness=-1)
cv.imshow("Circle", blank)

# Let's draw a line
cv.line(blank,
        (0, 0), (250, 250), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

# Let's write some text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX,
           1.0, (0, 255, 0), thickness=2)
cv.imshow("Test", blank)

cv.waitKey(0)
