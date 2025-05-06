from time import *
import tkinter as tk
import os
from picamera2 import Picamera2, Preview
import numpy as numpy
###EXPERIMENAL:
import cv2
colour = (255,0,0,255)
origin = (0,30)
font = cv2.FONT_HERSHEY_PLAIN
scale = 2
thickness = 2
###

WIDTH = 640
HEIGHT = 480

CAM_WIDTH = 2048
CAM_HEIGHT = 1536

window = tk.Tk()
window.title("Test")
frame1 = tk.Frame(master = window, bg = "black")
frame1.pack(fill = tk.BOTH, expand=True)
label1 = tk.Label(text="Hello welcome to my camera!", master =frame1, foreground = "white", background = "black")
label1.pack()
#window.update()

camera = Picamera2()

cam_configure = camera.create_preview_configuration({"size": (CAM_WIDTH, CAM_HEIGHT)})
camera.configure(cam_configure)


camera.start_preview(Preview.QTGL, x=0, y=0, width=WIDTH, height=HEIGHT)
camera.start()

overlay = numpy.zeros((300, 400, 4), dtype=numpy.uint8) #height, width, pixels (RGBA) using 4:3 aspect ratio

overlay[100, :] = (0, 0, 0, 10) # assign certain width & height to an RGBA value
overlay[200, :] = (0, 0, 0, 10) # assign certain width & height to an RGBA value
overlay[:, 133] = (0, 0, 0, 10) # assign certain width & height to an RGBA value
overlay[:, 266] = (0, 0, 0, 10) # assign certain width & height to an RGBA value
###
text = "Recording"
cv2.putText(overlay, text, origin, font, scale, colour, thickness)
###
camera.set_overlay(overlay)
sleep(1)
camera.capture_file("testWithOverlay.jpg")
window.mainloop()

"""
iteration = 0
while(1):
	iteration += 1
	window.update()
	sleep(1)
	camera.start_preview(Preview.QTGL, x=0, y=0, width=WIDTH, height=HEIGHT)
	camera.start()
	camera.capture_file("test_%s.jpg" % iteration)
	sleep(5)
	camera.stop()
	camera.stop_preview()
	sleep(5)
"""
