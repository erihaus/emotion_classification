#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 11:00:09 2019

@author: naomi
"""
import os
from PIL import Image

directory = "BAUM_images"

def findFiles(directory):
    images_left = []
    for file in os.listdir(directory):
        if file[0] == '.':
            continue
        im = Image.open(directory + '/' + file)
        width, height = im.size
        if width == 154:
            images_left.append(file)
        
    return images_left
print(findFiles(directory))
