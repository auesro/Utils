#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 18:10:34 2019

@author: augustoer
"""

import cv2
stream = cv2.VideoCapture('/home/augustoer/ABRS/Test/hour120.mp4')
fps = stream.get(cv2.CAP_PROP_FPS)
total_frames = int(stream.get(cv2.CAP_PROP_FRAME_COUNT))
duration = stream.get(cv2.CAP_PROP_POS_MSEC)
fourcc = int(stream.get(cv2.CAP_PROP_FOURCC))

frame_number = 1
stream.set(0, frame_number)
ret, frame = stream.read()
cv2.imshow('Hola', frame)
smallfr = cv2.resize(frame,(int(960*0.5),int(540*0.5)))
cv2.imshow('Adios', smallfr)

key = cv2.waitKey(0)
while key not in [ord('q'), ord('k')]:
    key = cv2.waitKey(0)
# Quit when 'q' is pressed
    if key == ord('q'):
        break
stream.release()
cv2.destroyAllWindows()


#count = 0
#while(True):
#      ret, frame = stream.read()
#      if not ret:
#          break
#      count += 1

