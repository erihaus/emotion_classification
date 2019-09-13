#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:31:48 2019

@author: naomi
"""

import cv2
import os
directory = "Train"
for file in os.listdir(directory):
    file_loc = directory + "/" + file
    img = cv2.imread(file_loc)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #face_loc = face_recognition.face_locations(gray)
    #sobel = crop_images.sobelDerivative(gray, 1.1, 0, cv2.CV_64F, 3, 1)
    __ ,contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(gray, contours, 3, 255, 3)
    cv2.imshow("new", gray)
    k=cv2.waitKey(0)
    cv2.destroyAllWindows()
    if k==ord('q'):
        break
    '''
    if (len(face_loc) > 0):
        top, right, bottom, left = face_loc[0]
        crop = gray[top:bottom, left:right]
        final = cv2.resize(crop, (154, 154), interpolation = cv2.INTER_AREA)
        cv2.imwrite(file_loc, final)
    '''
