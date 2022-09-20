# In openCV we can Split and Merge the colors of the Images
import cv2 as cv

img = cv.imread('Learning/Photos/park.jpg')

# It will split the colors of image to Bluw, Green, Red respectively
b, g, r = cv.split(img)

cv.imshow("Bluw", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

cv.waitKey(0)
