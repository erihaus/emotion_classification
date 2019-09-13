#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:10:37 2019

@author: naomi
"""

import os

directory = 'BAUM_videos'
folders = [x[0] for x in os.walk(directory) if x[0] != 'BAUM_videos']
clips = []
not_found = []
'''
for f in os.listdir(directory):
    if f[0:4] not in clips:
        clips.append(f[0:4])
print(clips)
'''
for folder in folders:
    for f in os.listdir(folder):
        if '.jpg' not in f:
            continue
        isFound = False
        for edited_file in os.listdir('BAUM_images'):
            if f == edited_file:
                isFound = True
        if not isFound:
            not_found.append(f)
        
print(not_found)