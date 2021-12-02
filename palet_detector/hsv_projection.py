import cv2
import matplotlib.pyplot as plt
import numpy as np

## Read image
img = cv2.imread('./input/palet.png')

## Convert to hsv
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## Threshold image
thresh = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)[1]

## Get mask with range
mask = cv2.inRange(thresh, (0, 255, 255), (20, 255, 255))
imask = mask > 0

## Create output image
green = np.zeros_like(img, np.uint8)
green[imask] = img[imask]

## Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Write image
cv2.imwrite('./result/hsv.png', gray)

## Eventually plot it
plt.imshow(green)
plt.show()
