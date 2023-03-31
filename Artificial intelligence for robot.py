#Artificial intelligence for robot
import cv2
import numpy as np
import time
import pyautogui as pag
san = 0
cap=cv2.VideoCapture(0)
hand_cascade=cv2.CascadeClassifier("haarcascade_lowerbody.xml")
prev_x,prev_y=0,0
count=0
while True:
	ret, frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	hands=hand_cascade.detectMultiScale(gray,1.2,5)
	for x,y,w,h in hands:
		#time.time()
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		next_x,next_y=x,y
		if count>0:
			diff_x,diff_y=((next_x-prev_x),(next_y-prev_y))
			if diff_x>7:
				print ("left")
				pag.moveRel(-85,0)
				san = 0
			elif diff_x<-7:
				print ("right")
				pag.moveRel(85,0)
				san = 0
			if diff_y>7:
				print ("down")
				pag.moveRel(0,85)
				san = 0
			elif diff_y<-7:
				print ("up")
				pag.moveRel(0,-85)
				san = 0
			if diff_y<7 and diff_y>-7 and diff_x>-7 and diff_x<7:
				san = san + 1
				if san == 50:
					print('click')
					san = 0
					pag.doubleClick()
		prev_x,prev_y=next_x,next_y
	#time.time()
	count+=1
	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
