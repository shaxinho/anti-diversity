import numpy as np
import cv2
import spidev

def get_green_limits():
	
	boundaries = [([50,25,25], [70,255,255]),]
	
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")
	
	return lower, upper

def get_red_limits():
	boundaries = [([51,87,111], [180,255,255]),]
	
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")
		
	
	return lower, upper
	
def get_black_limits():
	boundaries = [([0,0,0], [64,64,64]),]
	
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")
	
	return lower, upper
