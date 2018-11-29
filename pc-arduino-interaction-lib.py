import cv2 
import numpy as np
import serial
import time
from random import randrange
bin = ['a','b']


##try:
##	ser = serial.Serial('/dev/ttyACM0', 9600)
#except:
##	ser = serial.Serial('/dev/ttyACM1', 9600)


# Create video stream
Cap_video = cv2.VideoCapture(0)

# Background Image
ret,Cap_img_Background=Cap_video.read()
Cap_img_Background=cv2.cvtColor(Cap_img_Background, cv2.COLOR_BGR2GRAY)

while ret:
	time.sleep(0.5)
	ret, frame = Cap_video.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	# Absolute Difference
	diff = cv2.absdiff(Cap_img_Background, frame)
	
	# Threshold
	ret,thresh = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)
	thresh_old = thresh
	
	# Find contours
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	avg = np.average(im2)
	print avg
	
	if avg > 170:
		print("object found")
		#ser.write(bin[randrange(2)])
	
	
	cv2.imshow('frame',im2)
	if cv2.waitKey(1) == 27:
		break
		
   	
