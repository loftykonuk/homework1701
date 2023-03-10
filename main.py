import cv2
import numpy as np

img = cv2.imread("image.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([160,100,100])
upper_range = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("mask",mask)
cv2.imshow("image",img)
cv2.imshow("result",res)

cv2.waitKey(0)
cv2.destroyAllWindows()