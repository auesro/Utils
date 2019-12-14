#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:53:50 2019

@author: auesro
"""
import cv2
import imageio
import imageio_ffmpeg
import numpy as np



input_movie = '/home/auesro/Desktop/ABRS Test/hour120.mp4'
reader = imageio.get_reader(input_movie)

writer = imageio.get_writer(input_movie[:-4]+'_nocv2.mp4', fps=reader.get_meta_data()['fps'], codec='libx264', quality=5)
writercv2 = imageio.get_writer(input_movie[:-4]+'_cv2.mp4', fps=reader.get_meta_data()['fps'], codec='libx264', quality=5)

a = reader.iter_data()
frames = []
framescv2 = []
c = imageio_ffmpeg.count_frames_and_secs(input_movie)
for i in range(500):
    frame = np.uint8(next(a))
    framecv2 = cv2.cvtColor(np.uint8(next(a)), cv2.COLOR_BGR2GRAY)
    frames.append(np.resize(frame, (960, 960, 1)))
    framescv2.append(framecv2)
    writer.append_data(frames[i])
    writercv2.append_data(framescv2[i])
   
    
#resized = np.resize(frame[:,:,1], (960, 960, 1))

#rframe = np.pad(frame[:,:,1], ((210, 210),(0, 0)), 'constant')
#rframe = np.resize(rframe, (960, 960, 1))
#
#sidepad = np.pad(frame[:,:,1], ((0, 420),(0, 0)), 'constant')
#sidepad = np.resize(sidepad, (960, 960, 1))


#imageio.imwrite('~/Desktop/frame.png', frame)
#imageio.imwrite('~/Desktop/framecv2.png', framecv2)
#imageio.imwrite('~/Desktop/rframe.png', rframe)
#imageio.imwrite('~/Desktop/sidepad.png', sidepad)


#zeroframe = np.zeros((960, 960, 3)) #Creates array of wanted dimensions filled with zeros
#zeroframe[:frame.shape[0],:frame.shape[1]] = frame #Pastes frame on top of zeroframe
#imageio.imwrite('~/Desktop/zeroframe.png', zeroframe)
#imageio.imwrite('~/Desktop/frame.png', frame)

