<h1> anti-diversity </h1>
<h3> Engineering materials </h3>
<p> This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2023. </p>

<h3> Content </h3>

* `t-photos` contains 2 photos of the team.
* `v-photos` contains 6 photos of the vehicle (from every side, from top and bottom).
* `video` contains the video.md file with the link to a video where driving demonstration exists.
* `schemes` contains one schematic diagram in form of PDF of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed to participate in the competition

<h3> Introduction </h3>

1. To start, several libraries, including OpenCV, Numpy and Pillow should be installed! <br> 


Use the command below to install the packages. <br>
`$ pip install -r requirements.txt`

2. Set up connection between Raspberry Pi and Arduino via "serial" package.
```
import serial

usbCom = serial.Serial('/dev/ttyACM0', 256000, timeout=0.05)
time.sleep(1)
usbCom.flush()
```

3. Setting up the resolution for the camera (by default it has 200px height and 200px width). <br>
`cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200);` <br>
`cap.set(cv2.CAP_PROP_FRAME_WIDTH, 200);`

4. Camera is then turned on in an infinite loop, reading for red, green and black colors in particularly selected range (e.g. black color is ranging from [0,0,0] to [64,64,64]), which means that colors in a specific range will be detected by our program. <br>
<h5>Note: Open util.py to change the range (boundaries) of the colors.</h5> 

`red = cv2.inRange(hsvImage, lowerLimitRed, upperLimitRed)` <br>
`green = cv2.inRange(hsvImage, lowerLimitGreen, upperLimitGreen)` <br>
`black = cv2.inRange(hsvImage, lowerLimitBlack, upperLimitBlack)`

5. Creating a mask for every color that is going to be read (Here is the example for the red color only).

`maskRed = Image.fromarray(red)` <br>
`maskR = maskRed.getbbox()`

6. Finding contours and bounding the red/green/black colored object (Here is the example for the red color only).
```
(contours, hierarchy)=cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if (area>300):
			x,y,w,h = cv2.boundingRect(contour)
			frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
			cv2.putText(frame, "RED COLOR", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
```

7. Check if the color is detected then send a name of the color to Arduino (Here is the example for the red color only).
```
usbCom.write(b"red")
line = usbCom.readline().decode('utf-8').rstrip()
time.sleep(1)
```
