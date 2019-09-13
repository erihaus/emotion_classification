#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 13:41:10 2019

@author: naomi

The FINAL video processing code
"""

import os
import cv2

directory = 'BAUM_videos'
folders = [x[0] for x in os.walk(directory) if x[0] != 'BAUM_videos']

for folder in folders:
    for f in os.listdir(folder):
        if 'srt' in f:
            continue
        file_name = '/Users/naomi/Documents/Final_Dataset/' + folder + '/' + f
        cap = cv2.VideoCapture(file_name)
        '''
        try:
        except cv2.error:
            continue
        '''
        while not cap.isOpened():
            cap = cv2.VideoCapture(file_name)
            cv2.waitKey(1000)
        
        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        while True:
            flag, frame = cap.read()
            if flag:
                # The frame is ready and already captured
                if pos_frame == cap.get(cv2.CAP_PROP_POS_FRAMES):
                    break
                cv2.imshow('video', frame)
                pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                image_file = file_name + 'frame' + str(pos_frame) + '.jpg'
                cv2.imwrite(image_file, frame)
            else:
                # The next frame is not ready, so we try to read it again
                cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame-1)
                # It is better to wait for a while for the next frame to be ready
                cv2.waitKey(1000)
        
            if cv2.waitKey(10) == 27:
                break
            if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                # If the number of captured frames is equal to the total number of frames,
                # we stop
                break