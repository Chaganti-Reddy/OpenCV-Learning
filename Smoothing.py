# In this we will remove any Noice caused by photo sensors etc.., we will try smoothing and blurring.
import cv2 as cv

# In an image a small portion of matrix is known as kernel
# And changing the Intensities of this kernel will change the intensity of middle of the kernel and causes blurring

# There are different methods
# 1) Average :--> This method takes average of all the blocks in the kernel and take average and apply to all the blocks of the kernel
img = cv.imread('Learning/Photos/cats.jpg')
average = cv.blur(img, (3, 3))  # (3,3) --> Kernel size --> matrix
average1 = cv.blur(img, (7, 7))  # More blur
cv.imshow("Cats", img)
cv.imshow("Average Blur", average)
cv.imshow("Average 7*7", average1)

# 2) Gaussian Blur --> In this method we will all the weights of blocks of the kernel and takes the average of product of all then blocks and use it in the middle block
# Gaussian method is more natural & less blur than average blur

# 0 --> SigmaX which is Standard Deviation
gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian 7*7", gaussian)

# 3) MediaN Blur --> It is same as average blur but instead of taking average we will take median of all surrounding blocks
# This method is more efficient to clear the noice of the image
median = cv.medianBlur(img, 7)
cv.imshow("Median 7", median)

# 4) Bilateral Blurring --> This is the most efferctive blurring method which even used in large and advanced OPPENCV projects
bilateral = cv.bilateralFilter(img, 30, 35, 25)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)
