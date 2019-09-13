#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:02:46 2019

@author: naomi
"""
import os

class findImages:
    images = []
    directory = "downloads"
    other_dir = "Google/train"
    left = []
    folders = [x[0] for x in os.walk(directory) if x[0] != 'downloads']
    def find(self):
        for folder in self.folders:
            for file in os.listdir(folder):
                self.images.append(file)
                
        for file in os.listdir(self.other_dir):
            if file not in self.images:
                self.left.append(file)
        return self.left
    
def main():
    finder = findImages()
    print(len(finder.find()))
    print(len(finder.images))
    
if __name__ ==  "__main__":
    main()
