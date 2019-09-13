#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:52:42 2019

@author: naomi
"""

import os
import face_recognition
import cv2

#directory = "Google"
folder = 'Google/train/'
#folders = [x[0] for x in os.walk(directory) if x[0] != 'Google/train' and x[0] != 'Google']
#files_left = check_images.findFiles(directory)
def sobelDerivative(image, scale = 1, delta = 0, ddepth = cv2.CV_64F, ksize=3, order=1):
    grad_x = cv2.Sobel(image, ddepth, dx=order,dy=0, ksize=ksize, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    # Gradient-Y
    grad_y = cv2.Scharr(image,ddepth,dx=0,dy=order)
    #grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    
    
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad

def recognizeFaces(image):
    face_locations = face_recognition.face_locations(image)
    return face_locations
    #crop_img = image[face_locations[0][0]:face_locations[0][3], face_locations[0][2]:face_locations[0][1]]
    
def cropFaces(faces, image):
    if len(faces) > 0:
        top, right, bottom, left = faces[0]
        crop_img = image[top:bottom, left:right]
        final = cv2.resize(crop_img, (154, 154), interpolation = cv2.INTER_AREA)
        return final

def preprocess(img):
    contrast = cv2.equalizeHist(img) 
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10, 10))
    contrast_new = clahe.apply(contrast)
    blur = cv2.bilateralFilter(contrast_new, 9, 75, 75)
    return blur

#for folder in folders:
for file in os.listdir(folder):
    print(file)
    img = cv2.imread(folder + '/' + file, 0)
    #rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10, 10))
    #contrast_new = clahe.apply(contrast)
    #blur = cv2.bilateralFilter(contrast_new, 9, 75, 75)
    #sobel = sobelDerivative(blur, 1.1, 0, cv2.CV_64F, 3, 1)
    try:
        final = cv2.resize(img, (154, 154), interpolation = cv2.INTER_AREA)
        cv2.imwrite('Google/gray_train/' + file, final)
    except:
        continue
    '''
    try:
        face_locations = recognizeFaces(img)
        if (len(face_locations) > 0):
            print(file)
             #[y:y+h, x:x+w]
            #top, right, bottom, left = face_locations[0]
            #crop_img = img[top:bottom, left:right]
            final = cv2.resize(crop_img, (154, 154), interpolation = cv2.INTER_AREA)
            try:
                cv2.imwrite('Google/gray_train/' + file, final)
            except:
                continue
    except TypeError:
        continue
    '''
    

    #if (len(recognizeFaces(sobelDerivative(blur, 1.1, 0, cv2.CV_64F, 3, 1))) == 0):
        #not_working.append(file)
    #ifQuit = input("yes or no?")
    #if ifQuit == "yes":
    #    break

