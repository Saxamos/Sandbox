import math

import cv2
import numpy
from matplotlib import pyplot
from scipy.spatial import distance

MID_COLOR = (120, 120, 120)


def binarize_image(image):
    threshold = _get_threshold(image)
    image[image < threshold] = 0
    image[image >= threshold] = 255
    return image


def _get_threshold(image):
    pixel_intensity_histogram = numpy.histogram(image, bins=256, range=(0, 256))[0]
    threshold = _max_entropy(pixel_intensity_histogram)

    # pyplot.plot(pixel_intensity_histogram)
    # pyplot.axvline(x=threshold, color='r')
    # pyplot.show()
    return threshold


def _max_entropy(histogram):
    """
    "A New Method for Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985)
    https://github.com/zenr/ippy/blob/master/segmentation/max_entropy.py
    :param histogram: Sequence representing the histogram of the image
    :return threshold: Resulting maximum entropy threshold
    """
    cdf = histogram.astype(numpy.float).cumsum()
    non_null_bin_indexes = numpy.nonzero(histogram)[0]

    max_entropy, best_threshold = 0, 0
    for i in range(len(non_null_bin_indexes)):
        dark_histogram = histogram[non_null_bin_indexes[:i + 1]]
        number_of_pixel_in_dark_histogram = cdf[non_null_bin_indexes[i]]
        dark_entropy = _compute_entropy(dark_histogram, number_of_pixel_in_dark_histogram)

        bright_histogram = histogram[non_null_bin_indexes[i + 1:]]
        number_of_pixel_in_bright_histogram = cdf[-1] - cdf[non_null_bin_indexes[i]]
        bright_entropy = _compute_entropy(bright_histogram, number_of_pixel_in_bright_histogram)

        entropy = dark_entropy + bright_entropy
        if entropy > max_entropy:
            max_entropy, best_threshold = entropy, i + 1
    return best_threshold


def _compute_entropy(histogram, number_of_pixel_in_histogram):
    probability_density_function = histogram / number_of_pixel_in_histogram
    return -numpy.sum(probability_density_function * numpy.log(probability_density_function))


## Read image
img = cv2.imread('./input/photo1.jpeg')

## Convert HSV and gray
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)

## Binarize image
bin_img = binarize_image(gray)

## Blur image
non_noised = cv2.fastNlMeansDenoising(bin_img)
blurred = cv2.medianBlur(non_noised, 27)

## Find contours
blurred, contours, hierarchy = cv2.findContours(blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
palet_area = [cv2.contourArea(c) for c in contours]
sorted_area = sorted(zip(palet_area, contours), key=lambda x: x[0], reverse=True)
largest_contours = [area[1] for area in sorted_area if area[0] > 2000]
cv2.drawContours(blurred, largest_contours, -1, MID_COLOR, thickness=7)

## Find centers
centers = []
for contour in largest_contours:
    cX, cY = int(contour[:, :, 0].mean()), int(contour[:, :, 1].mean())
    cv2.circle(blurred, (cX, cY), 7, MID_COLOR, -1)
    centers.append((cX, cY))

## Compute dist
min_dist = math.inf
for center in centers[:-1]:
    cv2.line(blurred, center, centers[-1], MID_COLOR, 2)
    dist = distance.euclidean(center, centers[-1])
    if min_dist > dist:
        min_dist = dist
        min_dist_center = center
    cv2.putText(blurred, '{:.1f}in'.format(dist), center, cv2.FONT_HERSHEY_SIMPLEX, 0.55, MID_COLOR, 5)
cv2.line(blurred, min_dist_center, centers[-1], (250, 20, 250), 5)
cv2.putText(blurred, 'WINNER', min_dist_center, cv2.FONT_HERSHEY_SIMPLEX, 0.55, MID_COLOR, 20)

## Write image
cv2.imwrite('./result/max_entropy.png', blurred)
pyplot.imshow(blurred)
pyplot.show()
