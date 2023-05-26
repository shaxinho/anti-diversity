import cv2
from util import get_green_limits, get_red_limits, get_black_limits
from PIL import Image
import numpy as np
import serial
import time

usbCom = serial.Serial('/dev/ttyACM0', 256000, timeout=0.05)
time.sleep(1)
usbCom.flush()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200);
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200);
while True:
	ret, frame = cap.read()
	usbCom.open
	
	hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lowerLimitRed, upperLimitRed = get_red_limits()
	lowerLimitGreen, upperLimitGreen = get_green_limits()
	lowerLimitBlack, upperLimitBlack = get_black_limits()
	
	red = cv2.inRange(hsvImage, lowerLimitRed, upperLimitRed)
	green = cv2.inRange(hsvImage, lowerLimitGreen, upperLimitGreen)
	black = cv2.inRange(hsvImage, lowerLimitBlack, upperLimitBlack)
	
	maskRed = Image.fromarray(red)
	maskR = maskRed.getbbox()
	
	maskGreen = Image.fromarray(green)
	maskG = maskGreen.getbbox()
	
	maskBlack = Image.fromarray(black)
	maskB = maskBlack.getbbox()
	
	kernal = np.ones((5,5), "uint8")
	
	red = cv2.dilate(red, kernal)
	res = cv2.bitwise_and(frame, frame, mask=red)
	
	green = cv2.dilate(green, kernal)
	res1 = cv2.bitwise_and(frame, frame, mask=green)
	
	black = cv2.dilate(black, kernal)
	res2 = cv2.bitwise_and(frame, frame, mask=black)
	
	(contours, hierarchy)=cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if (area>300):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
			cv2.putText(frame, "RED COLOR", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			
			
	(contours, hierarchy)=cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if (area>300):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
			cv2.putText(frame, "GREEN COLOR", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))
			
	(contours, hierarchy)=cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if (area>300):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,0), 2)
			cv2.putText(frame, "BLACK COLOR", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0))
	
	if maskR != None:
		usbCom.write(b"red")
		line = usbCom.readline().decode('utf-8').rstrip()
		print(line)
		time.sleep(1)
	elif maskG != None:
		usbCom.write(b"green")
		line = usbCom.readline().decode('utf-8').rstrip()
		print(line)
		time.sleep(1)
	elif maskB != None:
		usbCom.write(b"black")
		line = usbCom.readline().decode('utf-8').rstrip()
		print(line)
		time.sleep(1)
	else:
		usbCom.write(b"None")
		line = usbCom.readline().decode('utf-8').rstrip()
		print(line)
		time.sleep(1)

	cv2.imshow('frame', frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release() 

cv2.destroyAllWindows()
	
