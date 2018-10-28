import cv2
import numpy as np
 
def nothing(x):
    pass
 
cap = cv2.VideoCapture("/home/ehhewng/Videos/GH010043.MP4") #0)
cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)
 
 
frame_num = 0

while True:
    ret, frame = cap.read()
    frame_num = frame_num + 1
    if frame_num > 100:
        cap.release()
        frame_num = 0
        cap = cv2.VideoCapture("/home/ehhewng/Videos/GH010043.MP4")

    if not ret:
        continue
    frame = cv2.resize(frame, (640,360))
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
 
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
 
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    dilated = cv2.dilate(mask, np.ones((3,3),np.uint8), iterations=3)

    result = cv2.bitwise_and(frame, frame, mask=dilated)
 
    cv2.imshow("frame", frame)
    cv2.imshow("mask", dilated)
    cv2.imshow("result", result)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

