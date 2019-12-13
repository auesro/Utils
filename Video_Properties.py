# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:58:14 2019

@author: AugustoER
"""

import cv2

capture_properties = ['CAP_PROP_POS_MSEC', 'CAP_PROP_POS_FRAMES', 'CAP_PROP_POS_AVI_RATIO', 'CAP_PROP_FRAME_WIDTH', 'CAP_PROP_FRAME_HEIGHT', 'CAP_PROP_FPS', 'CAP_PROP_FOURCC', 'CAP_PROP_FRAME_COUNT', 'CAP_PROP_FORMAT', 'CAP_PROP_MODE', 'CAP_PROP_BRIGHTNESS', 'CAP_PROP_CONTRAST', 'CAP_PROP_SATURATION', 'CAP_PROP_HUE', 'CAP_PROP_GAIN', 'CAP_PROP_EXPOSURE', 'CAP_PROP_CONVERT_RGB', 'CAP_PROP_WHITE_BALANCE_BLUE_U', 'CAP_PROP_RECTIFICATION', 'CAP_PROP_MONOCHROME', 'CAP_PROP_SHARPNESS', 'CAP_PROP_AUTO_EXPOSURE', 'CAP_PROP_GAMMA', 'CAP_PROP_TEMPERATURE', 'CAP_PROP_TRIGGER', 'CAP_PROP_TRIGGER_DELAY', 'CAP_PROP_WHITE_BALANCE_RED_V', 'CAP_PROP_ZOOM', 'CAP_PROP_FOCUS', 'CAP_PROP_GUID', 'CAP_PROP_ISO_SPEED', 'CAP_PROP_BACKLIGHT', 'CAP_PROP_PAN', 'CAP_PROP_TILT', 'CAP_PROP_ROLL', 'CAP_PROP_IRIS', 'CAP_PROP_SETTINGS', 'CAP_PROP_BUFFERSIZE', 'CAP_PROP_AUTOFOCUS']

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

print(cv2.__version__)

#camera = cv2.VideoCapture('C:/Users/AugustoER/Desktop/18349(Right)18351(Left).wmv')
#camera = cv2.VideoCapture('C:/Users/AugustoER/Desktop/hour001.mp4')
camera = cv2.VideoCapture('C:/Users/AugustoER/Desktop/hour001.wmv')


#codec = 0x47504A4D # MJPG
#codec = 844715353.0 # YUY2
#codec = 1196444237.0 # MJPG

#print 'fourcc:', decode_fourcc(codec)

print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(camera.get(cv2.CAP_PROP_FPS))
CC = int(camera.get(cv2.CAP_PROP_FOURCC))
print('fourcc:', decode_fourcc(CC))

for i in range(38):
    print(i, capture_properties[i], camera.get(i))

camera.release()
cv2.destroyAllWindows()