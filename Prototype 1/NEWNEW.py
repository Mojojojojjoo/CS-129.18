# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:41:39 2018

@author: Gwapito
"""

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
from sklearn.externals import joblib
import math

image = imread("car1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 250)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=50)
hough = np.zeros(image.shape, np.uint8)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(hough, (x1, y1), (x2, y2), (255, 255, 255), 2)

cv2.imwrite('hough.jpg', hough)