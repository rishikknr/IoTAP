import cv2
frameWidth=640
frameHeight=400
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,40)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame")
        break
    
    cv2.imshow("Result", img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        cv2.imwrite("/home/harsha/Desktop/iotaplab/week5/test.jpg", img)
        print("Image saved as test.jpg")
