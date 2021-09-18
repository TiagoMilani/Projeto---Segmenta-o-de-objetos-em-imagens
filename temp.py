
#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
image = cv2.imread('images/roxo.jpeg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blur = cv2.medianBlur(hsv ,11)
lower = np.array([132,113,223])
upper = np.array([140,153,255])
mask = cv2.inRange(blur, lower, upper)
res = cv2.bitwise_and(image,image, mask= mask)
cv2.imshow('printando a mascara', mask)
cv2.imshow('printando a separacao com cor', res)
cv2.waitKey(0)