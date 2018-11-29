#!/usr/bin/env python
# coding: utf-8




import cv2
import numpy as np
import scipy.ndimage


#Capturing Video through web camera of the pc
Cap_video=cv2.VideoCapture(0)

i=0
while(i<20):
	i+=1

ret,Cap_img_Background=Cap_video.read()# Considering the first image as the base case / Background image

Cap_img_Background=cv2.cvtColor(Cap_img_Background, cv2.COLOR_BGR2GRAY)#Converting it to GrayScale Image
Cap_img_Background=scipy.ndimage.filters.gaussian_filter(Cap_img_Background,1.5)# Applying Gaussian filter inorder to reduce noise and blur accordingly 


ret,Cap_img=Cap_video.read()  #first image after the Base Case for Comparison


#Calculating the difference in the captured images inorder to observe changes in the environment

def calculate():
	Cap_img1=scipy.ndimage.filters.gaussian_filter(Cap_img,0.01)

	x=Cap_img_Background-Cap_img1
	x=np.absolute(x)#Considering Absolute values inorder to avoid any sort of outliers

	row_count=0
	col_count=0
	flag=0

	import pdb; pdb.set_trace();
	for rows in range(row_count,480):
		for columns in range(col_count,640):
			#col_count=col_count+1	
			if 245<=x[rows][columns]<=255 or x[rows][columns]==0:#Average range hardcoded after observing the images.
				flag=flag+1 #Image Required
			#row_count=row_count+3
	import pdb; pdb.set_trace();
	if(flag<290000):
		print("no object")
	else:
		print("object")
	
	#cv2.imshow('Cap_img_Background',Cap_img_Background)
	#cv2.imshow('Cap_img',Cap_img)
	#cv2.imshow('x',np.absolute(x))
	
	#cv2.waitKey(1)
			
	
	
	
	


	
##Function to Capture IMages Continousuly ,WaitKey Can be implemented inorder to break the code a press of  a key.
count=0
x=2
while count<x:
	count=count+1
	if(count==(x-1)):	
		ret,Cap_img=Cap_video.read()
		Cap_img=cv2.cvtColor(Cap_img,cv2.COLOR_BGR2GRAY)
    		calculate()
		count=0







