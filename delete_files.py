#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 16:29:29 2019

@author: naomi
"""
import csv
import os
directory = 'Google/train/'
corrupted = ['241.59774-speech-bubble-with-confused-person-clipart.png', '349.Confused-595b40b75ba036ed117d934e.svg', '348.explorers_ISTP_bear_grylls.svg', '131.black%20panther%20disney%20white%20pin.jpg', '142.1f481-200d-2640-fe0f.svg', '250.confused-anime-boy.jpg', '235.210899_5_.jpg', '277.21401-80s-woman-confused-on-cell-phone.jpg', '248.gordon_ramsay.jpg', '280.Confused-595b40b65ba036ed117d0fd8.svg', '304.helpcenter_icons-05.svg', '313.gordon_ramsay.jpg', '57.confused-logo.png', '134.diplomats_ENFJ_barack_obama.svg', '280.khloe%20kardashian%20collage.jpg', '254.1f481-200d-2640-fe0f.svg', '53.George%20Ezra.jpg', '118.woman-at-war.jpg', '244.1188279.png', '288.549694.png', '312.diplomats_ENFP_robin_williams.svg', '86.1258662033309785144ghosthand_Tillie.svg', '170.person-generic.svg', '217.diplomats_ENFP_RM_Kim_Nam-joon.svg']

for file in corrupted:
    print(directory+file)
    os.remove(directory + file)

with open('final_dataset.csv', 'r') as inp, open('new_dataset.csv', 'w') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] not in corrupted:
            writer.writerow(row)
            
