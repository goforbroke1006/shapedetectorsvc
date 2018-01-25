import argparse
import imutils
import matplotlib.pyplot as plt
import cv2

import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=800)
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

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




# loop over the contours
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.03 * peri, True)
    shape_name = "unidentified"

    for clf in classifiers:
        if clf.match(approx):
            shape_name = clf.__class__.__name__
            break

    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)
    cv2.putText(resized, shape_name, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.drawContours(resized, [approx], -1, (255, 0, 0), 2)

    # show the output image
    cv2.imshow("Image", resized)
    cv2.waitKey(0)

    # plt.ion()
    # plt.imshow(image)
    # time.sleep(1)


exit()
