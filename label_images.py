#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:26:29 2019

@author: naomi
"""
import csv
import os

directory = "Google/" 
image_dataset = {}
final_dataset = [["id", "label"]]
folders = [x[0] for x in os.walk(directory) if x[0] != 'Google/train' and x[0] != 'Google']

with open(directory + 'google_dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        #clip_dataset.append([row[0], row[1]])
        image_dataset[row[0]] = row[1]
        
#for folder in folders:
for f in os.listdir("Google/gray_train/"):
    if '.' not in f or '.csv' in f or f == '.DS_Store':
        continue
    try:
        label = image_dataset[f]
        final_dataset.append([f, label])
    except KeyError:
        continue

with open('Google/new_dataset.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(final_dataset)
    