import cv2
frameWidth=720
frameHeight=1080
cap=cv2.VideoCapture("resources/test_video.mp4")

while True:
	success,img=cap.read()
	img=cv2.resize(img,(frameWidth,frameHeight))
	cv2.imshow("Result",img)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
