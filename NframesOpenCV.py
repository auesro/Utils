#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:44:08 2019

@author: auesro
"""

import cv2

cap = cv2.VideoCapture('/home/auesro/Desktop/MouseTracking-master_AER_pad/Tests/A_ellfit.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )