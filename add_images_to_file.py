#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:43:57 2019

@author: naomi
"""

import os
import cv2
import face_recognition


directory = 'BAUM_videos'

folders = [x[0] for x in os.walk(directory) if x[0] != 'BAUM_videos']

    
for folder in folders:
    if folder == 'BAUM_videos/s007' or folder == 'BAUM_videos/s008' or folder =='BAUM_videos/s031' or folder == 'BAUM_videos/s009':
        print("already finished")
        continue
    for f in os.listdir(folder):
        if 'jpg' in f:
            file_name = '/Users/naomi/Documents/Final_Dataset/' + folder + '/' + f
            img = cv2.imread(file_name, -1)
            cv2.imwrite('orig_BAUM_images/' + f, img)
            '''
            #rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            sensitivity = 15
            lower_bound = (60 - sensitivity, 100, 100)
            upper_bound = (60 + sensitivity, 255, 255)
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            mask = cv2.bitwise_not(mask, mask)
            result = cv2.bitwise_and(img, img, mask=mask)
            final = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
            face_locations = face_recognition.face_locations(final)
            
            #(top, left, bottom, right)???
            #[y:y+h, x:x+w]
            if len(face_locations) > 0:
                crop_img = final[face_locations[0][0]:face_locations[0][3], face_locations[0][2]:face_locations[0][1]]
                cv2.imwrite('BAUM_images/' + f, crop_img)
            '''