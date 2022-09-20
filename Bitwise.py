# In this we will use bitwise operators in openCV
import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
cv.imshow("Blank", blank)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200,  255, -1)
cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# Bitwise AND operator --> Intersecting Region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR operatorc --> Non Intersecting and Intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# We can also use XOR etc.., using the built-in functions
# Bitwise XOR --> Non-Intersecting Region
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow("Bitwise NOR", bitwise_not)

cv.waitKey(0)
