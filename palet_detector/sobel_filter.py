import cv2
from matplotlib import pyplot

img = cv2.imread('./input/palet.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray, (3, 3), 0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)  # x
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  # y

pyplot.subplot(2, 2, 1), pyplot.imshow(img, cmap='gray')
pyplot.title('Original'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 2), pyplot.imshow(laplacian, cmap='gray')
pyplot.title('Laplacian'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 3), pyplot.imshow(sobelx, cmap='gray')
pyplot.title('Sobel X'), pyplot.xticks([]), pyplot.yticks([])
pyplot.subplot(2, 2, 4), pyplot.imshow(sobely, cmap='gray')
pyplot.title('Sobel Y'), pyplot.xticks([]), pyplot.yticks([])

pyplot.show()

# TODO: ploter gradient de l'image
