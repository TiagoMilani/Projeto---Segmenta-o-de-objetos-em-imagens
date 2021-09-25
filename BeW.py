
#!/usr/bin/env python
# coding: utf-8

import cv2              
import numpy as np
import sys
#from matplotlib import pyplot as plt 
def teste(testeimg):
    image = cv2.imread(testeimg)  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    ret, thresh = cv2.threshold(gray, 0, 255, 
                                cv2.THRESH_BINARY_INV +
                                cv2.THRESH_OTSU) 
    cv2.imshow('image', thresh)      

    kernel = np.ones((3, 3), np.uint8) 
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, 
                                kernel, iterations = 2) 
    bg = cv2.dilate(closing, kernel, iterations = 1) 
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
    ret, fg = cv2.threshold(dist_transform, 0.02
                            * dist_transform.max(), 255, 0) 

    cv2.imshow('image2', fg) 

    cv2.waitKey(0)
