import argparse
import imutils
import matplotlib.pyplot as plt
import cv2

import os

from geometry_util import contour_center


def contour_do_scale(_contour, _ratio):
    _contour = _contour.astype("float")
    _contour *= _ratio
    return _contour.astype("int")


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
resized = imutils.resize(image, width=800)
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]

dir_ = "classifiers"
classifiers = []
for classifier_file in os.listdir(os.path.dirname(__file__) + "/" + dir_):
    if classifier_file == '__init__.py' or classifier_file[-3:] != '.py':
        continue
    classifier_name = classifier_file[:-3]
    print(classifier_name)
    module_ = __import__(dir_ + "." + classifier_name, locals(), globals(), fromlist=[classifier_name])
    class_ = getattr(module_, classifier_name)
    instance = class_()
    classifiers.append(instance)

plt.imshow(resized)

for c in contours:
    cX, cY = contour_center(c)
    cX, cY = int(cX * ratio), int(cY * ratio)

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.03 * peri, True)
    shape_name = "unidentified"

    for clf in classifiers:
        if clf.match(approx):
            shape_name = clf.__class__.__name__
            break

    c = contour_do_scale(c, ratio)
    cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)
    cv2.putText(resized, shape_name, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.drawContours(resized, [approx], -1, (255, 0, 0), 2)

plt.imshow(resized)
plt.show()
