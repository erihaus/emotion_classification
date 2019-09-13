#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:25:02 2019

@author: naomi
"""

import csv
import os

directory = "BAUM_Test"
folders = [x[0] for x in os.walk(directory) if x[0] != 'BAUM_Test']
frame_dataset = [["id", "label"]]
clip_dataset = {}
not_labeled = []
with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #clip_dataset.append([row[0], row[1]])
        clip_dataset[row[0]] = row[1]
last_clip = ""
last_data = ""
for f in os.listdir(directory):
    if f[0] == '.':
        continue
    '''
    with Image.open('BAUM_images/' + f) as img:
        width, height = img.size
        if width != 154:
            continue
    '''
    clip_name = f[0:8]
    if last_clip == clip_name:
        frame_dataset.append([f, last_data])
    else:
        try:
            last_data = clip_dataset[clip_name]
            frame_dataset.append([f, last_data])
            last_clip = clip_name
        except KeyError:
            not_labeled.append(clip_name)
            continue
    
    
'''
for row in clip_dataset:
    clip_name = row[0]
    for f in os.listdir(directory):
        if f.find(clip_name) != -1:
            frame_dataset.append([f, row[1]])
            with Image.open('BAUM_images/' + f) as img:
                width, height = img.size
                if width > maxSize[0] and height > maxSize[1]:
                    maxSize = (width, height)

'''
print(len(frame_dataset))
print(len(not_labeled))
with open('frame_test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(frame_dataset)