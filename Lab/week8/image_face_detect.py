import cv2
#pixels = cv2.imread('test.jpg')
pixels = cv2.imread('test2.jpg')
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
bboxes = classifier.detectMultiScale(pixels)
for box in bboxes:
	x, y, width, height = box
	x1, y1 = x + width, y + height
	cv2.rectangle(pixels, (x, y), (x1, y1), (0,0,255), 1)

cv2.imwrite('output2.jpg', pixels)
