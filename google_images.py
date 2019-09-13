#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 22:35:50 2019

@author: naomi
"""

# importing google_images_download module 
from google_images_download import google_images_download 
# creating object 
response = google_images_download.googleimagesdownload()  
  
search_queries = ["confused", "person -confused", "confused looking", "confused person",
                  "teenager -confused", "man -confused", "woman -confused", "confused man", 
                  "confused woman", "confused teenager", "smiling person", "person", "uncertain person",
                  "american person -confused", "white confused person", "asian confused person",
                  "black confused person", "hispanic confused person", "white person -confused",
                  "black person -confused", "asian person -confused", "hispanic person -confused"]
  
def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query,  
                 "limit":5000, } 
    try: 
        response.download(arguments) 
        # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query,  
                     "limit":4, 
                     "print_urls":True,  } 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()  