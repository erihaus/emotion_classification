#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 23:18:58 2019

@author: naomi

NOT the final video processing code
"""


import cv2     # for capturing videos   # for mathematical operations
import numpy as np    # for mathematical operations
import os
#from imutils.video import FileVideoStream
from imutils.video import FPS
import time
from threading import Thread
from queue import Queue

'''
data_set = inputString.splitlines()
videos = []

for value in data_set:
    if value[0] == 'O':
        videos.append(value[46:58])
'''
directory = 'Videos'
folders = [x[0] for x in os.walk(directory) if x[0] != 'Videos']

class FileVideoStream:
    def __init__(self, path, queueSize=128):
		# initialize the file video stream along with the boolean
		# used to indicate if the thread should be stopped or not
        self.stream = cv2.VideoCapture(path)
        self.stopped = False
 
		# initialize the queue used to store frames read from
		# the video file
        self.Q = Queue(maxsize=queueSize)
    def start(self):
		# start a thread to read frames from the file video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self
    def update(self):
		# keep looping infinitely
        while True:
			# if the thread indicator variable is set, stop the
			# thread
            if self.stopped:
                return
 
			# otherwise, ensure the queue has room in it
            if not self.Q.full():
				# read the next frame from the file
                (grabbed, frame) = self.stream.read()
 
				# if the `grabbed` boolean is `False`, then we have
				# reached the end of the video file
                if not grabbed:
                    self.stop()
                    return
 
				# add the frame to the queue
                self.Q.put(frame)
    def read(self):
		# return next frame in the queue
        return self.Q.get()
    def more(self):
		# return True if there are still frames in the queue
        return self.Q.qsize() > 0
    def stop(self):
		# indicate that the thread should be stopped
        self.stopped = True
        
for folder in folders:
    for f in os.listdir(folder):
        #f = 'Videos/' + video[0:4] + '/' + video
        if 'srt' in f:
            continue
        file_name = folder + '/'+ f
        print(file_name)
        fvs = FileVideoStream(file_name).start()
        time.sleep(1.0)
        # start the FPS timer
        fps = FPS().start()
        # loop over frames from the video file stream
        last_file_name = ""
        while fvs.more():
            	# grab the frame from the threaded video file stream, resize
            	# it, and convert it to grayscale (while still retaining 3
            	# channels)
            frame = fvs.read()
            #frame = imutils.resize(frame, width=450)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = np.dstack([frame, frame, frame])
            '''
            contrast = cv2.equalizeHist(frame) 
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(10, 10))
            contrast_new = clahe.apply(contrast)
            blur = cv2.bilateralFilter(contrast_new, 9, 75, 75)
            sobel = crop_images.sobelDerivative(blur, 1.1, 0, cv2.CV_64F, 3, 1)
            face_locations = crop_images.recognizeFaces(sobel)
            if (len(face_locations) > 0):
                queue_size = fvs.Q.qsize()
                new_file_name = "BAUM_images/" + file_name + "frame" + str(queue_size) + ".jpg"
                top, right, bottom, left = face_locations[0]
                crop_img = sobel[top:bottom, left:right]
                final = cv2.resize(crop_img, (154, 154), interpolation = cv2.INTER_AREA)
                cv2.imwrite(new_file_name, final)
            '''
            queue_size = fvs.Q.qsize()
            new_file_name = "BAUM_images" + file_name[20:] + "frame" + str(queue_size) + ".jpg"
            if last_file_name == new_file_name:
                continue
            else:
                cv2.imwrite(new_file_name, frame)
                last_file_name = new_file_name
            fps.update()
'''
count = 0
cap = cv2.VideoCapture(f)   # capturing the video from the given path
fps = cap.get(cv2.CAP_PROP_FPS)
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(fps) == 0):
        #filename = f[0:f.rindex('.')] + "frame%d.jpg" % count;
        count+=1
        #cv2.imwrite(filename, frame)
cap.release()
print ("Done!")
'''
        
