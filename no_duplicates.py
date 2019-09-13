#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:49:55 2019

@author: naomi
"""
import csv
images = {}
final_dataset =[["id", "label"]]
with open('Google/new_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #clip_dataset.append([row[0], row[1]])
        char = row[0]
        if char not in images:
            images[row[0]] = row[1]
for image in images:
    final_dataset.append([image, images[image]])
with open('Google/new_dataset.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(final_dataset)