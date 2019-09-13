#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 00:18:39 2019

@author: naomi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:25:02 2019

@author: naomi
"""

import os
import csv

directory = "downloads/"
folders = [x[0] for x in os.walk(directory) if x[0] != 'downloads']
frame_dataset = [["id", "label"]]

for folder in folders:
    value = 0
    if "confused" in folder:
        value = 1
    for f in os.listdir(folder):
        frame_dataset.append([f, value])
    
'''
if folder=="confused" or folder=="confused looking"
for f in os.listdir(directory):
        frame_dataset.append([f, last_data])
'''

with open('downloads/google_dataset.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(frame_dataset)
