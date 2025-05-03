import RPi.GPIO as GPIO
import time
import datetime
import os
from picamera2 import Picamera2, Preview
from datetime import datetime

import cv2

camera = Picamera2()

cam_conf = camera.create_preview_configuration()
camera.configure(cam_conf)

camera.start_preview(Preview.QTGL)
camera.start()1

now = datetime.now().strftime("%y-%m-%d")
frame = camera.capture_array()
cv2.putText(frame, now, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
while(1):
    time.sleep(2)

