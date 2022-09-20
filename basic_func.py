import cv2 as cv

img = cv.imread('Learning/Photos/park.jpg')
cv.imshow("Park", img)

# Converting to GrayScale Images from BGR Images
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cat", gray)

# Now Blur the Images
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
# Kernel size is to be odd number & it will increase the blurness
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur More", blur)

# Edge Cascade
# This shows the edges of the image
canny = cv.Canny(img, 125, 175)
cv.imshow("Edges", canny)

# If we want to reduce the amount of edges then use the blur images
canny = cv.Canny(blur, 125, 175)
cv.imshow("Edges_blur", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding the Dilated Images
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize() the Images
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)
# Interpolation changes the quality of the Images
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized_Inter", resized)

# Cropping the Images
cropped = img[50:200, 200:500]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
